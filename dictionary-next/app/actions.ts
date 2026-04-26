'use server';

import { supabase } from '@/lib/supabase';
import { redirect } from 'next/navigation';

function extractExamples(formData: FormData): { sentence: string; translation: string | null }[] {
  const sentences = formData.getAll('examples[]').map((v) => v.toString().trim());
  const translations = formData.getAll('translations[]').map((v) => v.toString().trim() || null);
  return sentences
    .map((sentence, i) => ({ sentence, translation: translations[i] ?? null }))
    .filter((r) => r.sentence !== '');
}

export async function addWord(formData: FormData) {
  const word = formData.get('word')?.toString().trim();
  const meaning = formData.get('meaning')?.toString().trim();
  const part_of_speech = formData.get('part_of_speech')?.toString().trim() || null;
  const pronunciation = formData.get('pronunciation')?.toString().trim() || null;
  const levelRaw = formData.get('level')?.toString().trim();
  const level = levelRaw ? parseInt(levelRaw, 10) : null;
  const examples = extractExamples(formData);

  if (!word || !meaning) throw new Error('word と meaning は必須です');

  const { data, error } = await supabase.from('words').insert({ word, meaning, part_of_speech, pronunciation, level }).select('id').single();
  if (error || !data) throw new Error(error?.message ?? 'insert failed');

  if (examples.length > 0) {
    const rows = examples.map(({ sentence, translation }) => ({ word_id: data.id, sentence, translation }));
    const { error: exError } = await supabase.from('examples').insert(rows);
    if (exError) throw new Error(exError.message);
  }

  redirect(`/dictionary/${encodeURIComponent(word)}`);
}

export async function updateWord(id: string, formData: FormData) {
  const word = formData.get('word')?.toString().trim();
  const meaning = formData.get('meaning')?.toString().trim();
  const part_of_speech = formData.get('part_of_speech')?.toString().trim() || null;
  const pronunciation = formData.get('pronunciation')?.toString().trim() || null;
  const levelRaw = formData.get('level')?.toString().trim();
  const level = levelRaw ? parseInt(levelRaw, 10) : null;
  const examples = extractExamples(formData);

  if (!word || !meaning) throw new Error('word と meaning は必須です');

  const { error } = await supabase.from('words').update({ word, meaning, part_of_speech, pronunciation, level }).eq('id', id);
  if (error) throw new Error(error.message);

  await supabase.from('examples').delete().eq('word_id', id);
  if (examples.length > 0) {
    const rows = examples.map(({ sentence, translation }) => ({ word_id: id, sentence, translation }));
    const { error: exError } = await supabase.from('examples').insert(rows);
    if (exError) throw new Error(exError.message);
  }

  redirect(`/dictionary/${encodeURIComponent(word)}`);
}

export async function deleteWord(id: string) {
  const { error } = await supabase.from('words').delete().eq('id', id);
  if (error) throw new Error(error.message);
  redirect('/');
}
