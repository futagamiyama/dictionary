#!/usr/bin/env python3
"""Generate example sentences for words ranked 4996-5016"""

from supabase import create_client, Client

# Supabase credentials
url = "https://tvklrujikuanxdddyfcx.supabase.co"
key = "sb_publishable_DLHimQA_Wyt18fOtUH-o3w_1_BGYb0t"
supabase: Client = create_client(url, key)

# Words data
words_data = [
    {"id": "29785493-ee38-49b5-aa08-a9b1b2c91fdb", "word": "couch", "rank": 4996},
    {"id": "b098f3bb-fc69-4b8d-a70f-4bc6c8788e55", "word": "chronology", "rank": 4997},
    {"id": "006e2a2c-5e78-4641-8a90-0ee01580584a", "word": "presuppose", "rank": 4998},
    {"id": "a4872dbc-f7f8-4962-875b-70d753cbae50", "word": "crunch", "rank": 4999},
    {"id": "4647f2bb-1845-4674-8fe8-047063e7324a", "word": "nutrient", "rank": 5000},
    {"id": "e208d6bd-907b-45c5-88f2-dedbc43709ec", "word": "demon", "rank": 5002},
    {"id": "85879782-c1e9-48e3-8736-88057e28d509", "word": "butt", "rank": 5003},
    {"id": "42b9b60a-c7ee-44ca-95c6-5ac5f3f4d3c0", "word": "drought", "rank": 5004},
    {"id": "5c616340-b075-44ec-9598-2d6e8df77587", "word": "enchant", "rank": 5005},
    {"id": "371b35dd-1b44-43f3-bfd8-f44a63e60236", "word": "rave", "rank": 5006},
    {"id": "4455d6a2-4eee-41e3-b1bd-04aa25a73ce2", "word": "astronomy", "rank": 5007},
    {"id": "c02cbcd8-128e-481f-8a92-83f0f7e4c073", "word": "remit", "rank": 5008},
    {"id": "25ce3540-5d52-48c4-b48b-30fe18d62428", "word": "growl", "rank": 5009},
    {"id": "35b0a5d4-ad0d-40b8-98b1-f98d9af72178", "word": "exemplify", "rank": 5010},
    {"id": "0832de7b-5a65-4649-9843-b01dc6043d8b", "word": "contented", "rank": 5011},
    {"id": "735924dc-c4e0-43fb-a60b-e5df865d5c87", "word": "deceive", "rank": 5012},
    {"id": "b0092446-b183-48f5-afee-c2936d032ef2", "word": "discomfort", "rank": 5013},
    {"id": "2be9e72e-a5f3-4ceb-925e-cd35fa792fe2", "word": "antigen", "rank": 5014},
    {"id": "8ce00882-5849-4297-b077-d61e98e3e933", "word": "artillery", "rank": 5015},
    {"id": "d42511f3-360e-4914-994c-dc7492522338", "word": "sweater", "rank": 5016},
]

# Example sentences for each word
examples_dict = {
    "couch": [
        {"sentence": "She sat on the couch watching TV.", "translation": "彼女はテレビを見ながらソファに座っていました。"},
        {"sentence": "The couch is comfortable and spacious.", "translation": "そのソファは快適で広々としています。"},
        {"sentence": "He couch surfed while traveling.", "translation": "彼は旅行中にカウチサーフィンをしました。"},
    ],
    "chronology": [
        {"sentence": "The chronology of events is important.", "translation": "イベントの年代順序は重要です。"},
        {"sentence": "The historian established the chronology.", "translation": "その歴史家は年代順序を確立しました。"},
        {"sentence": "Chronology helps us understand history.", "translation": "年代順序は私たちが歴史を理解するのに役立ちます。"},
    ],
    "presuppose": [
        {"sentence": "The argument presupposes certain facts.", "translation": "その議論は特定の事実を前提とします。"},
        {"sentence": "This theory presupposes prior knowledge.", "translation": "この理論は事前の知識を前提とします。"},
        {"sentence": "The question presupposes the answer.", "translation": "その質問は答えを前提とします。"},
    ],
    "crunch": [
        {"sentence": "The leaves crunch under our feet.", "translation": "その葉は私たちの足の下でパリパリと鳴ります。"},
        {"sentence": "She crunched on the apple.", "translation": "彼女はリンゴを噛みました。"},
        {"sentence": "We are in crunch time for the project.", "translation": "私たちはプロジェクトの締切間近です。"},
    ],
    "nutrient": [
        {"sentence": "Plants need nutrients to grow.", "translation": "植物は成長するために栄養が必要です。"},
        {"sentence": "The soil lacks essential nutrients.", "translation": "その土壌は必須栄養素に欠けています。"},
        {"sentence": "Food is a source of nutrients.", "translation": "食べ物は栄養素の源です。"},
    ],
    "demon": [
        {"sentence": "In the story, a demon haunted the house.", "translation": "その物語では、悪魔がその家に取り憑いていました。"},
        {"sentence": "She struggles with her inner demons.", "translation": "彼女は彼女の内なる悪魔と戦っています。"},
        {"sentence": "The demon was defeated by the hero.", "translation": "その悪魔は英雄に倒されました。"},
    ],
    "butt": [
        {"sentence": "Please butt out of this conversation.", "translation": "この会話から口を出さないでください。"},
        {"sentence": "The butt of the rifle was visible.", "translation": "そのライフルの銃床は見えました。"},
        {"sentence": "The butt end of the log was heavy.", "translation": "そのログの先端は重かった。"},
    ],
    "drought": [
        {"sentence": "The drought caused crop failures.", "translation": "その干ばつは作物の不作を引き起こしました。"},
        {"sentence": "The region suffered a severe drought.", "translation": "その地域は深刻な干ばつに苦しみました。"},
        {"sentence": "Water conservation is important during drought.", "translation": "干ばつ中の節水は重要です。"},
    ],
    "enchant": [
        {"sentence": "The magician enchanted the audience.", "translation": "そのマジシャンは観客を魅了しました。"},
        {"sentence": "She was enchanted by the beautiful scenery.", "translation": "彼女は美しい風景に魅了されました。"},
        {"sentence": "The enchanted forest was magical.", "translation": "その魔法の森は魔法のようでした。"},
    ],
    "rave": [
        {"sentence": "He raved about the excellent meal.", "translation": "彼は素晴らしい食事について絶賛しました。"},
        {"sentence": "The critics gave the movie rave reviews.", "translation": "評論家たちはその映画を大絶賛しました。"},
        {"sentence": "The rave party lasted all night.", "translation": "そのレイブパーティーは一晩中続きました。"},
    ],
    "astronomy": [
        {"sentence": "Astronomy is the study of celestial objects.", "translation": "天文学は天体の研究です。"},
        {"sentence": "She is interested in astronomy and space.", "translation": "彼女は天文学と宇宙に興味があります。"},
        {"sentence": "Modern astronomy uses telescopes.", "translation": "現代天文学は望遠鏡を使用しています。"},
    ],
    "remit": [
        {"sentence": "Please remit payment by the deadline.", "translation": "期限までに支払いを送金してください。"},
        {"sentence": "He remitted the funds to the account.", "translation": "彼は資金をアカウントに送金しました。"},
        {"sentence": "The crime was remitted after rehabilitation.", "translation": "その犯罪は更生後に減刑されました。"},
    ],
    "growl": [
        {"sentence": "The dog began to growl at the stranger.", "translation": "その犬は見知らぬ人に向かってうなり始めました。"},
        {"sentence": "His stomach made a growling sound.", "translation": "彼の胃はうなる音を出しました。"},
        {"sentence": "She growled her disapproval.", "translation": "彼女は不承認をうなりました。"},
    ],
    "exemplify": [
        {"sentence": "His actions exemplify courage.", "translation": "彼の行動は勇気を示しています。"},
        {"sentence": "This painting exemplifies the artist's style.", "translation": "この絵はアーティストのスタイルを示しています。"},
        {"sentence": "She exemplifies what a good teacher should be.", "translation": "彼女は良い先生がどうあるべきかを示しています。"},
    ],
    "contented": [
        {"sentence": "She seemed contented with her life.", "translation": "彼女は彼女の人生に満足しているようでした。"},
        {"sentence": "The contented cat purred softly.", "translation": "その満足した猫はそっと喉を鳴らしました。"},
        {"sentence": "He was contented with simple pleasures.", "translation": "彼は単純な喜びに満足していました。"},
    ],
    "deceive": [
        {"sentence": "Don't deceive people with false information.", "translation": "虚偽の情報で人々を欺いてはいけません。"},
        {"sentence": "He deceived his friends about his whereabouts.", "translation": "彼は彼の居場所について友人を欺きました。"},
        {"sentence": "Appearances can deceive.", "translation": "見かけは欺くことができます。"},
    ],
    "discomfort": [
        {"sentence": "The chair caused him discomfort.", "translation": "その椅子は彼に不快感を与えました。"},
        {"sentence": "She felt discomfort during the flight.", "translation": "彼女はフライト中に不快感を感じました。"},
        {"sentence": "His discomfort was evident.", "translation": "彼の不快感は明らかでした。"},
    ],
    "antigen": [
        {"sentence": "The antigen triggers an immune response.", "translation": "その抗原は免疫反応をトリガーします。"},
        {"sentence": "Antigens help the body fight disease.", "translation": "抗原は体が病気と戦うのを助けます。"},
        {"sentence": "The test detects the antigen.", "translation": "そのテストは抗原を検出します。"},
    ],
    "artillery": [
        {"sentence": "Artillery was used in the battle.", "translation": "その戦いで砲兵が使用されました。"},
        {"sentence": "The artillery unit was well-trained.", "translation": "その砲兵部隊はよく訓練されていました。"},
        {"sentence": "Heavy artillery destroyed the fortress.", "translation": "重砲がその要塞を破壊しました。"},
    ],
    "sweater": [
        {"sentence": "She wore a warm sweater in winter.", "translation": "彼女は冬に暖かいセーターを着ました。"},
        {"sentence": "The sweater was made of wool.", "translation": "そのセーターはウールでできていました。"},
        {"sentence": "He pulled on his favorite sweater.", "translation": "彼は彼のお気に入りのセーターを引っ張りました。"},
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
