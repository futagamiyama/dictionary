# Dictionary Project

## プロジェクト概要

英単語辞書アプリ。Supabase（PostgreSQL）をバックエンドに使用し、Next.jsでフロントエンドを構成する。

## Supabase 接続

**環境変数や `.env` ファイルを参照する必要はない。**  
Supabase MCP ツール（`mcp__890d9a77-4656-4239-b991-14ae502e6213__*`）を直接使用する。

- Project ID: `tvklrujikuanxdddyfcx`
- Project name: `dictionary`
- Region: `ap-northeast-1`

スクリプトを実行したり、環境変数を確認したりせず、**MCP ツールのみで DB 操作を行う。**

## DB スキーマ（主要テーブル）

```sql
-- 単語テーブル
words (
  id uuid PRIMARY KEY,
  word text UNIQUE,
  meaning text,
  part_of_speech text,
  pronunciation text,
  level integer,         -- 1〜20
  rank integer,          -- BNC/COCA frequency rank
  created_at timestamptz
)

-- 例文テーブル
examples (
  id uuid PRIMARY KEY,
  word_id uuid REFERENCES words(id),
  sentence text,
  translation text,
  created_at timestamptz
)
```

## 例文追加タスクの手順

「Rank #XXXX から N 単語に例文を追加して」というリクエストが来たら、以下の手順で行う。

1. **対象単語を取得**
   ```sql
   SELECT id, word, meaning, rank
   FROM words
   WHERE rank BETWEEN :start AND :end
   ORDER BY rank;
   ```

2. **例文を生成**（Claude が直接生成する）
   - 各単語に英文例文3つ＋日本語訳を作成
   - レベル感：やさしいニュース記事程度（NHK Web Easy 相当）
   - 日常・社会・自然・科学などの身近なトピックを使う
   - スクリプトファイルを作成したり、外部コマンドを実行したりしない

3. **MCP ツールでまとめて INSERT**
   ```sql
   INSERT INTO examples (word_id, sentence, translation) VALUES
   ('uuid', 'sentence', '和訳'),
   ...;
   ```

4. **件数を確認して完了報告**
   ```sql
   SELECT w.word, w.rank, COUNT(e.id) AS example_count
   FROM words w JOIN examples e ON e.word_id = w.id
   WHERE w.rank BETWEEN :start AND :end
   GROUP BY w.word, w.rank ORDER BY w.rank;
   ```

## フロントエンド

- ディレクトリ: `dictionary-next/`
- フレームワーク: Next.js (App Router)
