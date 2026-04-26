-- 単語テーブル
create table words (
  id             uuid primary key default gen_random_uuid(),
  word           text not null unique,
  meaning        text not null,
  example        text,
  part_of_speech text,
  created_at     timestamptz default now()
);
