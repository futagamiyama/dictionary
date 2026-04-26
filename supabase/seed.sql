insert into words (word, meaning, part_of_speech, pronunciation, level) values
  ('dog',   '犬', 'noun', 'dɔːɡ', 1),
  ('cat',   '猫', 'noun', 'kæt',  1),
  ('cow',   '牛', 'noun', 'kaʊ',  2),
  ('sheep', '羊', 'noun', 'ʃiːp', 2),
  ('fish',  '魚', 'noun', 'fɪʃ',  1);

insert into examples (word_id, sentence, translation)
select id, 'The dog is barking loudly.', '犬が大きな声で吠えている。' from words where word = 'dog';

insert into examples (word_id, sentence, translation)
select id, 'A cat is sleeping on the sofa.', '猫がソファの上で眠っている。' from words where word = 'cat';

insert into examples (word_id, sentence, translation)
select id, 'The cow is grazing in the field.', '牛が野原で草を食べている。' from words where word = 'cow';

insert into examples (word_id, sentence, translation)
select id, 'The sheep are on the hill.', '羊が丘の上にいる。' from words where word = 'sheep';

insert into examples (word_id, sentence, translation)
select id, 'The fish swims in the river.', '魚が川を泳いでいる。' from words where word = 'fish';
