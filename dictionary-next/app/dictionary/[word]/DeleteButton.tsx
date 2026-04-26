'use client';

import { deleteWord } from '@/app/actions';

export default function DeleteButton({ id, word }: { id: string; word: string }) {
  const action = deleteWord.bind(null, id);
  return (
    <form action={action} onSubmit={(e) => { if (!confirm(`「${word}」を削除しますか？`)) e.preventDefault(); }}>
      <button type="submit" className="text-sm border border-red-200 text-red-500 rounded-lg px-3 py-1 hover:bg-red-50 transition-colors">
        Delete
      </button>
    </form>
  );
}
