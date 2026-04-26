import Link from 'next/link';
import { addWord } from '@/app/actions';
import ExamplesField from '@/app/components/ExamplesField';

export default function NewWordPage() {
  return (
    <main className="max-w-2xl mx-auto px-4 py-10">
      <Link href="/" className="text-sm text-gray-400 hover:text-gray-600">← List</Link>
      <h1 className="text-2xl font-bold mt-6 mb-8">Add Word</h1>
      <form action={addWord} className="space-y-5">
        <div>
          <label className="block text-sm font-medium mb-1">Word *</label>
          <input name="word" required className="w-full border rounded-lg px-3 py-2 focus:outline-none focus:ring-2 focus:ring-black" />
        </div>
        <div>
          <label className="block text-sm font-medium mb-1">Meaning *</label>
          <textarea name="meaning" required rows={3} className="w-full border rounded-lg px-3 py-2 focus:outline-none focus:ring-2 focus:ring-black" />
        </div>
        <div className="flex gap-4">
          <div className="flex-1">
            <label className="block text-sm font-medium mb-1">Part of Speech</label>
            <input name="part_of_speech" className="w-full border rounded-lg px-3 py-2 focus:outline-none focus:ring-2 focus:ring-black" placeholder="noun / verb / adjective ..." />
          </div>
          <div className="w-32">
            <label className="block text-sm font-medium mb-1">Level (1–20)</label>
            <input name="level" type="number" min={1} max={20} className="w-full border rounded-lg px-3 py-2 focus:outline-none focus:ring-2 focus:ring-black" />
          </div>
        </div>
        <div>
          <label className="block text-sm font-medium mb-1">Pronunciation</label>
          <input name="pronunciation" className="w-full border rounded-lg px-3 py-2 focus:outline-none focus:ring-2 focus:ring-black" placeholder="e.g. dɔːɡ" />
        </div>
        <ExamplesField />
        <button type="submit" className="w-full bg-black text-white rounded-lg py-2 hover:bg-gray-800 transition-colors">
          Add
        </button>
      </form>
    </main>
  );
}
