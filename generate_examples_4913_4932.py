#!/usr/bin/env python3
"""Generate example sentences for words ranked 4913-4932"""

from supabase import create_client, Client

# Supabase credentials
url = "https://tvklrujikuanxdddyfcx.supabase.co"
key = "sb_publishable_DLHimQA_Wyt18fOtUH-o3w_1_BGYb0t"
supabase: Client = create_client(url, key)

# Words data
words_data = [
    {"id": "4a236b8c-3775-4179-9bcf-cb416eae8db1", "word": "indemnity", "rank": 4913},
    {"id": "22bc4571-02a9-407c-98e8-07c9b4c1752d", "word": "versatile", "rank": 4914},
    {"id": "b7409ccf-faff-4fe4-bb04-9e180c3a21e5", "word": "allegiance", "rank": 4915},
    {"id": "39ecbda6-2477-4ba6-acde-35615e925881", "word": "interrogate", "rank": 4916},
    {"id": "db96a689-a922-435b-8ad0-71088328387a", "word": "vintage", "rank": 4917},
    {"id": "f0a30d16-b65b-418f-994b-35529b0c41aa", "word": "dialect", "rank": 4918},
    {"id": "68a734b4-0c54-4aa7-b427-66009b00caf2", "word": "collier", "rank": 4919},
    {"id": "d65a6889-4df7-4e85-939c-40c86b149f99", "word": "communal", "rank": 4920},
    {"id": "49ebc861-a062-48e5-86db-5886329f07e1", "word": "frail", "rank": 4921},
    {"id": "6bc406de-9d75-4cd1-a8ed-f7ce19ed27c3", "word": "synonym", "rank": 4922},
    {"id": "f623f336-2a52-4010-8893-e8f96b3ca7c4", "word": "pamphlet", "rank": 4923},
    {"id": "b1068ecd-8966-4683-8d50-d33cf8f80dfe", "word": "icon", "rank": 4924},
    {"id": "7a21c681-d655-45ad-b026-c37a264f9468", "word": "legion", "rank": 4925},
    {"id": "0ff11350-4c2a-4b35-bc39-73cae194e23a", "word": "scripture", "rank": 4926},
    {"id": "7116b0df-e7d1-42c7-b3bd-779f790b1ec9", "word": "austere", "rank": 4927},
    {"id": "777f5132-173e-4afa-9b98-800b791369f5", "word": "sponge", "rank": 4928},
    {"id": "a2476889-73f0-485d-bdfa-d9dea4757b94", "word": "draught", "rank": 4929},
    {"id": "d13543b2-c10e-4a05-999c-d38807d29e92", "word": "clasp", "rank": 4930},
    {"id": "cfc42b0d-0f2e-40c8-8e38-7964cd46d809", "word": "encode", "rank": 4931},
    {"id": "a8d8279a-a9af-40c9-9a9b-5811909b56fc", "word": "nylon", "rank": 4932},
]

# Example sentences for each word
examples_dict = {
    "indemnity": [
        {"sentence": "The company provided indemnity against losses.", "translation": "その企業は損失に対する補償を提供した。"},
        {"sentence": "Insurance offers indemnity for damage.", "translation": "保険は損害に対する補償を提供します。"},
        {"sentence": "They sought indemnity for the breach of contract.", "translation": "彼らは契約違反に対する補償を求めた。"},
    ],
    "versatile": [
        {"sentence": "A knife is a versatile tool in the kitchen.", "translation": "ナイフは台所での多用途な道具です。"},
        {"sentence": "She is a versatile performer in dance and music.", "translation": "彼女はダンスと音楽での多才なパフォーマーです。"},
        {"sentence": "The software is versatile and easy to use.", "translation": "そのソフトウェアは多用途で使いやすいです。"},
    ],
    "allegiance": [
        {"sentence": "Soldiers swore allegiance to the flag.", "translation": "兵士たちは旗に対する忠誠を誓った。"},
        {"sentence": "Her allegiance was to her family first.", "translation": "彼女の忠誠は最初は彼女の家族にありました。"},
        {"sentence": "The citizens pledged allegiance to the country.", "translation": "市民たちは国に対する忠誠を誓った。"},
    ],
    "interrogate": [
        {"sentence": "Police will interrogate the suspect.", "translation": "警察は容疑者に尋問するでしょう。"},
        {"sentence": "The witness was interrogated for hours.", "translation": "その目撃者は数時間尋問された。"},
        {"sentence": "Lawyers interrogated the defendant in court.", "translation": "弁護士たちは法廷で被告に尋問した。"},
    ],
    "vintage": [
        {"sentence": "He collects vintage cars from the 1960s.", "translation": "彼は1960年代のヴィンテージカーを収集しています。"},
        {"sentence": "This wine is a fine vintage.", "translation": "このワインは優れたヴィンテージです。"},
        {"sentence": "Vintage clothing has become fashionable again.", "translation": "ヴィンテージ衣類は再びファッショナブルになりました。"},
    ],
    "dialect": [
        {"sentence": "The local dialect is difficult to understand.", "translation": "その地元の方言は理解しにくいです。"},
        {"sentence": "She speaks in her native dialect.", "translation": "彼女は彼女の母語の方言を話します。"},
        {"sentence": "The dialect differs from standard English.", "translation": "その方言は標準英語と異なります。"},
    ],
    "collier": [
        {"sentence": "The collier worked in the coal mine.", "translation": "その炭鉱労働者は炭鉱で働いていた。"},
        {"sentence": "A collier ship transported coal.", "translation": "石炭船は石炭を運びました。"},
        {"sentence": "The collier's job was dangerous.", "translation": "その炭鉱労働者の仕事は危険でした。"},
    ],
    "communal": [
        {"sentence": "The communal garden is shared by residents.", "translation": "その共有庭園は住民で共有されています。"},
        {"sentence": "They have communal meals together.", "translation": "彼らは一緒に共有の食事をしています。"},
        {"sentence": "The communal space is used for gatherings.", "translation": "その共有スペースは集まりに使用されます。"},
    ],
    "frail": [
        {"sentence": "The elderly woman was frail and weak.", "translation": "その高齢女性は虚弱で弱かった。"},
        {"sentence": "His health is frail after the illness.", "translation": "病気の後、彼の健康は虚弱です。"},
        {"sentence": "The frail child needed care.", "translation": "その虚弱な子どもはケアが必要でした。"},
    ],
    "synonym": [
        {"sentence": "Happy is a synonym for joyful.", "translation": "「幸せ」は「喜びに満ちた」の同義語です。"},
        {"sentence": "Find a synonym for the underlined word.", "translation": "下線を引かれた単語の同義語を見つけてください。"},
        {"sentence": "Big and large are synonyms.", "translation": "「大きい」と「大きな」は同義語です。"},
    ],
    "pamphlet": [
        {"sentence": "The informational pamphlet explained the program.", "translation": "その情報パンフレットはプログラムを説明した。"},
        {"sentence": "She distributed pamphlets about health.", "translation": "彼女は健康に関するパンフレットを配布した。"},
        {"sentence": "The political pamphlet advocated for change.", "translation": "その政治パンフレットは変化を提唱した。"},
    ],
    "icon": [
        {"sentence": "She is an icon of fashion and style.", "translation": "彼女はファッションとスタイルのアイコンです。"},
        {"sentence": "The app icon appears on the home screen.", "translation": "そのアプリアイコンはホーム画面に表示されます。"},
        {"sentence": "Religious icons decorated the church.", "translation": "宗教的なアイコンが教会を飾りました。"},
    ],
    "legion": [
        {"sentence": "A legion of fans waited outside the theater.", "translation": "大勢のファンが劇場の外で待っていた。"},
        {"sentence": "Roman legions were powerful military units.", "translation": "ローマの軍団は強力な軍事ユニットでした。"},
        {"sentence": "The legion of supporters cheered loudly.", "translation": "その支援者の大軍は大きく歓声を上げた。"},
    ],
    "scripture": [
        {"sentence": "She quoted scripture from the Bible.", "translation": "彼女は聖書から聖句を引用した。"},
        {"sentence": "Religious scripture guides believers.", "translation": "宗教的な聖句は信者を導きます。"},
        {"sentence": "The ancient scriptures are preserved carefully.", "translation": "古い聖句は慎重に保存されています。"},
    ],
    "austere": [
        {"sentence": "The room had an austere design.", "translation": "その部屋は厳格なデザインを持っていた。"},
        {"sentence": "His austere lifestyle reflected his values.", "translation": "彼の厳格なライフスタイルは彼の価値観を反映していた。"},
        {"sentence": "The austere beauty of the landscape impressed us.", "translation": "その風景の厳格な美しさは私たちを感動させました。"},
    ],
    "sponge": [
        {"sentence": "Use a sponge to clean the dishes.", "translation": "スポンジを使用して食器をきれいにしてください。"},
        {"sentence": "The sponge absorbed water easily.", "translation": "そのスポンジは簡単に水を吸収した。"},
        {"sentence": "He acts like a sponge, absorbing information.", "translation": "彼は情報を吸収するスポンジのように行動します。"},
    ],
    "draught": [
        {"sentence": "There was a cold draught from the window.", "translation": "窓から冷たい風が吹いていた。"},
        {"sentence": "A draught of fresh air refreshed him.", "translation": "新鮮な空気の一息は彼をリフレッシュした。"},
        {"sentence": "The draught board was set up for the game.", "translation": "そのドラフトボードはゲームのためにセットアップされた。"},
    ],
    "clasp": [
        {"sentence": "She held the necklace clasp carefully.", "translation": "彼女はネックレスのクラスプを慎重に保持した。"},
        {"sentence": "He clasped her hand warmly.", "translation": "彼は彼女の手を温かく握った。"},
        {"sentence": "The clasp on the bag broke.", "translation": "そのバッグのクラスプが壊れた。"},
    ],
    "encode": [
        {"sentence": "The software will encode the video file.", "translation": "そのソフトウェアはビデオファイルをエンコードします。"},
        {"sentence": "Genes encode information about organisms.", "translation": "遺伝子は生物についての情報をエンコードします。"},
        {"sentence": "We need to encode the message for security.", "translation": "セキュリティのためにメッセージをエンコードする必要があります。"},
    ],
    "nylon": [
        {"sentence": "The nylon rope is strong and durable.", "translation": "そのナイロンロープは強くて耐久性があります。"},
        {"sentence": "Her nylon stockings were fashionable.", "translation": "彼女のナイロンストッキングはファッショナブルでした。"},
        {"sentence": "The tent is made of nylon material.", "translation": "そのテントはナイロン素材で作られています。"},
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
