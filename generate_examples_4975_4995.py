#!/usr/bin/env python3
"""Generate example sentences for words ranked 4975-4995"""

from supabase import create_client, Client

# Supabase credentials
url = "https://tvklrujikuanxdddyfcx.supabase.co"
key = "sb_publishable_DLHimQA_Wyt18fOtUH-o3w_1_BGYb0t"
supabase: Client = create_client(url, key)

# Words data
words_data = [
    {"id": "d818f1f0-806f-4ccf-a3fa-e297718714ad", "word": "veto", "rank": 4975},
    {"id": "945e95fc-ecdd-4db7-a631-413b8249b95b", "word": "quiz", "rank": 4976},
    {"id": "3b5fbdc0-5903-4168-a9f4-b9dda437fcfa", "word": "antibiotic", "rank": 4977},
    {"id": "62745ec9-c712-4626-9bf7-98bb03c84371", "word": "jealousy", "rank": 4978},
    {"id": "eea5606f-8981-43a4-a766-5fd7f5f800e8", "word": "mischief", "rank": 4979},
    {"id": "47e41c55-8ea3-45a5-9870-6973de80e6b1", "word": "ceramic", "rank": 4981},
    {"id": "8b216967-d3f0-4ad0-8ed7-679dc3e1ed93", "word": "chatter", "rank": 4982},
    {"id": "e3847f36-8a62-4280-9013-c7d5781ee3e8", "word": "muse", "rank": 4983},
    {"id": "98890794-98d6-4f08-8c06-b41e1fdf5cf1", "word": "paradigm", "rank": 4984},
    {"id": "8c834179-3007-462a-88f0-00127fca8bde", "word": "torment", "rank": 4985},
    {"id": "9e119a43-363d-48b9-b9eb-6f0fb6aa132d", "word": "hare", "rank": 4986},
    {"id": "d60067ec-524c-4d99-86db-fe99919d8abe", "word": "crag", "rank": 4987},
    {"id": "46220810-6aca-4bbc-b845-85a1f52b2b28", "word": "intercept", "rank": 4988},
    {"id": "730ff013-4a3c-4a24-83d0-a5341b0c6b40", "word": "lavish", "rank": 4989},
    {"id": "dc497b90-13a8-4fc3-a91c-984167ff92e0", "word": "segregate", "rank": 4990},
    {"id": "dc4f2c62-2d41-4111-80be-e3471aabc18d", "word": "tractor", "rank": 4991},
    {"id": "6b15b9e2-bd48-4c48-b2a2-5e0ed896c04e", "word": "oracle", "rank": 4992},
    {"id": "f52df16a-fae7-4ab1-ad32-86dac1bf035a", "word": "franc", "rank": 4993},
    {"id": "9073e6b0-3407-47ba-a20b-8703d25e28c3", "word": "blossom", "rank": 4994},
    {"id": "dfe1a7db-0b65-43f1-85fc-fe7497b6fe4a", "word": "ignorant", "rank": 4995},
]

# Example sentences for each word
examples_dict = {
    "veto": [
        {"sentence": "The president used his veto power.", "translation": "大統領は彼の拒否権を使用しました。"},
        {"sentence": "Congress can override a presidential veto.", "translation": "議会は大統領の拒否権を覆すことができます。"},
        {"sentence": "He decided to veto the proposal.", "translation": "彼は提案を拒否することに決めました。"},
    ],
    "quiz": [
        {"sentence": "We have a quiz tomorrow in math class.", "translation": "明日、数学のクラスでクイズがあります。"},
        {"sentence": "The teacher gave us a surprise quiz.", "translation": "その先生は私たちにサプライズクイズを与えました。"},
        {"sentence": "How did you do on the quiz?", "translation": "クイズでどのようにしましたか？"},
    ],
    "antibiotic": [
        {"sentence": "The doctor prescribed an antibiotic.", "translation": "医者は抗生物質を処方しました。"},
        {"sentence": "Antibiotics help fight bacterial infections.", "translation": "抗生物質は細菌感染と戦うのに役立ちます。"},
        {"sentence": "Take the antibiotic as directed.", "translation": "指示通りに抗生物質を服用してください。"},
    ],
    "jealousy": [
        {"sentence": "His jealousy ruined the relationship.", "translation": "彼の嫉妬は関係を台無しにしました。"},
        {"sentence": "She felt a pang of jealousy.", "translation": "彼女は嫉妬の痛みを感じた。"},
        {"sentence": "Jealousy is a destructive emotion.", "translation": "嫉妬は破壊的な感情です。"},
    ],
    "mischief": [
        {"sentence": "The children were full of mischief.", "translation": "その子どもたちはいたずらでいっぱいでした。"},
        {"sentence": "He had a mischievous glint in his eye.", "translation": "彼の目にはいたずら好きな輝きがありました。"},
        {"sentence": "The mischief caused some damage.", "translation": "そのいたずらは若干の被害を引き起こしました。"},
    ],
    "ceramic": [
        {"sentence": "The ceramic tiles are beautiful.", "translation": "その陶製タイルは美しいです。"},
        {"sentence": "She collects ceramic figurines.", "translation": "彼女は陶製の人形を収集しています。"},
        {"sentence": "Ceramic bowls are durable.", "translation": "陶製のボウルは耐久性があります。"},
    ],
    "chatter": [
        {"sentence": "The students' chatter filled the classroom.", "translation": "その学生のおしゃべりが教室を満たしました。"},
        {"sentence": "She chattered excitedly about the trip.", "translation": "彼女は旅行について興奮して話しかけた。"},
        {"sentence": "The birds' chatter woke me up.", "translation": "その鳥のさえずりは私を起こしました。"},
    ],
    "muse": [
        {"sentence": "He mused about the future.", "translation": "彼は未来について沈思した。"},
        {"sentence": "Artists seek inspiration from their muse.", "translation": "アーティストたちは彼らのミューズからインスピレーションを求めます。"},
        {"sentence": "She mused quietly while walking.", "translation": "彼女は歩きながら静かに沈思した。"},
    ],
    "paradigm": [
        {"sentence": "This discovery represents a paradigm shift.", "translation": "この発見はパラダイムシフトを表しています。"},
        {"sentence": "The paradigm in education is changing.", "translation": "教育のパラダイムは変わっています。"},
        {"sentence": "A new paradigm was established.", "translation": "新しいパラダイムが確立されました。"},
    ],
    "torment": [
        {"sentence": "The pain caused him great torment.", "translation": "その痛みは彼に大きな苦しみをもたらしました。"},
        {"sentence": "She was tormented by guilt.", "translation": "彼女は罪悪感に苦しめられました。"},
        {"sentence": "The torment lasted for months.", "translation": "その苦しみは数ヶ月間続きました。"},
    ],
    "hare": [
        {"sentence": "The hare ran quickly through the field.", "translation": "そのノウサギは野原を素早く走った。"},
        {"sentence": "The hare is faster than a rabbit.", "translation": "ノウサギはウサギより速いです。"},
        {"sentence": "In the fable, the hare raced the tortoise.", "translation": "そのおとぎ話では、ノウサギはカメとレースをしました。"},
    ],
    "crag": [
        {"sentence": "The eagle perched on the crag.", "translation": "そのワシは崖に止まりました。"},
        {"sentence": "The climbers navigated the rocky crag.", "translation": "その登山者たちは岩だらけの崖をナビゲートしました。"},
        {"sentence": "The crag overlooked the valley.", "translation": "その崖は谷を見下ろしていました。"},
    ],
    "intercept": [
        {"sentence": "The police will intercept the shipment.", "translation": "警察は出荷を傍受するでしょう。"},
        {"sentence": "He intercepted the pass in football.", "translation": "彼はフットボールでパスを傍受しました。"},
        {"sentence": "The message was intercepted by enemies.", "translation": "そのメッセージは敵によって傍受されました。"},
    ],
    "lavish": [
        {"sentence": "They had a lavish wedding ceremony.", "translation": "彼らは豪華な結婚式を挙げました。"},
        {"sentence": "The lavish decoration impressed everyone.", "translation": "その豪華な装飾は誰もを感動させました。"},
        {"sentence": "He lavished praise on the team.", "translation": "彼はチームに賞賛を惜しみなく与えました。"},
    ],
    "segregate": [
        {"sentence": "Laws once segregated people by race.", "translation": "法律は一度人々を人種で隔離しました。"},
        {"sentence": "The school does not segregate students.", "translation": "その学校は学生を隔離しません。"},
        {"sentence": "Segregation caused social division.", "translation": "人種隔離は社会的分裂を引き起こしました。"},
    ],
    "tractor": [
        {"sentence": "The farmer used a tractor to plow the field.", "translation": "その農民はトラクターを使用して畑を耕しました。"},
        {"sentence": "The tractor is powerful and efficient.", "translation": "そのトラクターは強力で効率的です。"},
        {"sentence": "Modern tractors have advanced features.", "translation": "現代のトラクターは高度な機能を持っています。"},
    ],
    "oracle": [
        {"sentence": "The ancient oracle gave prophecies.", "translation": "その古代の神託は予言を与えました。"},
        {"sentence": "People consulted the oracle for guidance.", "translation": "人々は指導のためにその神託に相談しました。"},
        {"sentence": "The oracle's predictions came true.", "translation": "その神託の予言は現実になりました。"},
    ],
    "franc": [
        {"sentence": "The franc was the currency of France.", "translation": "フランは フランスの通貨でした。"},
        {"sentence": "She exchanged dollars for francs.", "translation": "彼女はドルをフランに交換しました。"},
        {"sentence": "The Swiss franc is still in use.", "translation": "スイスフランはまだ使用されています。"},
    ],
    "blossom": [
        {"sentence": "The cherry blossoms are beautiful.", "translation": "その桜は美しいです。"},
        {"sentence": "The flowers will blossom in spring.", "translation": "その花は春に咲くでしょう。"},
        {"sentence": "Her talent continued to blossom.", "translation": "彼女の才能は引き続き開花しました。"},
    ],
    "ignorant": [
        {"sentence": "He was ignorant of the facts.", "translation": "彼は事実を知りませんでした。"},
        {"sentence": "Ignorance is not an excuse.", "translation": "無知は言い訳ではありません。"},
        {"sentence": "She made an ignorant comment.", "translation": "彼女は無知なコメントをしました。"},
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
