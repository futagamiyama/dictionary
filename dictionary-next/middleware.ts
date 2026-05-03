import { type NextRequest, NextResponse } from 'next/server';
import { createClient } from '@supabase/supabase-js';

const supabase = createClient(
  process.env.NEXT_PUBLIC_SUPABASE_URL!,
  process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY!
);

export async function middleware(request: NextRequest) {
  const { pathname } = request.nextUrl;

  // 保護されたルートのチェック
  const protectedPaths = ['/new', /^\/dictionary\/.*\/edit$/];
  const isProtectedPath = protectedPaths.some((path) => {
    if (typeof path === 'string') {
      return pathname === path;
    }
    return path.test(pathname);
  });

  if (!isProtectedPath) {
    return NextResponse.next();
  }

  // セッションの確認
  const sessionCookie = request.cookies.get('sb-sbvktfppilekgiqbymhqg-auth-token')?.value;

  if (!sessionCookie) {
    // クエリパラメータに現在のパスを保存してログインにリダイレクト
    const loginUrl = new URL('/login', request.url);
    loginUrl.searchParams.set('redirectTo', pathname);
    return NextResponse.redirect(loginUrl);
  }

  return NextResponse.next();
}

export const config = {
  matcher: ['/new', '/dictionary/:path*/edit', '/login'],
};
