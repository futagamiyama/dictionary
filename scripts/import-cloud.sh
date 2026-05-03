#!/bin/bash
HOST=db.tvklrujikuanxdddyfcx.supabase.co

psql -h $HOST -p 5432 -d postgres -U postgres \
  -c "\copy public.bnc_coca (list, headword, related_forms, total_frequency, rank) FROM '/Users/yutaka/projects/word-rank/supabase/data/bnc_coca.csv' CSV HEADER;"

psql -h $HOST -p 5432 -d postgres -U postgres \
  -c "UPDATE public.words w SET rank = b.rank FROM public.bnc_coca b WHERE lower(b.headword) = lower(w.word);"
