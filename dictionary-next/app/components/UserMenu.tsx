'use client';

import { useAuth } from '@/app/hooks/useAuth';
import { LoginButton } from '@/app/components/LoginButton';
import { useState } from 'react';

export function UserMenu() {
  const { user, loading, signOut } = useAuth();
  const [isOpen, setIsOpen] = useState(false);

  if (loading) {
    return <div className="w-32 h-10 bg-gray-200 rounded animate-pulse" />;
  }

  if (!user) {
    return <LoginButton />;
  }

  return (
    <div className="relative">
      <button
        onClick={() => setIsOpen(!isOpen)}
        className="flex items-center gap-2 px-4 py-2 text-sm rounded-lg hover:bg-gray-100"
      >
        <span className="truncate max-w-[200px]">{user.email}</span>
        <svg
          className={`w-4 h-4 transition-transform ${isOpen ? 'rotate-180' : ''}`}
          fill="none"
          stroke="currentColor"
          viewBox="0 0 24 24"
        >
          <path
            strokeLinecap="round"
            strokeLinejoin="round"
            strokeWidth={2}
            d="M19 14l-7 7m0 0l-7-7m7 7V3"
          />
        </svg>
      </button>

      {isOpen && (
        <div className="absolute right-0 mt-2 w-48 bg-white rounded-lg shadow-lg z-50">
          <button
            onClick={async () => {
              await signOut();
              setIsOpen(false);
            }}
            className="w-full text-left px-4 py-2 text-sm text-red-600 hover:bg-red-50 rounded-lg"
          >
            ログアウト
          </button>
        </div>
      )}
    </div>
  );
}
