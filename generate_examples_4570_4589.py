#!/usr/bin/env python3
"""Generate example sentences for words ranked 4570-4589"""

from supabase import create_client, Client

# Supabase credentials
url = "https://tvklrujikuanxdddyfcx.supabase.co"
key = "sb_publishable_DLHimQA_Wyt18fOtUH-o3w_1_BGYb0t"
supabase: Client = create_client(url, key)

# Words data
words_data = [
    {"id": "59cbc3e0-191c-47b1-8900-e0ccc254451b", "word": "bait", "rank": 4570},
    {"id": "e1d6586a-42a8-4b09-aa23-3baad7132949", "word": "imminent", "rank": 4571},
    {"id": "8ea2ff62-c0e1-4c54-aa75-b86751521ddc", "word": "meditate", "rank": 4572},
    {"id": "23f11b76-e996-4afa-bdb8-b30c66b5b20a", "word": "compartment", "rank": 4573},
    {"id": "7f190633-2c01-4916-950d-3f3291e8eaaa", "word": "intrinsic", "rank": 4574},
    {"id": "8faa298d-c0a5-4f38-963d-73aeb929e4a9", "word": "incubate", "rank": 4575},
    {"id": "f8fcae99-04f8-4c9b-b693-f24ca9fe6d06", "word": "piper", "rank": 4576},
    {"id": "e9bee079-9c25-4e6e-a338-ea23866c72b0", "word": "detention", "rank": 4577},
    {"id": "4fbf2b16-ef63-4187-9ddd-f3b8767ec986", "word": "libel", "rank": 4578},
    {"id": "aea55040-5725-4d7e-a60d-a9b260efe6df", "word": "curb", "rank": 4579},
    {"id": "b63f1041-5b33-4c53-bc78-9f25e8378844", "word": "cafe", "rank": 4580},
    {"id": "2fc6a719-f624-4360-8af1-aa8d27e6808c", "word": "physician", "rank": 4581},
    {"id": "bf2e9550-9fea-4189-9762-9790f2e55fdd", "word": "precipitate", "rank": 4582},
    {"id": "54aca172-351f-43d8-881f-e781a23c1544", "word": "eminent", "rank": 4583},
    {"id": "b352e536-8d01-4c3d-a9cc-a6df7d48a3a0", "word": "warranty", "rank": 4584},
    {"id": "0e970239-bdc6-4db1-bba5-976621bb3e29", "word": "reckless", "rank": 4585},
    {"id": "e4eff56a-5c61-4aa2-924a-b69b1c95bc3b", "word": "hospitality", "rank": 4586},
    {"id": "9269609f-4dd6-466c-8137-e1e4bef17c12", "word": "adequacy", "rank": 4587},
    {"id": "0af09262-b1e3-4351-9b73-f3794ce4e597", "word": "affinity", "rank": 4588},
    {"id": "3e63f979-4052-4396-a811-aa63a3988ea6", "word": "archer", "rank": 4589},
]

# Example sentences for each word
examples_dict = {
    "bait": [
        {"sentence": "The fisherman used worms as bait to catch fish.", "translation": "その漁師は魚を捕まえるために虫を餌として使用した。"},
        {"sentence": "The store displayed free samples as bait to attract customers.", "translation": "その店は顧客を引き付けるために無料サンプルを餌として展示した。"},
        {"sentence": "He couldn't resist the bait of a free vacation offer.", "translation": "彼は無料休暇のオファーの誘いに逆らうことができなかった。"},
    ],
    "imminent": [
        {"sentence": "The weather report warned of an imminent storm.", "translation": "天気予報は差し迫った嵐を警告した。"},
        {"sentence": "An imminent danger required immediate action.", "translation": "差し迫った危険は即座の行動を必要とした。"},
        {"sentence": "The company announced an imminent merger with its competitor.", "translation": "その会社は競争相手との差し迫った合併を発表した。"},
    ],
    "meditate": [
        {"sentence": "Every morning, she meditates for thirty minutes.", "translation": "毎朝、彼女は30分間瞑想をする。"},
        {"sentence": "He meditates on the meaning of life.", "translation": "彼は人生の意味について熟考する。"},
        {"sentence": "The monks meditate in the quiet temple.", "translation": "僧たちは静かな寺院で瞑想する。"},
    ],
    "compartment": [
        {"sentence": "Each compartment of the train was clean and comfortable.", "translation": "列車の各車両は清潔で快適だった。"},
        {"sentence": "She stored her jewelry in a small compartment.", "translation": "彼女は彼女の宝石を小さなコンパートメントに保管した。"},
        {"sentence": "The ship had separate compartments for different purposes.", "translation": "その船はさまざまな目的のための別々の隔室を持っていた。"},
    ],
    "intrinsic": [
        {"sentence": "Education has intrinsic value beyond earning money.", "translation": "教育はお金を稼ぐこと以上の本来の価値を持つ。"},
        {"sentence": "The intrinsic quality of the product impressed customers.", "translation": "その製品の本質的な品質は顧客を感動させた。"},
        {"sentence": "Happiness is intrinsic to living a meaningful life.", "translation": "幸福は有意義な人生を送ることに本来備わっている。"},
    ],
    "incubate": [
        {"sentence": "The bird incubates her eggs for about two weeks.", "translation": "その鳥は約2週間卵を温める。"},
        {"sentence": "The startup incubator helps new companies develop ideas.", "translation": "そのスタートアップインキュベーターは新しい企業がアイデアを開発するのを助ける。"},
        {"sentence": "Scientists incubate bacteria in special containers.", "translation": "科学者たちは特別な容器で細菌を培養する。"},
    ],
    "piper": [
        {"sentence": "The piper played traditional music at the festival.", "translation": "その笛吹きは祭りで伝統的な音楽を演奏した。"},
        {"sentence": "A Scottish piper led the parade with bagpipes.", "translation": "スコットランドの笛吹きはバグパイプで行進を先導した。"},
        {"sentence": "The famous piper attracted large crowds wherever he performed.", "translation": "その有名な笛吹きはどこで演奏しても大勢の群衆を引き付けた。"},
    ],
    "detention": [
        {"sentence": "The student received detention for missing homework.", "translation": "その学生は宿題の提出を忘れたため留置を受けた。"},
        {"sentence": "Immigration detention centers hold people awaiting processing.", "translation": "移民留置センターは処理を待つ人々を収容している。"},
        {"sentence": "The police detained the suspect for questioning.", "translation": "警察は容疑者を尋問のために留置した。"},
    ],
    "libel": [
        {"sentence": "The newspaper was sued for libel against the politician.", "translation": "その新聞はその政治家に対する名誉毀損で訴えられた。"},
        {"sentence": "False statements about someone can be considered libel.", "translation": "誰かについての虚偽の声明は名誉毀損と見なされることができる。"},
        {"sentence": "He won the case against libel and received compensation.", "translation": "彼は名誉毀損に対する訴訟に勝ち、補償を受けた。"},
    ],
    "curb": [
        {"sentence": "Parents need to curb their children's screen time.", "translation": "親は子どものスクリーン時間を制限する必要がある。"},
        {"sentence": "The government tried to curb inflation through new policies.", "translation": "政府は新しい政策を通じてインフレーションを抑制しようとした。"},
        {"sentence": "She parked the car next to the curb of the street.", "translation": "彼女は車を通りの縁石の横に駐車した。"},
    ],
    "cafe": [
        {"sentence": "We met our friends at a cafe for coffee and pastries.", "translation": "私たちは友人とカフェでコーヒーとペストリーで会った。"},
        {"sentence": "The cozy cafe is a popular spot for students to study.", "translation": "その居心地の良いカフェは学生が勉強するための人気スポットだ。"},
        {"sentence": "They opened a new cafe near the university campus.", "translation": "彼らは大学キャンパスの近くに新しいカフェをオープンした。"},
    ],
    "physician": [
        {"sentence": "She scheduled an appointment with her physician.", "translation": "彼女は医者との予約をスケジュールした。"},
        {"sentence": "The physician diagnosed the patient with the flu.", "translation": "医者は患者をインフルエンザと診断した。"},
        {"sentence": "A good physician listens carefully to their patients.", "translation": "良い医者は患者の話をよく聞く。"},
    ],
    "precipitate": [
        {"sentence": "The scandal precipitated the company's downfall.", "translation": "そのスキャンダルはその会社の衰退を招いた。"},
        {"sentence": "Heavy rain precipitated flooding in the region.", "translation": "大雨がその地域の洪水を引き起こした。"},
        {"sentence": "In chemistry, the solution precipitates into crystals.", "translation": "化学では、溶液が結晶に沈殿する。"},
    ],
    "eminent": [
        {"sentence": "An eminent scientist was invited to give a lecture.", "translation": "著名な科学者が講演を行うよう招かれた。"},
        {"sentence": "He achieved eminent success in his field.", "translation": "彼は彼の分野で著名な成功を達成した。"},
        {"sentence": "The eminent professor has won many international awards.", "translation": "その著名な教授は多くの国際賞を受賞している。"},
    ],
    "warranty": [
        {"sentence": "The car comes with a five-year warranty.", "translation": "その車は5年の保証が付いている。"},
        {"sentence": "The manufacturer provides a warranty against defects.", "translation": "製造業者は欠陥に対する保証を提供する。"},
        {"sentence": "There is no warranty that the investment will be profitable.", "translation": "その投資が利益を得るという保証はない。"},
    ],
    "reckless": [
        {"sentence": "The reckless driver was fined for speeding.", "translation": "その無謀なドライバーはスピード違反で罰金を科された。"},
        {"sentence": "It was reckless of him to jump into the water without checking.", "translation": "確認せずに水に飛び込むのは彼の無謀だった。"},
        {"sentence": "The reckless behavior endangered the lives of others.", "translation": "その無謀な行動は他の人たちの命を危険にさらした。"},
    ],
    "hospitality": [
        {"sentence": "The family's hospitality made the guests feel welcome.", "translation": "その家族のもてなしはゲストたちを歓迎されていると感じさせた。"},
        {"sentence": "Hotel industry depends on hospitality to attract customers.", "translation": "ホテル業界はお客さんを引き付けるためにもてなしに依存している。"},
        {"sentence": "We appreciated their warm hospitality during our visit.", "translation": "私たちは訪問中の彼らの温かいもてなしに感謝した。"},
    ],
    "adequacy": [
        {"sentence": "The adequacy of the budget was questioned by the committee.", "translation": "予算の適切性が委員会に疑問視された。"},
        {"sentence": "We must ensure the adequacy of food supplies.", "translation": "食糧供給の十分性を確保する必要がある。"},
        {"sentence": "The adequacy of the facilities improved after renovation.", "translation": "改装後、施設の適切性が向上した。"},
    ],
    "affinity": [
        {"sentence": "She has a natural affinity for languages.", "translation": "彼女は言語に対する自然な親近感を持っている。"},
        {"sentence": "The two countries share cultural affinity.", "translation": "その2つの国は文化的な親近感を共有している。"},
        {"sentence": "His affinity with animals made him a great veterinarian.", "translation": "彼の動物に対する親近感は彼を優れた獣医にした。"},
    ],
    "archer": [
        {"sentence": "The skilled archer hit the target with precision.", "translation": "その熟練した射手は正確に的を射た。"},
        {"sentence": "Ancient archers were essential to military forces.", "translation": "古代の射手は軍隊に不可欠だった。"},
        {"sentence": "The archer drew the bowstring and released the arrow.", "translation": "その射手は弓の弦を引いて矢を放った。"},
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
