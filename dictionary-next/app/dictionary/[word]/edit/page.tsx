import { supabase, Word } from '@/lib/supabase';
import { notFound } from 'next/navigation';
import Link from 'next/link';
import { updateWord } from '@/app/actions';
import ExamplesField from '@/app/components/ExamplesField';

async function getWord(word: string): Promise<Word> {
  const { data, error } = await supabase
    .from('words')
    .select('*, examples(sentence, translation)')
    .eq('word', decodeURIComponent(word))
    .single();
  if (error || !data) notFound();
  return data;
}

export default async function EditWordPage({ params }: { params: Promise<{ word: string }> }) {
  const { word: slug } = await params;
  const w = await getWord(slug);
  const action = updateWord.bind(null, w.id);
  const initialExamples = (w.examples ?? []).map((e) => ({ sentence: e.sentence, translation: e.translation ?? '' }));

  return (
    <main className="max-w-2xl mx-auto px-4 py-10">
      <Link href={`/dictionary/${slug}`} className="text-sm text-gray-400 hover:text-gray-600">← Detail</Link>
      <h1 className="text-2xl font-bold mt-6 mb-8">Edit Word</h1>
      <form action={action} className="space-y-5">
        <div>
          <label className="block text-sm font-medium mb-1">Word *</label>
          <input name="word" required defaultValue={w.word} className="w-full border rounded-lg px-3 py-2 focus:outline-none focus:ring-2 focus:ring-black" />
        </div>
        <div>
          <label className="block text-sm font-medium mb-1">Meaning *</label>
          <textarea name="meaning" required rows={3} defaultValue={w.meaning} className="w-full border rounded-lg px-3 py-2 focus:outline-none focus:ring-2 focus:ring-black" />
        </div>
        <div className="flex gap-4">
          <div className="flex-1">
            <label className="block text-sm font-medium mb-1">Part of Speech</label>
            <input name="part_of_speech" defaultValue={w.part_of_speech ?? ''} className="w-full border rounded-lg px-3 py-2 focus:outline-none focus:ring-2 focus:ring-black" placeholder="noun / verb / adjective ..." />
          </div>
          <div className="w-32">
            <label className="block text-sm font-medium mb-1">Level (1–20)</label>
            <input name="level" type="number" min={1} max={20} defaultValue={w.level ?? ''} className="w-full border rounded-lg px-3 py-2 focus:outline-none focus:ring-2 focus:ring-black" />
          </div>
        </div>
        <div>
          <label className="block text-sm font-medium mb-1">Pronunciation</label>
          <input name="pronunciation" defaultValue={w.pronunciation ?? ''} className="w-full border rounded-lg px-3 py-2 focus:outline-none focus:ring-2 focus:ring-black" placeholder="e.g. dɔːɡ" />
        </div>
        <ExamplesField initial={initialExamples} />
        <button type="submit" className="w-full bg-black text-white rounded-lg py-2 hover:bg-gray-800 transition-colors">
          Save
        </button>
      </form>
    </main>
  );
}
