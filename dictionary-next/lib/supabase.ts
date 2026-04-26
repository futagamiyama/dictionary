import { createClient } from '@supabase/supabase-js';

export const supabase = createClient(
  process.env.NEXT_PUBLIC_SUPABASE_URL!,
  process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY!
);

export type Example = {
  id: string;
  word_id: string;
  sentence: string;
  translation: string | null;
  created_at: string;
};

export type Word = {
  id: string;
  word: string;
  meaning: string;
  part_of_speech: string | null;
  pronunciation: string | null;
  level: number | null;
  rank: number | null;
  created_at: string;
  examples?: Example[];
};
