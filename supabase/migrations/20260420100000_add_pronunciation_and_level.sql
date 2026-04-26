alter table words add column pronunciation text;
alter table words add column level integer check (level >= 1 and level <= 20);
