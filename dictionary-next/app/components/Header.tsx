import Link from 'next/link';
import { UserMenu } from '@/app/components/UserMenu';
import SearchBox from '@/app/components/SearchBox';

export function Header() {
  return (
    <header className="border-b px-6 py-3 flex items-center justify-between gap-4">
      <h1 className="text-xl font-bold shrink-0">Dictionary</h1>
      <SearchBox />
      <div className="flex items-center gap-4 shrink-0">
        <Link
          href="/new"
          className="bg-black text-white text-sm rounded-lg px-4 py-2 hover:bg-gray-800 transition-colors"
        >
          + Add
        </Link>
        <UserMenu />
      </div>
    </header>
  );
}
