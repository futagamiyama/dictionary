#!/usr/bin/env python3
"""Generate example sentences for words ranked 4690-4709"""

from supabase import create_client, Client

# Supabase credentials
url = "https://tvklrujikuanxdddyfcx.supabase.co"
key = "sb_publishable_DLHimQA_Wyt18fOtUH-o3w_1_BGYb0t"
supabase: Client = create_client(url, key)

# Words data
words_data = [
    {"id": "5eade82c-ecc3-40b1-b0c5-9f3a3b0ba6ca", "word": "shuffle", "rank": 4690},
    {"id": "bf3ac478-ba5a-41f9-a54d-d04b546f937e", "word": "salon", "rank": 4691},
    {"id": "438c82e4-fcf4-4ea5-9fe1-66047018de17", "word": "indignant", "rank": 4692},
    {"id": "9343601d-7c29-4a64-9b2c-838391430a7c", "word": "wade", "rank": 4693},
    {"id": "772dffbb-d6cc-48ca-8972-5635984bd4a4", "word": "duchess", "rank": 4694},
    {"id": "fb95ff12-7d1b-4b7d-b24a-973e228e2fb8", "word": "exchequer", "rank": 4695},
    {"id": "dfd6cc40-5967-451a-9588-c3d3d2c6fd95", "word": "disarm", "rank": 4696},
    {"id": "69d34109-899d-4d5f-b08a-16f2bab713f4", "word": "disposition", "rank": 4697},
    {"id": "833169aa-96df-4a1c-9cea-4a3979d9008e", "word": "solemn", "rank": 4698},
    {"id": "786b97b3-c4d6-401a-a496-ea5e115182d7", "word": "demise", "rank": 4700},
    {"id": "56ff8319-0357-4cfd-9e2c-0860bb8010a7", "word": "climax", "rank": 4701},
    {"id": "cbc5b50d-bdb2-457c-b966-da3da3c7c75f", "word": "emulate", "rank": 4702},
    {"id": "528b2a1e-111f-45ec-939d-49ee6fc3c8c5", "word": "adore", "rank": 4703},
    {"id": "2d3eb439-233a-4bc2-bf06-ea1ad9d1d999", "word": "optimism", "rank": 4704},
    {"id": "879dd009-0273-4daa-9240-08193ec6b3fb", "word": "smack", "rank": 4705},
    {"id": "951c1262-97f5-49a2-83eb-7c5afb605db8", "word": "nephew", "rank": 4706},
    {"id": "b880fec2-11d3-4531-bc07-b9d368d4c221", "word": "thorn", "rank": 4707},
    {"id": "409e7425-6314-489c-a401-50d9037844ae", "word": "invoice", "rank": 4708},
    {"id": "72fe6677-e970-4e00-a286-10cb3c466ecd", "word": "fabulous", "rank": 4709},
]

# Example sentences for each word
examples_dict = {
    "shuffle": [
        {"sentence": "He shuffled the deck of cards before dealing.", "translation": "彼は配る前にカードのデックを切った。"},
        {"sentence": "She shuffled her feet nervously while waiting.", "translation": "彼女は待っている間神経質に足を引きずった。"},
        {"sentence": "The manager shuffled the staff assignments.", "translation": "マネージャーはスタッフの割り当てを変更した。"},
    ],
    "salon": [
        {"sentence": "She visited the beauty salon for a haircut.", "translation": "彼女は散髪のために美容サロンを訪問した。"},
        {"sentence": "The salon was decorated with elegant furniture.", "translation": "そのサロンはエレガントな家具で装飾されていた。"},
        {"sentence": "Famous artists gathered at the cultural salon.", "translation": "有名な芸術家たちは文化的なサロンに集まった。"},
    ],
    "indignant": [
        {"sentence": "She was indignant at the rude behavior.", "translation": "彼女は失礼な行動に怒った。"},
        {"sentence": "He gave an indignant response to the accusation.", "translation": "彼は告発に対して怒った返答をした。"},
        {"sentence": "The customers were indignant about the poor service.", "translation": "その顧客たちは貧弱なサービスに怒った。"},
    ],
    "wade": [
        {"sentence": "They waded through the shallow river.", "translation": "彼らは浅い川を歩いて渡った。"},
        {"sentence": "He had to wade through the snow to reach the cabin.", "translation": "彼はキャビンに到達するために雪の中を歩かなければならなかった。"},
        {"sentence": "She waded into the discussion carefully.", "translation": "彼女は慎重に議論に入った。"},
    ],
    "duchess": [
        {"sentence": "The duchess wore an elaborate gown at the ball.", "translation": "その公爵夫人はボールで精巧なガウンを着ていた。"},
        {"sentence": "The duchess was known for her charitable works.", "translation": "その公爵夫人は彼女の慈善事業で知られていた。"},
        {"sentence": "The duchess received guests in the grand hall.", "translation": "その公爵夫人は大ホールでゲストを受け入れた。"},
    ],
    "exchequer": [
        {"sentence": "The exchequer was depleted by military spending.", "translation": "その国庫は軍事支出により枯渇していた。"},
        {"sentence": "The government's exchequer faces a deficit.", "translation": "政府の国庫は赤字に直面している。"},
        {"sentence": "The exchequer received tax revenues from the provinces.", "translation": "その国庫は州からの税収を受け取った。"},
    ],
    "disarm": [
        {"sentence": "The negotiators worked to disarm tensions.", "translation": "その交渉官たちは緊張を緩和するために働いた。"},
        {"sentence": "Her smile could disarm even the angriest person.", "translation": "彼女の笑顔は最も怒った人さえもなだめることができた。"},
        {"sentence": "The government decided to disarm the rebels.", "translation": "政府は反政府勢力を武装解除することを決めた。"},
    ],
    "disposition": [
        {"sentence": "His cheerful disposition brightened everyone's mood.", "translation": "彼の陽気な気質はみんなの気分を明るくした。"},
        {"sentence": "The disposition of the furniture enhanced the room.", "translation": "家具の配置は部屋を向上させた。"},
        {"sentence": "She had no disposition to argue with him.", "translation": "彼女は彼と議論する気質を持っていなかった。"},
    ],
    "solemn": [
        {"sentence": "The solemn ceremony was attended by thousands.", "translation": "その厳肃な式典には数千人が出席した。"},
        {"sentence": "He gave a solemn promise to help.", "translation": "彼は助けるための厳かな約束をした。"},
        {"sentence": "The solemn expression on her face showed concern.", "translation": "彼女の顔の厳粛な表情は懸念を示していた。"},
    ],
    "demise": [
        {"sentence": "The demise of the old company was inevitable.", "translation": "その古い会社の衰退は不可避だった。"},
        {"sentence": "His sudden demise shocked the entire community.", "translation": "彼の突然の死はコミュニティ全体を衝撃した。"},
        {"sentence": "The demise of the monarchy marked a turning point.", "translation": "君主制の衰退は転機をマークした。"},
    ],
    "climax": [
        {"sentence": "The film reached its climax in the final scene.", "translation": "その映画は最終シーンでクライマックスに達した。"},
        {"sentence": "The climax of the story surprised all readers.", "translation": "その物語のクライマックスはすべての読者を驚かせた。"},
        {"sentence": "The performance climaxed with a standing ovation.", "translation": "そのパフォーマンスはスタンディングオベーションでクライマックスに達した。"},
    ],
    "emulate": [
        {"sentence": "Young athletes emulate their sports heroes.", "translation": "若いアスリートは彼らのスポーツのヒーローを見習う。"},
        {"sentence": "She tried to emulate her mother's success.", "translation": "彼女は彼女の母親の成功を見習おうとした。"},
        {"sentence": "Companies emulate the strategies of market leaders.", "translation": "企業は市場リーダーの戦略を見習う。"},
    ],
    "adore": [
        {"sentence": "The children adore their grandfather.", "translation": "その子どもたちは彼らの祖父を愛している。"},
        {"sentence": "She adores chocolate and eats it every day.", "translation": "彼女はチョコレートが好きで毎日食べる。"},
        {"sentence": "Many people adore the music of that composer.", "translation": "多くの人々はその作曲家の音楽を愛している。"},
    ],
    "optimism": [
        {"sentence": "His optimism was inspiring to the team.", "translation": "彼の楽観主義はチームに鼓舞した。"},
        {"sentence": "Despite the challenges, she maintained her optimism.", "translation": "課題にもかかわらず、彼女は彼女の楽観主義を保った。"},
        {"sentence": "Optimism can help people achieve their goals.", "translation": "楽観主義は人々が彼らの目標を達成するのに役立つことができる。"},
    ],
    "smack": [
        {"sentence": "The candy has a lemon smack to it.", "translation": "そのキャンディはそれにレモンの味がある。"},
        {"sentence": "He gave the ball a smack with the bat.", "translation": "彼はコウモリでボールをぴしゃりと打った。"},
        {"sentence": "Her plan smacks of desperation.", "translation": "彼女の計画は絶望のにおいがする。"},
    ],
    "nephew": [
        {"sentence": "My nephew came to visit for the summer.", "translation": "私の甥は夏に訪問に来た。"},
        {"sentence": "She is very close to her nephew.", "translation": "彼女は彼女の甥にとても近い。"},
        {"sentence": "The nephew inherited the family business.", "translation": "その甥は家族事業を相続した。"},
    ],
    "thorn": [
        {"sentence": "The rose had a sharp thorn on its stem.", "translation": "そのバラはその茎に鋭いとげを持っていた。"},
        {"sentence": "The thorn pricked her finger as she picked the flower.", "translation": "そのとげは彼女が花を摘んだとき彼女の指を刺した。"},
        {"sentence": "A thorn in the side means a persistent problem.", "translation": "側面のとげは永続的な問題を意味する。"},
    ],
    "invoice": [
        {"sentence": "The invoice was sent to the customer after delivery.", "translation": "その請求書は配達後に顧客に送られた。"},
        {"sentence": "She carefully reviewed the invoice before paying.", "translation": "彼女は支払う前に請求書を注意深く確認した。"},
        {"sentence": "The company invoiced the client for the services.", "translation": "その会社はサービスの顧客に請求書を送った。"},
    ],
    "fabulous": [
        {"sentence": "She wore a fabulous dress to the party.", "translation": "彼女はパーティーに素晴らしいドレスを着ていった。"},
        {"sentence": "The fabulous success exceeded their expectations.", "translation": "その驚くべき成功は彼らの期待を超えた。"},
        {"sentence": "The chef prepared a fabulous meal for the guests.", "translation": "そのシェフはゲスト向けの素晴らしい食事を準備した。"},
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

    print(f"\n📊 Total examples inserted: {total_inserted}/57")

if __name__ == "__main__":
    insert_examples()
