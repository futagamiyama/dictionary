import { supabase, Word } from '@/lib/supabase';
import { notFound } from 'next/navigation';
import Link from 'next/link';
import DeleteButton from './DeleteButton';
import SearchBox from '@/app/components/SearchBox';

async function getWord(word: string): Promise<Word> {
  const { data, error } = await supabase
    .from('words')
    .select('*, examples(id, sentence, translation)')
    .eq('word', decodeURIComponent(word))
    .single();
  if (error || !data) notFound();
  return data;
}

export default async function WordPage({ params }: { params: Promise<{ word: string }> }) {
  const { word: slug } = await params;
  const w = await getWord(slug);

  return (
    <div className="min-h-screen flex flex-col">

      {/* Header */}
      <header className="border-b px-6 py-3 flex items-center justify-between gap-4">
        <Link href="/" className="text-sm text-gray-400 hover:text-gray-600 shrink-0">← List</Link>
        <SearchBox />
        <Link href="/new" className="bg-black text-white text-sm rounded-lg px-4 py-2 hover:bg-gray-800 transition-colors shrink-0">+ Add</Link>
      </header>

      {/* Body */}
      <div className="flex flex-1 overflow-hidden">

        {/* Main */}
        <main className="flex-1 overflow-y-auto p-8">
          <div className="group relative">
            <div className="flex items-baseline gap-3">
              <h1 className="text-4xl font-bold cursor-default">{w.word}</h1>
              {w.part_of_speech && (
                <span className="text-gray-500">{w.part_of_speech}</span>
              )}
              {w.level && (
                <span className="text-xs bg-gray-100 text-gray-500 rounded px-2 py-0.5">Lv.{w.level}</span>
              )}
              {w.rank && (
                <span className="text-xs bg-blue-50 text-blue-500 rounded px-2 py-0.5">#{w.rank}</span>
              )}
            </div>
            {w.pronunciation && (
              <p className="text-gray-400 text-lg mt-1">[{w.pronunciation}]</p>
            )}
            <div className="absolute left-0 top-full mt-1 w-full opacity-0 group-hover:opacity-100 transition-opacity duration-200 pointer-events-none z-10">
              <p className="whitespace-pre-wrap text-sm text-blue-800 bg-blue-50 rounded px-3 py-2">{w.meaning}</p>
            </div>
          </div>

          {w.examples && w.examples.length > 0 && (
            <ul className="mt-8 space-y-3">
              {w.examples.map((ex) => (
                <li key={ex.id} className="group relative border-l-4 border-gray-200 pl-4">
                  <span className="text-gray-500 italic cursor-default">{ex.sentence}</span>
                  {ex.translation && (
                    <div className="absolute left-4 top-full mt-1 right-0 opacity-0 group-hover:opacity-100 transition-opacity duration-200 pointer-events-none z-10">
                      <p className="text-sm text-blue-800 bg-blue-50 rounded px-3 py-2">{ex.translation}</p>
                    </div>
                  )}
                </li>
              ))}
            </ul>
          )}
        </main>

        {/* Right pane */}
        <aside className="w-56 border-l p-6 shrink-0 flex flex-col gap-4 text-sm text-gray-500">
          {w.rank && (
            <div>
              <p className="text-xs text-gray-400 uppercase tracking-wide mb-1">Frequency Rank</p>
              <p className="text-2xl font-bold text-blue-600">#{w.rank}</p>
              <p className="text-xs text-gray-400">/ 25,000</p>
            </div>
          )}
          {w.level && (
            <div>
              <p className="text-xs text-gray-400 uppercase tracking-wide mb-1">Level</p>
              <p className="text-2xl font-bold text-gray-700">{w.level}</p>
            </div>
          )}
          {w.part_of_speech && (
            <div>
              <p className="text-xs text-gray-400 uppercase tracking-wide mb-1">Part of Speech</p>
              <p>{w.part_of_speech}</p>
            </div>
          )}
          {w.pronunciation && (
            <div>
              <p className="text-xs text-gray-400 uppercase tracking-wide mb-1">Pronunciation</p>
              <p>[{w.pronunciation}]</p>
            </div>
          )}
          {w.examples && (
            <div>
              <p className="text-xs text-gray-400 uppercase tracking-wide mb-1">Examples</p>
              <p>{w.examples.length}</p>
            </div>
          )}
        </aside>

      </div>

      {/* Footer */}
      <footer className="border-t px-6 py-3 flex justify-end gap-2">
        <Link href={`/dictionary/${slug}/edit`} className="text-sm border rounded-lg px-4 py-2 hover:bg-gray-50 transition-colors">Edit</Link>
        <DeleteButton id={w.id} word={w.word} />
      </footer>

    </div>
  );
}
