import Link from 'next/link';
import { supabase, Word } from '@/lib/supabase';
import SearchBox from '@/app/components/SearchBox';

async function getWords(): Promise<Word[]> {
  const { data, error } = await supabase.from('words').select('*').order('word');
  if (error) throw new Error(error.message);
  return data ?? [];
}

export default async function Home() {
  const words = await getWords();

  return (
    <div className="min-h-screen flex flex-col">

      {/* Header */}
      <header className="border-b px-6 py-3 flex items-center justify-between gap-4">
        <h1 className="text-xl font-bold shrink-0">Dictionary</h1>
        <SearchBox />
        <Link href="/new" className="bg-black text-white text-sm rounded-lg px-4 py-2 hover:bg-gray-800 transition-colors shrink-0">+ Add</Link>
      </header>

      {/* Body */}
      <div className="flex flex-1 overflow-hidden">

        {/* Word list */}
        <main className="flex-1 overflow-y-auto p-6">
          {words.length === 0 ? (
            <p className="text-gray-500">No words found.</p>
          ) : (
            <ul>
              {words.map((w) => (
                <li key={w.id} className="border-b last:border-b-0">
                  <Link href={`/dictionary/${encodeURIComponent(w.word)}`} className="block px-2 py-2.5 hover:bg-gray-50 text-base font-medium">
                    {w.word}
                  </Link>
                </li>
              ))}
            </ul>
          )}
        </main>

        {/* Right pane */}
        <aside className="w-64 border-l p-6 flex flex-col gap-4 shrink-0">
          <div>
            <p className="text-xs text-gray-400 uppercase tracking-wide mb-1">Total</p>
            <p className="text-2xl font-bold">{words.length}</p>
          </div>
          <div>
            <p className="text-xs text-gray-400 uppercase tracking-wide mb-2">By Level</p>
            <ul className="space-y-1 text-sm text-gray-600">
              {Array.from(
                words.reduce((acc, w) => {
                  const lv = w.level ?? 0;
                  acc.set(lv, (acc.get(lv) ?? 0) + 1);
                  return acc;
                }, new Map<number, number>())
              )
                .sort(([a], [b]) => a - b)
                .map(([lv, count]) => (
                  <li key={lv} className="flex justify-between">
                    <span>{lv === 0 ? 'No level' : `Lv.${lv}`}</span>
                    <span className="text-gray-400">{count}</span>
                  </li>
                ))}
            </ul>
          </div>
        </aside>

      </div>

      {/* Footer */}
      <footer className="border-t px-6 py-3 text-xs text-gray-400 text-center">
        Dictionary App <span className="ml-2">ver 0.01</span>
      </footer>

    </div>
  );
}
