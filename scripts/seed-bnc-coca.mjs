/**
 * Imports BNC/COCA frequency data from CSV into the dictionary's bnc_coca table.
 * Run from the dictionary-next directory:
 *   node --env-file=.env.local ../scripts/seed-bnc-coca.mjs
 */

import { createClient } from '@supabase/supabase-js';
import { createReadStream } from 'fs';
import { createInterface } from 'readline';
import { resolve, dirname } from 'path';
import { fileURLToPath } from 'url';

const __dirname = dirname(fileURLToPath(import.meta.url));
const CSV_PATH = resolve(__dirname, '../../word-rank/supabase/data/bnc_coca.csv');
const BATCH_SIZE = 500;

const supabase = createClient(
  process.env.NEXT_PUBLIC_SUPABASE_URL,
  process.env.SUPABASE_SERVICE_ROLE_KEY ?? process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY
);

function parseLine(line) {
  // Format: list,headword,"related_forms",total_frequency,rank
  // related_forms is always double-quoted (may contain commas)
  const m = line.match(/^([^,]+),([^,]+),"((?:[^"]|"")*)"\s*,(\d+),(\d+)$/);
  if (m) {
    return {
      list: m[1],
      headword: m[2],
      related_forms: m[3].replace(/""/g, '"'),
      total_frequency: parseInt(m[4], 10),
      rank: parseInt(m[5], 10),
    };
  }
  // Fallback: unquoted related_forms (5 comma-separated fields)
  const parts = line.split(',');
  if (parts.length === 5) {
    return {
      list: parts[0],
      headword: parts[1],
      related_forms: parts[2],
      total_frequency: parseInt(parts[3], 10),
      rank: parseInt(parts[4], 10),
    };
  }
  return null;
}

async function insertBatch(batch) {
  const { error } = await supabase.from('bnc_coca').insert(batch);
  if (error) throw new Error(`Insert failed: ${error.message}`);
}

async function main() {
  // Clear existing data
  const { error: delError } = await supabase.from('bnc_coca').delete().gte('rank', 0);
  if (delError) throw new Error(`Delete failed: ${delError.message}`);

  const rl = createInterface({ input: createReadStream(CSV_PATH), crlfDelay: Infinity });
  let batch = [];
  let total = 0;
  let skipped = 0;

  for await (const line of rl) {
    if (!line.trim() || line.startsWith('list,')) continue; // skip header/blank
    const row = parseLine(line);
    if (!row) { skipped++; continue; }
    batch.push(row);
    if (batch.length >= BATCH_SIZE) {
      await insertBatch(batch);
      total += batch.length;
      process.stdout.write(`\rInserted ${total} rows...`);
      batch = [];
    }
  }

  if (batch.length > 0) {
    await insertBatch(batch);
    total += batch.length;
  }

  console.log(`\nDone. Inserted ${total} rows. Skipped ${skipped} lines.`);
}

main().catch((e) => { console.error(e.message); process.exit(1); });
