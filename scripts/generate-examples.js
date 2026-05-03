#!/usr/bin/env node

// Change to project root to access node_modules
const path = require('path');
process.chdir(path.resolve(__dirname, '../dictionary-next'));

const { createClient } = require('@supabase/supabase-js');
const Anthropic = require('@anthropic-ai/sdk');

const supabaseUrl = 'https://tvklrujikuanxdddyfcx.supabase.co';
const supabaseKey = process.env.SUPABASE_SERVICE_ROLE_KEY;
const anthropicKey = process.env.ANTHROPIC_API_KEY;

if (!supabaseKey) {
  console.error('SUPABASE_SERVICE_ROLE_KEY environment variable is not set');
  process.exit(1);
}

if (!anthropicKey) {
  console.error('ANTHROPIC_API_KEY environment variable is not set');
  process.exit(1);
}

const supabase = createClient(supabaseUrl, supabaseKey);
const anthropic = new Anthropic({ apiKey: anthropicKey });

async function generateExamplesForWord(word) {
  const prompt = `Generate 3 example sentences for the word "${word}" in simple English suitable for news articles. Each sentence should be a common usage example.

Format your response as JSON array with this structure:
[
  {
    "sentence": "example sentence 1",
    "translation": "Japanese translation 1"
  },
  {
    "sentence": "example sentence 2",
    "translation": "Japanese translation 2"
  },
  {
    "sentence": "example sentence 3",
    "translation": "Japanese translation 3"
  }
]

Make sure:
- Each sentence uses simple vocabulary (news article level)
- Translations are accurate Japanese
- Each sentence is 10-20 words long
- Return ONLY the JSON array, no other text`;

  try {
    const message = await anthropic.messages.create({
      model: 'claude-opus-4-7',
      max_tokens: 500,
      messages: [
        {
          role: 'user',
          content: prompt
        }
      ]
    });

    const responseText = message.content[0].type === 'text' ? message.content[0].text : '';
    const examples = JSON.parse(responseText);
    return examples;
  } catch (err) {
    console.error(`Error generating examples for "${word}":`, err.message);
    return null;
  }
}

async function main() {
  try {
    // Fetch all words in the rank range
    const { data: words, error } = await supabase
      .from('words')
      .select('id, word')
      .gte('rank', 4160)
      .lte('rank', 4179)
      .order('rank', { ascending: true });

    if (error) {
      console.error('Error fetching words:', error);
      process.exit(1);
    }

    console.log(`Found ${words.length} words to process`);

    let processed = 0;
    let skipped = 0;

    // Process each word with rate limiting
    for (const wordObj of words) {
      const examples = await generateExamplesForWord(wordObj.word);

      if (!examples || examples.length === 0) {
        skipped++;
        console.log(`⚠ Skipped ${wordObj.word} (generation failed)`);
        continue;
      }

      // Insert examples into database
      for (const example of examples) {
        const { error: insertError } = await supabase.from('examples').insert({
          word_id: wordObj.id,
          sentence: example.sentence,
          translation: example.translation
        });

        if (insertError) {
          console.error(`Error inserting example for ${wordObj.word}:`, insertError);
        } else {
          console.log(`✓ ${wordObj.word}: "${example.sentence}"`);
        }
      }

      processed++;

      // Rate limiting: wait 1 second between API calls
      if (processed < words.length) {
        await new Promise(resolve => setTimeout(resolve, 1000));
      }
    }

    console.log(`\n✅ Completed! Processed: ${processed}, Skipped: ${skipped}`);
  } catch (err) {
    console.error('Error:', err);
    process.exit(1);
  }
}

main();
