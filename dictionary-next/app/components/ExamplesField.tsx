'use client';

import { useState } from 'react';

type ExampleEntry = { sentence: string; translation: string };

export default function ExamplesField({ initial = [] }: { initial?: ExampleEntry[] }) {
  const [examples, setExamples] = useState<ExampleEntry[]>(
    initial.length > 0 ? initial : [{ sentence: '', translation: '' }]
  );

  const update = (i: number, field: keyof ExampleEntry, value: string) =>
    setExamples((prev) => prev.map((e, idx) => idx === i ? { ...e, [field]: value } : e));

  const add = () => setExamples((prev) => [...prev, { sentence: '', translation: '' }]);

  const remove = (i: number) => setExamples((prev) => prev.filter((_, idx) => idx !== i));

  return (
    <div className="space-y-3">
      <label className="block text-sm font-medium">Examples</label>
      {examples.map((ex, i) => (
        <div key={i} className="border rounded-lg p-3 space-y-2">
          <div className="flex gap-2">
            <textarea
              name="examples[]"
              rows={2}
              placeholder="英文"
              value={ex.sentence}
              onChange={(e) => update(i, 'sentence', e.target.value)}
              className="flex-1 border rounded-lg px-3 py-2 focus:outline-none focus:ring-2 focus:ring-black"
            />
            {examples.length > 1 && (
              <button type="button" onClick={() => remove(i)} className="text-gray-400 hover:text-red-500 text-lg px-1 self-start">×</button>
            )}
          </div>
          <input
            name="translations[]"
            placeholder="Translation (shown on hover)"
            value={ex.translation}
            onChange={(e) => update(i, 'translation', e.target.value)}
            className="w-full border rounded-lg px-3 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-black"
          />
        </div>
      ))}
      <button type="button" onClick={add} className="text-sm text-gray-500 hover:text-black">+ Add Example</button>
    </div>
  );
}
