import { supabase, Word } from '@/lib/supabase';
import { notFound } from 'next/navigation';
import Link from 'next/link';
import SearchBox from '@/app/components/SearchBox';

async function getWordsByRank(from: number, to: number): Promise<Word[]> {
  const { data, error } = await supabase
    .from('words')
    .select('*')
    .gte('rank', from)
    .lt('rank', to)
    .order('rank');
  if (error) throw new Error(error.message);
  return data ?? [];
}

export default async function RankPage({ params }: { params: Promise<{ startRank: string }> }) {
  const { startRank } = await params;
  const from = parseInt(startRank, 10);
  if (isNaN(from) || from < 1) notFound();
  const to = from + 100;

  const words = await getWordsByRank(from, to);

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

        {/* Word list */}
        <main className="flex-1 overflow-y-auto p-6">
          <h2 className="text-lg font-semibold mb-4 text-gray-700">
            Frequency Rank #{from} – #{to - 1}
          </h2>
          {words.length === 0 ? (
            <p className="text-gray-500">No words found in this rank range.</p>
          ) : (
            <ul>
              {words.map((w) => (
                <li key={w.id} className="border-b last:border-b-0">
                  <Link
                    href={`/dictionary/${encodeURIComponent(w.word)}`}
                    className="flex items-baseline gap-2 px-2 py-2.5 hover:bg-gray-50"
                  >
                    {w.rank && (
                      <span className="text-xs text-gray-400 w-12 shrink-0">#{w.rank}</span>
                    )}
                    <span className="text-base font-medium">{w.word}</span>
                    {w.part_of_speech && (
                      <span className="text-xs text-gray-400">{w.part_of_speech}</span>
                    )}
                    {w.level && (
                      <span className="text-xs text-gray-400">[lv{w.level}]</span>
                    )}
                  </Link>
                </li>
              ))}
            </ul>
          )}
        </main>

        {/* Right pane */}
        <aside className="w-56 border-l p-6 shrink-0 flex flex-col gap-4 text-sm text-gray-500">
          <div>
            <p className="text-xs text-gray-400 uppercase tracking-wide mb-1">Range</p>
            <p className="text-lg font-bold text-gray-700">#{from} – #{to - 1}</p>
          </div>
          <div>
            <p className="text-xs text-gray-400 uppercase tracking-wide mb-1">Words Found</p>
            <p className="text-2xl font-bold text-blue-600">{words.length}</p>
          </div>
          <div className="flex flex-col gap-2 mt-2">
            {from > 100 && (
              <Link
                href={`/rank/${from - 100}`}
                className="text-sm text-center border rounded-lg px-3 py-1.5 hover:bg-gray-50 transition-colors"
              >
                ← #{from - 100}–#{from - 1}
              </Link>
            )}
            <Link
              href={`/rank/${to}`}
              className="text-sm text-center border rounded-lg px-3 py-1.5 hover:bg-gray-50 transition-colors"
            >
              #{to}–#{to + 99} →
            </Link>
          </div>
        </aside>

      </div>

    </div>
  );
}
