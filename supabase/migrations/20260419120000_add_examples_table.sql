create table examples (
  id         uuid primary key default gen_random_uuid(),
  word_id    uuid not null references words(id) on delete cascade,
  sentence   text not null,
  created_at timestamptz default now()
);

-- words.example の既存データを移行
insert into examples (word_id, sentence)
select id, example from words where example is not null;

alter table words drop column example;
