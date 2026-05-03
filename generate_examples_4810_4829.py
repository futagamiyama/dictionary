#!/usr/bin/env python3
"""Generate example sentences for words ranked 4810-4829"""

from supabase import create_client, Client

# Supabase credentials
url = "https://tvklrujikuanxdddyfcx.supabase.co"
key = "sb_publishable_DLHimQA_Wyt18fOtUH-o3w_1_BGYb0t"
supabase: Client = create_client(url, key)

# Words data
words_data = [
    {"id": "d340d9c1-a43b-44b0-a4e3-3085a86a2269", "word": "preside", "rank": 4810},
    {"id": "592b982f-1b0b-44af-a07d-9f111fe9eb67", "word": "slogan", "rank": 4811},
    {"id": "85ab2b1c-0a7e-441d-a747-122f55f68640", "word": "contraction", "rank": 4812},
    {"id": "4d95884b-2b2a-41fe-bcd7-18913c329320", "word": "mankind", "rank": 4813},
    {"id": "6d98187f-423b-42c6-883c-a09a051a503e", "word": "ale", "rank": 4814},
    {"id": "28e25a46-eae8-43c3-89a9-09fa6dd1a7b3", "word": "daisy", "rank": 4816},
    {"id": "4ef9e741-1063-421e-8449-37a33c9c7a70", "word": "subside", "rank": 4817},
    {"id": "24326d0e-3148-4197-9b4c-b4cd4c4eab9e", "word": "consecutive", "rank": 4818},
    {"id": "8dd23cef-d3b4-4e73-acae-b940cd184dff", "word": "decentralize", "rank": 4819},
    {"id": "f3a9d47d-a0c4-4a8f-b016-d8054b32ea8a", "word": "insulin", "rank": 4820},
    {"id": "175dd64b-4703-4fa1-aa0f-2fc2d73c7f14", "word": "goblin", "rank": 4821},
    {"id": "906473da-354b-4870-b5c2-19fd14169662", "word": "garlic", "rank": 4822},
    {"id": "19ac276d-a9c1-46c6-accb-9d06e0c7c52a", "word": "grill", "rank": 4823},
    {"id": "b711bf9b-7c6d-4917-b123-fc4039327d50", "word": "lapse", "rank": 4824},
    {"id": "f0d1cf4c-0ff8-4a14-81a9-e09ee1036453", "word": "basil", "rank": 4825},
    {"id": "698282ef-a778-4e05-9fb5-fcdbbd6c65a1", "word": "imperative", "rank": 4826},
    {"id": "733cf97a-1642-46d5-9709-7c14b647810d", "word": "requisite", "rank": 4827},
    {"id": "7d6cbd77-79cf-4126-b184-172640ca1c60", "word": "empower", "rank": 4828},
    {"id": "0829d333-bebc-49ad-a233-7c8415112b0f", "word": "anatomy", "rank": 4829},
    {"id": "012556cd-df22-4a9c-acb8-71924d1b6c04", "word": "gloss", "rank": 4830},
]

# Example sentences for each word
examples_dict = {
    "preside": [
        {"sentence": "The judge will preside over the court case.", "translation": "その裁判官はその法廷事件を主宰するだろう。"},
        {"sentence": "She presides over the board meeting every month.", "translation": "彼女は毎月取締役会の会議を司会する。"},
        {"sentence": "The president presides over the government.", "translation": "大統領は政府を統治する。"},
    ],
    "slogan": [
        {"sentence": "The company's slogan is 'Think Different.'", "translation": "その企業のスローガンは「考え方を変えよう」です。"},
        {"sentence": "Protesters marched with slogans calling for change.", "translation": "デモ参加者は変化を求めるスローガンとともに行進した。"},
        {"sentence": "The campaign slogan was catchy and memorable.", "translation": "そのキャンペーンスローガンは覚えやすくて印象的だった。"},
    ],
    "contraction": [
        {"sentence": "The word 'don't' is a contraction of 'do not.'", "translation": "\"don't\"という単語は\"do not\"の縮約形です。"},
        {"sentence": "Muscle contraction allows movement of the body.", "translation": "筋肉の収縮は身体の運動を可能にする。"},
        {"sentence": "The contraction of the economy worried investors.", "translation": "経済の縮小は投資家を心配させた。"},
    ],
    "mankind": [
        {"sentence": "Science has advanced the welfare of mankind.", "translation": "科学は人類の福祉を進歩させた。"},
        {"sentence": "Throughout history, mankind has faced many challenges.", "translation": "歴史を通じて、人類は多くの課題に直面してきた。"},
        {"sentence": "Climate change affects all of mankind.", "translation": "気候変動は人類全体に影響を与える。"},
    ],
    "ale": [
        {"sentence": "The pub served several types of ale.", "translation": "そのパブはいくつかの種類のエールを提供した。"},
        {"sentence": "Dark ale is popular in British pubs.", "translation": "黒いエールはイギリスのパブで人気がある。"},
        {"sentence": "He ordered a pint of ale at the bar.", "translation": "彼はバーでエール1パイントを注文した。"},
    ],
    "daisy": [
        {"sentence": "A white daisy bloomed in the garden.", "translation": "白いデイジーが庭で咲いた。"},
        {"sentence": "Children made daisy chains in the field.", "translation": "子どもたちは野原でデイジーチェーンを作った。"},
        {"sentence": "The daisy is a common wildflower.", "translation": "デイジーは一般的な野生花です。"},
    ],
    "subside": [
        {"sentence": "The storm subsided by evening.", "translation": "その嵐は夕方までに治まった。"},
        {"sentence": "The water level will subside after the rain stops.", "translation": "雨が止まった後、水位は低下するでしょう。"},
        {"sentence": "The pain began to subside after treatment.", "translation": "治療後、痛みは軽くなり始めた。"},
    ],
    "consecutive": [
        {"sentence": "The team won three consecutive games.", "translation": "そのチームは連続して3試合勝った。"},
        {"sentence": "She worked for five consecutive hours.", "translation": "彼女は連続して5時間働いた。"},
        {"sentence": "The days passed in consecutive order.", "translation": "日々は連続した順序で過ぎていった。"},
    ],
    "decentralize": [
        {"sentence": "The government will decentralize decision-making power.", "translation": "政府は意思決定権を地方分権化するだろう。"},
        {"sentence": "Decentralize the authority to local offices.", "translation": "権限を地域のオフィスに分権化してください。"},
        {"sentence": "Many companies decentralize operations to reduce costs.", "translation": "多くの企業はコストを削減するために業務を地方分権化する。"},
    ],
    "insulin": [
        {"sentence": "Diabetes patients need insulin injections.", "translation": "糖尿病患者はインスリン注射を必要とします。"},
        {"sentence": "Insulin regulates blood sugar levels.", "translation": "インスリンは血糖値を調節する。"},
        {"sentence": "The discovery of insulin saved millions of lives.", "translation": "インスリンの発見は何百万もの命を救った。"},
    ],
    "goblin": [
        {"sentence": "In fairy tales, a goblin is a small magical creature.", "translation": "おとぎ話では、ゴブリンは小さな魔法の生き物です。"},
        {"sentence": "The goblin tried to trick the adventurers.", "translation": "ゴブリンは冒険家たちをだまそうとした。"},
        {"sentence": "Children enjoyed the story about the mischievous goblin.", "translation": "子どもたちはいたずら好きなゴブリンについての物語を楽しんだ。"},
    ],
    "garlic": [
        {"sentence": "Garlic adds flavor to many dishes.", "translation": "ニンニクは多くの料理に風味を加える。"},
        {"sentence": "She minced the garlic for the pasta sauce.", "translation": "彼女はパスタソースのためにニンニクをみじん切りにした。"},
        {"sentence": "Garlic is known for its health benefits.", "translation": "ニンニクはその健康上の利益で知られている。"},
    ],
    "grill": [
        {"sentence": "We will grill burgers for dinner.", "translation": "私たちは夕食のためにハンバーガーをグリルするだろう。"},
        {"sentence": "The restaurant uses a charcoal grill.", "translation": "そのレストランは炭火グリルを使用している。"},
        {"sentence": "Grilled vegetables taste delicious.", "translation": "グリルで焼いた野菜はおいしい。"},
    ],
    "lapse": [
        {"sentence": "A lapse in concentration caused the mistake.", "translation": "注意散漫が過ちを引き起こした。"},
        {"sentence": "His insurance policy lapsed due to non-payment.", "translation": "彼の保険証券は未払いのために失効した。"},
        {"sentence": "It was just a momentary lapse of judgment.", "translation": "それはほんの一時的な判断の過誤でした。"},
    ],
    "basil": [
        {"sentence": "Fresh basil makes the pizza taste better.", "translation": "新鮮なバジルはピザの味をよくする。"},
        {"sentence": "The recipe calls for a handful of basil.", "translation": "そのレシピはひとつかみのバジルを必要とします。"},
        {"sentence": "Basil is a common ingredient in Italian cooking.", "translation": "バジルはイタリア料理の一般的な材料です。"},
    ],
    "imperative": [
        {"sentence": "It is imperative that we act immediately.", "translation": "すぐに行動することが必須です。"},
        {"sentence": "Safety is an imperative concern for the company.", "translation": "安全は会社にとって不可欠な関心事です。"},
        {"sentence": "The imperative mood is used for commands.", "translation": "命令法は命令に使用される。"},
    ],
    "requisite": [
        {"sentence": "Good health is a requisite for success.", "translation": "良好な健康は成功に必要である。"},
        {"sentence": "He has all the requisite qualifications.", "translation": "彼はすべての必要な資格を持っている。"},
        {"sentence": "Experience is a requisite for this job.", "translation": "この仕事には経験が必要です。"},
    ],
    "empower": [
        {"sentence": "Education empowers people to achieve their goals.", "translation": "教育は人々が目標を達成することを力づける。"},
        {"sentence": "The new law empowers local governments.", "translation": "新しい法律は地方政府を権限を与える。"},
        {"sentence": "We should empower women in the workplace.", "translation": "私たちは職場の女性に力を与えるべきです。"},
    ],
    "anatomy": [
        {"sentence": "She studied human anatomy in medical school.", "translation": "彼女は医学部で人体解剖学を学んだ。"},
        {"sentence": "Understanding anatomy helps doctors treat patients.", "translation": "解剖学を理解することは医者が患者を治療するのを助ける。"},
        {"sentence": "The anatomy of the heart is fascinating.", "translation": "心臓の解剖学は魅力的です。"},
    ],
    "gloss": [
        {"sentence": "The magazine's pages had a glossy gloss.", "translation": "その雑誌のページは光沢のある光沢を持っていた。"},
        {"sentence": "She applied lip gloss before the party.", "translation": "彼女はパーティーの前にリップグロスを塗った。"},
        {"sentence": "The teacher added a gloss explaining difficult terms.", "translation": "その先生は難しい用語を説明する注釈を加えた。"},
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
