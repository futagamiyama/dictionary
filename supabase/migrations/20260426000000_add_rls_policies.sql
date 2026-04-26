-- Allow public read/write access for anonymous users (no auth required)
CREATE POLICY "allow_all_words" ON words FOR ALL TO anon USING (true) WITH CHECK (true);
CREATE POLICY "allow_all_examples" ON examples FOR ALL TO anon USING (true) WITH CHECK (true);
