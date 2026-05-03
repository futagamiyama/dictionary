#!/usr/bin/env python3

import os
import json
import time
from pathlib import Path
from anthropic import Anthropic
from supabase import create_client, Client
from dotenv import load_dotenv

# Load environment from .env.local
env_path = Path(__file__).parent / "dictionary-next" / ".env.local"
if env_path.exists():
    load_dotenv(env_path)

# Initialize clients
supabase_url = "https://tvklrujikuanxdddyfcx.supabase.co"
supabase_key = os.getenv("SUPABASE_SERVICE_ROLE_KEY") or os.getenv("NEXT_PUBLIC_SUPABASE_ANON_KEY")
anthropic_key = os.getenv("ANTHROPIC_API_KEY")

if not supabase_key:
    print("Error: SUPABASE_SERVICE_ROLE_KEY or NEXT_PUBLIC_SUPABASE_ANON_KEY not set")
    exit(1)

if not anthropic_key:
    print("Error: ANTHROPIC_API_KEY not set")
    exit(1)

supabase: Client = create_client(supabase_url, supabase_key)
client = Anthropic(api_key=anthropic_key)

def generate_examples_for_word(word: str) -> list | None:
    """Generate 3 example sentences for a word using Claude"""
    prompt = f"""Generate 3 example sentences for the word "{word}" in simple English suitable for news articles.

Format your response as JSON array with this structure:
[
  {{
    "sentence": "example sentence 1",
    "translation": "Japanese translation 1"
  }},
  {{
    "sentence": "example sentence 2",
    "translation": "Japanese translation 2"
  }},
  {{
    "sentence": "example sentence 3",
    "translation": "Japanese translation 3"
  }}
]

Make sure:
- Each sentence uses simple vocabulary (news article level)
- Translations are accurate Japanese
- Each sentence is 10-20 words long
- Return ONLY the JSON array, no other text"""

    try:
        message = client.messages.create(
            model="claude-opus-4-7",
            max_tokens=500,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        response_text = message.content[0].text
        examples = json.loads(response_text)
        return examples
    except Exception as e:
        print(f"Error generating examples for '{word}': {e}")
        return None

def main():
    # Fetch words in rank range 5058-5077 (20 words)
    try:
        response = supabase.table("words").select("id, word").gte("rank", 5058).lte("rank", 5077).order("rank", desc=False).execute()
        words = response.data
    except Exception as e:
        print(f"Error fetching words: {e}")
        exit(1)

    print(f"Found {len(words)} words to process")

    processed = 0
    skipped = 0

    # Process each word
    for word_obj in words:
        word_id = word_obj["id"]
        word = word_obj["word"]

        examples = generate_examples_for_word(word)

        if not examples or len(examples) == 0:
            skipped += 1
            print(f"⚠ Skipped {word} (generation failed)")
            continue

        # Insert examples
        for example in examples:
            try:
                supabase.table("examples").insert({
                    "word_id": word_id,
                    "sentence": example["sentence"],
                    "translation": example["translation"]
                }).execute()
                print(f'✓ {word}: "{example["sentence"]}"')
            except Exception as e:
                print(f"Error inserting example for {word}: {e}")

        processed += 1

        # Rate limiting
        if processed < len(words):
            time.sleep(1)

    print(f"\n✅ Completed! Processed: {processed}, Skipped: {skipped}")

if __name__ == "__main__":
    main()
