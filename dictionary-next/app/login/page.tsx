'use client';

import { useSearchParams, useRouter } from 'next/navigation';
import { LoginButton } from '@/app/components/LoginButton';
import { useAuth } from '@/app/hooks/useAuth';
import { Suspense, useEffect } from 'react';

function LoginPageInner() {
  const router = useRouter();
  const searchParams = useSearchParams();
  const { user, loading } = useAuth();

  const redirectTo = searchParams.get('redirectTo') || '/';

  useEffect(() => {
    if (!loading && user) {
      router.push(redirectTo);
    }
  }, [user, loading, router, redirectTo]);

  return (
    <div className="min-h-screen flex items-center justify-center bg-gray-50">
      <div className="max-w-md w-full space-y-8">
        <div className="text-center">
          <h1 className="text-3xl font-bold">Dictionary</h1>
          <p className="mt-2 text-gray-600">
            ログインして単語を追加・編集しましょう
          </p>
        </div>

        {loading ? (
          <div className="flex justify-center">
            <div className="animate-spin rounded-full h-8 w-8 border-b-2 border-black" />
          </div>
        ) : (
          <div className="flex justify-center">
            <LoginButton />
          </div>
        )}
      </div>
    </div>
  );
}

export default function LoginPage() {
  return (
    <Suspense fallback={null}>
      <LoginPageInner />
    </Suspense>
  );
}
