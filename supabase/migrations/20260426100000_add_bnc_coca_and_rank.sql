-- BNC/COCA frequency reference table
create table public.bnc_coca (
  list            text,
  headword        text,
  related_forms   text,
  total_frequency integer,
  rank            integer
);

create index bnc_coca_headword_idx on public.bnc_coca (lower(headword));
create index bnc_coca_rank_idx     on public.bnc_coca (rank);

alter table public.bnc_coca enable row level security;
create policy "allow_read_bnc_coca" on public.bnc_coca for select to anon using (true);

-- Frequency rank column on words (populated automatically on insert/update)
alter table public.words add column rank integer;
