#!/usr/bin/env python3
"""Generate example sentences for words ranked 5037-5057"""

from supabase import create_client, Client

# Supabase credentials
url = "https://tvklrujikuanxdddyfcx.supabase.co"
key = "sb_publishable_DLHimQA_Wyt18fOtUH-o3w_1_BGYb0t"
supabase: Client = create_client(url, key)

# Words data
words_data = [
    {"id": "d14ea808-475d-44fd-a999-bdbb2be79a84", "word": "winger", "rank": 5037},
    {"id": "24c9919f-49ec-425e-a424-584f09f4f635", "word": "peril", "rank": 5038},
    {"id": "315e5dff-96d4-404c-9a8e-f1a8ffe391d9", "word": "parachute", "rank": 5039},
    {"id": "4096bdac-df4c-4b74-b482-4c6e93226870", "word": "cramp", "rank": 5040},
    {"id": "d4390b5f-555f-4306-b247-7ed47fe29f79", "word": "writ", "rank": 5041},
    {"id": "1b7a886c-2456-4426-9e34-536e660d4b94", "word": "outright", "rank": 5042},
    {"id": "b4245eba-201e-49fa-a056-5d9e982e4dc8", "word": "putt", "rank": 5043},
    {"id": "c6aaa9da-e4c3-4c91-9bdc-b159a92369e0", "word": "corporal", "rank": 5044},
    {"id": "0be20d3f-61f1-436d-8a69-16843eee771e", "word": "coefficient", "rank": 5045},
    {"id": "e05eb8e3-ad52-4e37-ba39-a6412db5157d", "word": "gradient", "rank": 5046},
    {"id": "2091f5fb-c775-4d01-b926-f75d6e7c0c75", "word": "engrave", "rank": 5047},
    {"id": "de5ccb8b-4628-4088-adeb-97042f0a2dd6", "word": "hurl", "rank": 5048},
    {"id": "b598f807-dc53-410b-a124-ba6e6b0d9082", "word": "infuse", "rank": 5049},
    {"id": "10b54ffb-aeb4-4cc5-8ae3-0d7c6d3f8c8b", "word": "plantation", "rank": 5050},
    {"id": "bb84dbdf-9cd7-4c87-9083-7818b60d6724", "word": "buoy", "rank": 5051},
    {"id": "ff7fb91b-6c29-43f3-acb4-9a8172cbf2b1", "word": "vowel", "rank": 5053},
    {"id": "7273d3d4-17c1-4be4-b4de-e52f64a6152f", "word": "telescope", "rank": 5054},
    {"id": "082095bf-12bc-485e-99f0-08edca6be303", "word": "algae", "rank": 5055},
    {"id": "a10407ae-061f-49b4-94b6-739ee54e9b9f", "word": "detriment", "rank": 5056},
    {"id": "50325a83-7dc5-4664-86bf-5e270d5d63a8", "word": "naughty", "rank": 5057},
]

# Example sentences for each word
examples_dict = {
    "winger": [
        {"sentence": "The winger scored a goal from the corner.", "translation": "そのウィンガーはコーナーからゴールを決めました。"},
        {"sentence": "The team's best winger was injured.", "translation": "そのチームの最高のウィンガーが怪我をしました。"},
        {"sentence": "He played as a left winger.", "translation": "彼は左ウィンガーとしてプレーしました。"},
    ],
    "peril": [
        {"sentence": "The sailors were in great peril.", "translation": "その船員たちは大きな危機に瀕していました。"},
        {"sentence": "The city faced peril from flooding.", "translation": "その都市は洪水の危機に直面していました。"},
        {"sentence": "She was warned of the peril ahead.", "translation": "彼女は前方の危機について警告されました。"},
    ],
    "parachute": [
        {"sentence": "The skydiver deployed his parachute.", "translation": "そのスカイダイバーはパラシュートを展開しました。"},
        {"sentence": "The parachute opened safely.", "translation": "そのパラシュートは安全に開きました。"},
        {"sentence": "He jumped with a parachute on his back.", "translation": "彼は背中にパラシュートを背負って飛び降りました。"},
    ],
    "cramp": [
        {"sentence": "She got a cramp in her leg.", "translation": "彼女は足にけいれんが起きました。"},
        {"sentence": "The cramp was very painful.", "translation": "そのけいれんは非常に痛かった。"},
        {"sentence": "Drinking water helped ease the cramp.", "translation": "水を飲むことはけいれんを和らげるのに役立ちました。"},
    ],
    "writ": [
        {"sentence": "The judge issued a writ.", "translation": "その裁判官は令状を発行しました。"},
        {"sentence": "A writ of habeas corpus was filed.", "translation": "人身保護令状が提出されました。"},
        {"sentence": "The writ commanded the defendant to appear in court.", "translation": "その令状は被告に出廷を命じました。"},
    ],
    "outright": [
        {"sentence": "He rejected the offer outright.", "translation": "彼はその申し出を完全に拒否しました。"},
        {"sentence": "It was an outright lie.", "translation": "それは完全なうそでした。"},
        {"sentence": "She gave him an outright refusal.", "translation": "彼女は彼に明確な拒否を与えました。"},
    ],
    "putt": [
        {"sentence": "He missed the putt by inches.", "translation": "彼はインチ単位でパットを外しました。"},
        {"sentence": "She sank a long putt.", "translation": "彼女は長いパットを沈めました。"},
        {"sentence": "The golfer lined up his putt.", "translation": "そのゴルファーは彼のパットをラインに合わせました。"},
    ],
    "corporal": [
        {"sentence": "Corporal punishment is not allowed in schools.", "translation": "学校では体罰は許可されていません。"},
        {"sentence": "The military rank of corporal is below sergeant.", "translation": "兵卒の軍事階級は下士官より低いです。"},
        {"sentence": "He was promoted to corporal.", "translation": "彼は兵卒に昇進しました。"},
    ],
    "coefficient": [
        {"sentence": "The coefficient in the equation is five.", "translation": "その方程式の係数は5です。"},
        {"sentence": "The friction coefficient depends on the surfaces.", "translation": "摩擦係数は表面に依存します。"},
        {"sentence": "Scientists calculated the coefficient of expansion.", "translation": "科学者たちは膨張係数を計算しました。"},
    ],
    "gradient": [
        {"sentence": "The road has a steep gradient.", "translation": "その道路は急な勾配を持っています。"},
        {"sentence": "The temperature gradient affects the weather.", "translation": "温度勾配は天気に影響を与えます。"},
        {"sentence": "The gradient of the hill made climbing difficult.", "translation": "その丘の勾配は登ることを難しくしました。"},
    ],
    "engrave": [
        {"sentence": "They will engrave your name on the trophy.", "translation": "彼らはあなたの名前をトロフィーに刻みます。"},
        {"sentence": "The artist engraved the design into metal.", "translation": "そのアーティストは金属にデザインを刻みました。"},
        {"sentence": "The image was engraved in her memory.", "translation": "そのイメージは彼女の記憶に刻まれました。"},
    ],
    "hurl": [
        {"sentence": "He hurled the ball across the field.", "translation": "彼はボールをフィールド全体に投げました。"},
        {"sentence": "She hurled insults at him.", "translation": "彼女は彼に侮辱を浴びせました。"},
        {"sentence": "The waves hurled the ship against the rocks.", "translation": "その波は船を岩に投げつけました。"},
    ],
    "infuse": [
        {"sentence": "Infuse the tea for five minutes.", "translation": "5分間お茶を浸します。"},
        {"sentence": "The chef will infuse the sauce with herbs.", "translation": "そのシェフはソースにハーブを染み込ませます。"},
        {"sentence": "They sought to infuse energy into the team.", "translation": "彼らはチームにエネルギーを注入しようとしました。"},
    ],
    "plantation": [
        {"sentence": "The plantation produced coffee beans.", "translation": "その農園はコーヒー豆を生産しました。"},
        {"sentence": "They work on a sugar plantation.", "translation": "彼らはサトウキビ農園で働いています。"},
        {"sentence": "The plantation covers hundreds of acres.", "translation": "その農園は数百エーカーをカバーしています。"},
    ],
    "buoy": [
        {"sentence": "The buoy marked the safe channel.", "translation": "そのブイは安全な航路を示しました。"},
        {"sentence": "The buoy was anchored to the seabed.", "translation": "そのブイは海底に停泊していました。"},
        {"sentence": "Hope began to buoy her spirits.", "translation": "希望は彼女の精神を高揚させ始めました。"},
    ],
    "vowel": [
        {"sentence": "The letter 'A' is a vowel.", "translation": "文字「A」は母音です。"},
        {"sentence": "English has five main vowels.", "translation": "英語には5つの主要な母音があります。"},
        {"sentence": "She pronounced the vowel incorrectly.", "translation": "彼女は母音を誤って発音しました。"},
    ],
    "telescope": [
        {"sentence": "The telescope revealed distant stars.", "translation": "その望遠鏡は遠い星を明らかにしました。"},
        {"sentence": "He looked through the telescope.", "translation": "彼は望遠鏡を覗きました。"},
        {"sentence": "The astronomical telescope is powerful.", "translation": "その天文望遠鏡は強力です。"},
    ],
    "algae": [
        {"sentence": "Algae grew in the pond.", "translation": "藻が池で育ちました。"},
        {"sentence": "The water was covered with algae.", "translation": "その水は藻で覆われていました。"},
        {"sentence": "Algae can be used for biofuel.", "translation": "藻はバイオ燃料に使用できます。"},
    ],
    "detriment": [
        {"sentence": "Smoking is a detriment to health.", "translation": "喫煙は健康に悪影響を与えます。"},
        {"sentence": "The scandal was to his detriment.", "translation": "そのスキャンダルは彼に悪影響を与えました。"},
        {"sentence": "Lack of sleep is a detriment to performance.", "translation": "睡眠不足はパフォーマンスに悪影響を与えます。"},
    ],
    "naughty": [
        {"sentence": "The naughty child was sent to bed early.", "translation": "そのいたずら好きな子どもは早く寝かされました。"},
        {"sentence": "He gave her a naughty smile.", "translation": "彼は彼女にいたずら好きな笑みを与えました。"},
        {"sentence": "Naughty behavior will not be tolerated.", "translation": "いたずら好きな行動は容認されません。"},
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
