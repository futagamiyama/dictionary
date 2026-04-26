'use client';

import { useState, useEffect, useRef } from 'react';
import { useRouter } from 'next/navigation';
import { supabase } from '@/lib/supabase';

type Result = { word: string; pronunciation: string | null };

export default function SearchBox() {
  const [query, setQuery] = useState('');
  const [results, setResults] = useState<Result[]>([]);
  const [open, setOpen] = useState(false);
  const router = useRouter();
  const ref = useRef<HTMLDivElement>(null);

  useEffect(() => {
    if (!query.trim()) { setResults([]); return; }
    const timer = setTimeout(async () => {
      const { data } = await supabase
        .from('words')
        .select('word, pronunciation')
        .ilike('word', `${query}%`)
        .order('word')
        .limit(8);
      setResults(data ?? []);
      setOpen(true);
    }, 150);
    return () => clearTimeout(timer);
  }, [query]);

  useEffect(() => {
    const handler = (e: MouseEvent) => {
      if (ref.current && !ref.current.contains(e.target as Node)) setOpen(false);
    };
    document.addEventListener('mousedown', handler);
    return () => document.removeEventListener('mousedown', handler);
  }, []);

  const go = (word: string) => {
    setQuery('');
    setOpen(false);
    router.push(`/dictionary/${encodeURIComponent(word)}`);
  };

  return (
    <div ref={ref} className="relative w-full max-w-sm">
      <input
        type="search"
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        onFocus={() => results.length > 0 && setOpen(true)}
        placeholder="Search words..."
        className="w-full border rounded-lg px-3 py-1.5 text-sm focus:outline-none focus:ring-2 focus:ring-black"
      />
      {open && results.length > 0 && (
        <ul className="absolute left-0 top-full mt-1 w-full bg-white border rounded-lg shadow-lg z-20 overflow-hidden">
          {results.map((r) => (
            <li key={r.word}>
              <button
                type="button"
                onMouseDown={() => go(r.word)}
                className="w-full text-left px-3 py-2 text-sm hover:bg-gray-50 flex items-baseline gap-2"
              >
                <span className="font-medium">{r.word}</span>
                {r.pronunciation && <span className="text-gray-400 text-xs">[{r.pronunciation}]</span>}
              </button>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}
