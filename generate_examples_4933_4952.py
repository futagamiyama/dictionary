#!/usr/bin/env python3
"""Generate example sentences for words ranked 4933-4952"""

from supabase import create_client, Client

# Supabase credentials
url = "https://tvklrujikuanxdddyfcx.supabase.co"
key = "sb_publishable_DLHimQA_Wyt18fOtUH-o3w_1_BGYb0t"
supabase: Client = create_client(url, key)

# Words data
words_data = [
    {"id": "d99a9afd-bd20-4755-8354-58e86a1c110b", "word": "pear", "rank": 4933},
    {"id": "c45c8e71-6746-4291-8966-fb887821e12f", "word": "mandate", "rank": 4934},
    {"id": "dfdb1fc5-eae2-4883-984c-151b3f1fab3b", "word": "delta", "rank": 4935},
    {"id": "86cc12a3-b1f9-492e-84d8-5f55cdadf7cc", "word": "relish", "rank": 4936},
    {"id": "2a36ce50-8cfa-4c0f-a2cc-e86e8e677eeb", "word": "outing", "rank": 4937},
    {"id": "cb635809-00e8-4522-900b-9b426b38eb0c", "word": "wretch", "rank": 4938},
    {"id": "3b7ea007-096b-445d-8334-2c1155981ba4", "word": "noon", "rank": 4939},
    {"id": "982fa93e-aa98-48f1-86ad-b1b8239a5fed", "word": "aerial", "rank": 4940},
    {"id": "20443b76-2f4a-4707-8018-a0013169830d", "word": "dinosaur", "rank": 4941},
    {"id": "f83ac7f3-b5a5-44b1-8fb1-866b4655c15f", "word": "blot", "rank": 4942},
    {"id": "c59bb54c-dcb9-4a2c-99ff-bc0dd57a4fa9", "word": "brood", "rank": 4943},
    {"id": "ca6063e4-b18b-4fe0-aee9-4f5fafdf59ca", "word": "chuckle", "rank": 4944},
    {"id": "4ad016da-fcbc-452e-b4f1-fe12efbb7874", "word": "erode", "rank": 4945},
    {"id": "ac51d85b-6921-4543-98f6-bd20d2a3fa99", "word": "influenza", "rank": 4946},
    {"id": "36e4130c-b04a-4964-ae71-231907c65c17", "word": "qualitative", "rank": 4947},
    {"id": "563d8d40-5faf-4a50-a1ff-03a234e0d65b", "word": "snack", "rank": 4948},
    {"id": "c1fc4c64-15aa-4899-8bb6-d89781fbac66", "word": "bland", "rank": 4949},
    {"id": "23f82c2c-7b18-42ef-8fbe-a561bd9c7e19", "word": "clad", "rank": 4950},
    {"id": "32a417cb-5887-4e01-bc6f-46c4bd55fba9", "word": "cone", "rank": 4951},
    {"id": "bff2946d-6f6e-4249-9d92-0b2edc6c98d4", "word": "purify", "rank": 4952},
]

# Example sentences for each word
examples_dict = {
    "pear": [
        {"sentence": "She bit into the juicy pear.", "translation": "彼女は多汁性のナシをかじった。"},
        {"sentence": "A pear tree grows in their garden.", "translation": "彼らの庭にナシの木が育ちます。"},
        {"sentence": "Pears are a healthy fruit to eat.", "translation": "ナシは食べるのに健康的な果物です。"},
    ],
    "mandate": [
        {"sentence": "The government has a mandate to act.", "translation": "政府は行動する義務があります。"},
        {"sentence": "The mandate was granted by the voters.", "translation": "その委任は有権者から付与されました。"},
        {"sentence": "She refused to follow his mandate.", "translation": "彼女は彼の指令に従うことを拒否した。"},
    ],
    "delta": [
        {"sentence": "The delta is where the river meets the ocean.", "translation": "デルタは川が海と出会う場所です。"},
        {"sentence": "The Nile Delta is very fertile.", "translation": "ナイルデルタは非常に肥沃です。"},
        {"sentence": "The delta region is home to many species.", "translation": "そのデルタ地域は多くの種の家です。"},
    ],
    "relish": [
        {"sentence": "He ate his sandwich with relish.", "translation": "彼は喜んでサンドイッチを食べました。"},
        {"sentence": "She relished the opportunity to travel.", "translation": "彼女は旅行の機会を満喫した。"},
        {"sentence": "The relish added flavor to the hot dog.", "translation": "そのレリッシュはホットドッグに風味を加えた。"},
    ],
    "outing": [
        {"sentence": "The school planned an outing to the museum.", "translation": "学校は博物館への遠足を計画した。"},
        {"sentence": "We had a family outing to the park.", "translation": "私たちは公園への家族の遠足をしました。"},
        {"sentence": "The outing was canceled due to rain.", "translation": "その遠足は雨のためにキャンセルされました。"},
    ],
    "wretch": [
        {"sentence": "The poor wretch had nowhere to go.", "translation": "その哀れな人は行く場所がなかった。"},
        {"sentence": "He felt like a miserable wretch.", "translation": "彼は惨めな人のように感じました。"},
        {"sentence": "That wretch deserves no sympathy.", "translation": "その嫌な奴は同情の余地がありません。"},
    ],
    "noon": [
        {"sentence": "We will meet at noon tomorrow.", "translation": "私たちは明日正午に会うでしょう。"},
        {"sentence": "The sun is highest at noon.", "translation": "太陽は正午に最も高いです。"},
        {"sentence": "Lunch is served at noon.", "translation": "昼食は正午に提供されます。"},
    ],
    "aerial": [
        {"sentence": "The aerial photograph showed the whole city.", "translation": "その航空写真は都市全体を示した。"},
        {"sentence": "An aerial view reveals the landscape.", "translation": "航空的な見方は風景を明らかにします。"},
        {"sentence": "The TV antenna needs an aerial connection.", "translation": "そのテレビアンテナは航空接続が必要です。"},
    ],
    "dinosaur": [
        {"sentence": "The dinosaur was very large.", "translation": "その恐竜は非常に大きかった。"},
        {"sentence": "Children are fascinated by dinosaurs.", "translation": "子どもたちは恐竜に魅了されています。"},
        {"sentence": "The museum has dinosaur fossils.", "translation": "その博物館は恐竜の化石を持っています。"},
    ],
    "blot": [
        {"sentence": "An ink blot appeared on the paper.", "translation": "紙にインク汚れが現れた。"},
        {"sentence": "The stain was a blot on his reputation.", "translation": "そのしみは彼の評判の汚点でした。"},
        {"sentence": "She blotted the spill with a cloth.", "translation": "彼女はこぼれたものを布で拭き取った。"},
    ],
    "brood": [
        {"sentence": "She brooded over the unfair decision.", "translation": "彼女は不公正な決定について沈思した。"},
        {"sentence": "The bird sits on her brood of eggs.", "translation": "その鳥は彼女の一団の卵の上に座っています。"},
        {"sentence": "Don't brood about things you can't change.", "translation": "変えられないことについて思い悩まないでください。"},
    ],
    "chuckle": [
        {"sentence": "He gave a quiet chuckle.", "translation": "彼は静かに笑った。"},
        {"sentence": "She chuckled at the funny joke.", "translation": "彼女は面白いジョークに笑った。"},
        {"sentence": "The audience chuckled at his humor.", "translation": "観客は彼のユーモアに笑った。"},
    ],
    "erode": [
        {"sentence": "Water erodes the rock over time.", "translation": "水は時間とともに岩を浸食します。"},
        {"sentence": "Erosion will erode the mountainside.", "translation": "侵食は山の側面を浸食するでしょう。"},
        {"sentence": "Doubt began to erode his confidence.", "translation": "疑いは彼の自信を損なわせ始めた。"},
    ],
    "influenza": [
        {"sentence": "He caught influenza last winter.", "translation": "彼は去年の冬にインフルエンザにかかった。"},
        {"sentence": "The influenza vaccine is available.", "translation": "インフルエンザワクチンは入手可能です。"},
        {"sentence": "Many people suffered from influenza.", "translation": "多くの人々がインフルエンザに苦しんだ。"},
    ],
    "qualitative": [
        {"sentence": "The qualitative analysis showed improvements.", "translation": "その定性的な分析は改善を示した。"},
        {"sentence": "We conducted a qualitative research study.", "translation": "私たちは定性的な研究を実施した。"},
        {"sentence": "Qualitative data is hard to measure.", "translation": "定性的なデータは測定しにくいです。"},
    ],
    "snack": [
        {"sentence": "Have a snack if you're hungry.", "translation": "お腹がすいたらスナックを食べてください。"},
        {"sentence": "We enjoyed snacks after the movie.", "translation": "映画の後、私たちはスナックを楽しみました。"},
        {"sentence": "Healthy snacks are better than junk food.", "translation": "健康的なスナックはジャンクフードより良いです。"},
    ],
    "bland": [
        {"sentence": "The food was bland and tasteless.", "translation": "その食べ物は味気なく味がなかった。"},
        {"sentence": "His bland expression showed no emotion.", "translation": "彼の無表情な表情は感情を示さなかった。"},
        {"sentence": "The bland diet is recommended for the sick.", "translation": "その淡色食は病人に推奨されます。"},
    ],
    "clad": [
        {"sentence": "He was clad in warm winter clothes.", "translation": "彼は暖かい冬の服を着ていました。"},
        {"sentence": "The soldiers were clad in armor.", "translation": "その兵士たちは鎧を着ていました。"},
        {"sentence": "She was clad in a beautiful dress.", "translation": "彼女は美しいドレスを着ていました。"},
    ],
    "cone": [
        {"sentence": "The ice cream cone was delicious.", "translation": "そのアイスクリームコーンはおいしかった。"},
        {"sentence": "The traffic cone blocked the road.", "translation": "そのトラフィックコーンは道路をふさいだ。"},
        {"sentence": "A cone is a three-dimensional shape.", "translation": "円錐は三次元形状です。"},
    ],
    "purify": [
        {"sentence": "Water filters help purify drinking water.", "translation": "水フィルターは飲料水を浄化するのに役立ちます。"},
        {"sentence": "The ceremony is meant to purify the soul.", "translation": "その儀式は魂を浄化することを目的としています。"},
        {"sentence": "We need to purify the contaminated air.", "translation": "私たちは汚染された空気を浄化する必要があります。"},
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
