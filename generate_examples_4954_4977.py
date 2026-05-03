#!/usr/bin/env python3
"""Generate example sentences for words ranked 4954-4977"""

from supabase import create_client, Client

# Supabase credentials
url = "https://tvklrujikuanxdddyfcx.supabase.co"
key = "sb_publishable_DLHimQA_Wyt18fOtUH-o3w_1_BGYb0t"
supabase: Client = create_client(url, key)

# Words data
words_data = [
    {"id": "bab436c0-c5e5-4d9b-af70-36690a082351", "word": "clap", "rank": 4954},
    {"id": "f53178e7-b2a0-4fd0-b52a-f0377b476e1a", "word": "discern", "rank": 4955},
    {"id": "cca7492e-a6a7-48d0-b436-7acb2718cece", "word": "generator", "rank": 4956},
    {"id": "feebf951-bc2e-4e88-a41a-1c288728ad95", "word": "grunt", "rank": 4957},
    {"id": "df0af14c-9c60-4356-83f6-5e054a2fdd91", "word": "reclaim", "rank": 4958},
    {"id": "378bbf36-bb6a-43be-9730-ed33e9b75962", "word": "wrestle", "rank": 4959},
    {"id": "e8d6a200-2925-47d9-baf9-9950d0a3b66d", "word": "pathetic", "rank": 4960},
    {"id": "15359144-32ef-4bff-b920-f959a63e35d7", "word": "debris", "rank": 4961},
    {"id": "0940bac7-f61d-443a-ab7c-236f3913f8f0", "word": "procure", "rank": 4962},
    {"id": "8b60be90-9072-4522-b6cb-87276f887dd9", "word": "wry", "rank": 4963},
    {"id": "807b4f60-7aae-4303-98ea-4f9d40c6a1e2", "word": "lavatory", "rank": 4964},
    {"id": "1166321a-f7f5-4969-8943-89ae80255161", "word": "infinitive", "rank": 4965},
    {"id": "5ed3e1c6-074e-4256-86d2-fe8c200aa1bd", "word": "gratitude", "rank": 4966},
    {"id": "e2714b13-9510-44f6-8a19-9c6c2e0cabe1", "word": "induct", "rank": 4967},
    {"id": "21404122-cdff-4dba-a432-d45d3feb7af5", "word": "stipulate", "rank": 4968},
    {"id": "b9ec34fa-74d5-4441-91d4-5e012876e032", "word": "microwave", "rank": 4969},
    {"id": "46f2a6cb-3e17-404b-8fc7-e2fabc24e1ae", "word": "cumulative", "rank": 4970},
    {"id": "3f00fba8-d1a1-4fc1-ac20-b7d0ceb8f8c5", "word": "globe", "rank": 4971},
    {"id": "e9ea1d33-d72b-431a-9aa9-29c5a29bdd1c", "word": "fen", "rank": 4972},
    {"id": "d6ace48a-1008-4b5d-b574-fd1ff9b56b52", "word": "relay", "rank": 4974},
]

# Example sentences for each word
examples_dict = {
    "clap": [
        {"sentence": "The audience began to clap loudly.", "translation": "観客は大きく拍手し始めた。"},
        {"sentence": "He clapped his hands in approval.", "translation": "彼は承認のために手をたたいた。"},
        {"sentence": "The clap of thunder startled everyone.", "translation": "その雷の音は誰もがびっくりした。"},
    ],
    "discern": [
        {"sentence": "It is hard to discern the truth.", "translation": "真実を識別することは困難です。"},
        {"sentence": "She could discern a pattern in the data.", "translation": "彼女はデータにパターンを見分けることができた。"},
        {"sentence": "Can you discern the difference between them?", "translation": "あなたは彼らの違いを区別できますか？"},
    ],
    "generator": [
        {"sentence": "The generator produces electricity.", "translation": "その発電機は電気を生成します。"},
        {"sentence": "A backup generator was installed.", "translation": "バックアップ発電機がインストールされました。"},
        {"sentence": "The generator runs on diesel fuel.", "translation": "その発電機はディーゼル燃料で動きます。"},
    ],
    "grunt": [
        {"sentence": "He grunt while lifting the heavy box.", "translation": "彼は重い箱を持ち上げながらうめいた。"},
        {"sentence": "The pig let out a grunt.", "translation": "その豚は一声うめき声を出した。"},
        {"sentence": "With a grunt, he stood up.", "translation": "うめき声を出して、彼は立ち上がった。"},
    ],
    "reclaim": [
        {"sentence": "They plan to reclaim the land.", "translation": "彼らは土地を回収する計画です。"},
        {"sentence": "She wants to reclaim her dignity.", "translation": "彼女は彼女の尊厳を取り戻したいと思っています。"},
        {"sentence": "The project will reclaim wasteland.", "translation": "そのプロジェクトは荒れ地を開拓します。"},
    ],
    "wrestle": [
        {"sentence": "The wrestlers wrestle on the mat.", "translation": "その レスラーたちはマットでレスリングをします。"},
        {"sentence": "He wrestled with the decision for weeks.", "translation": "彼は数週間その決定と格闘した。"},
        {"sentence": "The boys wrestle as a sport.", "translation": "その少年たちはスポーツとしてレスリングをします。"},
    ],
    "pathetic": [
        {"sentence": "His excuse was pathetic and unconvincing.", "translation": "彼の言い訳は哀れで説得力がなかった。"},
        {"sentence": "The team's performance was pathetic.", "translation": "そのチームのパフォーマンスは哀れでした。"},
        {"sentence": "It was a pathetic attempt to help.", "translation": "それは助けようとする哀れな試みでした。"},
    ],
    "debris": [
        {"sentence": "The explosion left debris everywhere.", "translation": "その爆発はあちこちに瓦礫を残した。"},
        {"sentence": "Debris from the accident blocked the road.", "translation": "その事故からの瓦礫は道路をふさいだ。"},
        {"sentence": "They cleaned up the debris after the storm.", "translation": "彼らは嵐の後で瓦礫をきれいにしました。"},
    ],
    "procure": [
        {"sentence": "The company will procure new equipment.", "translation": "その企業は新しい装備を調達します。"},
        {"sentence": "It is difficult to procure rare items.", "translation": "珍しいアイテムを調達することは困難です。"},
        {"sentence": "We need to procure supplies for the event.", "translation": "私たちはイベントのために物資を調達する必要があります。"},
    ],
    "wry": [
        {"sentence": "He made a wry comment about the situation.", "translation": "彼は状況について皮肉なコメントをした。"},
        {"sentence": "A wry smile crossed her face.", "translation": "皮肉な笑みが彼女の顔を横切った。"},
        {"sentence": "Her wry sense of humor is appreciated.", "translation": "彼女の皮肉なユーモアのセンスは高く評価されています。"},
    ],
    "lavatory": [
        {"sentence": "The lavatory is down the hallway.", "translation": "そのトイレは廊下を下ります。"},
        {"sentence": "Please use the lavatory before boarding.", "translation": "搭乗する前にトイレを使用してください。"},
        {"sentence": "The airplane lavatory is small.", "translation": "その飛行機のトイレは小さいです。"},
    ],
    "infinitive": [
        {"sentence": "The infinitive form of the verb is 'to go.'", "translation": "その動詞の不定詞形は「go」です。"},
        {"sentence": "In English, the infinitive uses 'to.'", "translation": "英語では、不定詞は「to」を使用します。"},
        {"sentence": "The infinitive phrase modifies the noun.", "translation": "その不定詞句は名詞を修飾します。"},
    ],
    "gratitude": [
        {"sentence": "She expressed her gratitude for the gift.", "translation": "彼女はその贈り物に対する感謝を表現した。"},
        {"sentence": "He showed gratitude for their help.", "translation": "彼は彼らの助けに感謝を示しました。"},
        {"sentence": "Gratitude is an important value.", "translation": "感謝は重要な価値です。"},
    ],
    "induct": [
        {"sentence": "They will induct new members this month.", "translation": "彼らは今月新しいメンバーを就任させるでしょう。"},
        {"sentence": "The ceremony will induct the winners.", "translation": "その式典は勝者を就任させます。"},
        {"sentence": "The hall of fame will induct five people.", "translation": "その名誉の殿堂は5人を就任させます。"},
    ],
    "stipulate": [
        {"sentence": "The contract stipulates the payment terms.", "translation": "その契約は支払い条件を規定しています。"},
        {"sentence": "The rules stipulate that everyone must participate.", "translation": "その規則は誰もが参加しなければならないことを規定しています。"},
        {"sentence": "The agreement stipulates a six-month trial.", "translation": "その合意は6か月の試験期間を規定しています。"},
    ],
    "microwave": [
        {"sentence": "She heated the food in the microwave.", "translation": "彼女は電子レンジで食べ物を温めました。"},
        {"sentence": "The microwave oven is convenient.", "translation": "その電子レンジオーブンは便利です。"},
        {"sentence": "Don't put metal in the microwave.", "translation": "電子レンジに金属を入れないでください。"},
    ],
    "cumulative": [
        {"sentence": "The cumulative effect was significant.", "translation": "その累積効果は重要でした。"},
        {"sentence": "Cumulative stress can lead to illness.", "translation": "累積ストレスは病気につながる可能性があります。"},
        {"sentence": "The cumulative score determines the winner.", "translation": "その累積スコアは勝者を決定します。"},
    ],
    "globe": [
        {"sentence": "She spun the globe to find a country.", "translation": "彼女は国を見つけるために地球儀を回転させました。"},
        {"sentence": "The globe represents the Earth.", "translation": "その地球儀は地球を表します。"},
        {"sentence": "Around the globe, people speak many languages.", "translation": "世界中で、人々は多くの言語を話します。"},
    ],
    "fen": [
        {"sentence": "The fen is a wetland ecosystem.", "translation": "その沼地は湿地生態系です。"},
        {"sentence": "Plants grow abundantly in the fen.", "translation": "植物は沼地に豊富に育ちます。"},
        {"sentence": "The fen is home to many birds.", "translation": "その沼地は多くの鳥の家です。"},
    ],
    "relay": [
        {"sentence": "The relay race requires teamwork.", "translation": "そのリレー競争はチームワークを必要とします。"},
        {"sentence": "Please relay the message to him.", "translation": "彼にメッセージを中継してください。"},
        {"sentence": "The relay team won the championship.", "translation": "そのリレーチームは選手権に勝った。"},
    ],
}

def insert_examples():
    """Insert example sentences into the database"""
    total_inserted = 0

    for word_info in words_data:
        word = word_info["word"]
        word_id = word_info["id"]

        if word not in examples_dict:
            print(f"⚠️  No examples found for: {word}")
            continue

        examples = examples_dict[word]

        for example in examples:
            try:
                response = supabase.table("examples").insert({
                    "word_id": word_id,
                    "sentence": example["sentence"],
                    "translation": example["translation"],
                }).execute()

                print(f"✅ {word}: {example['sentence'][:50]}...")
                total_inserted += 1
            except Exception as e:
                print(f"❌ Error inserting example for {word}: {str(e)}")

    print(f"\n📊 Total examples inserted: {total_inserted}/60")

if __name__ == "__main__":
    insert_examples()
