#!/usr/bin/env python3
"""Generate example sentences for words ranked 4852-4871"""

from supabase import create_client, Client

# Supabase credentials
url = "https://tvklrujikuanxdddyfcx.supabase.co"
key = "sb_publishable_DLHimQA_Wyt18fOtUH-o3w_1_BGYb0t"
supabase: Client = create_client(url, key)

# Words data
words_data = [
    {"id": "e7ed6d4f-58a6-4b13-8b17-28e38de4331f", "word": "slender", "rank": 4852},
    {"id": "bd689851-199a-4951-8f36-4b5c15825114", "word": "groove", "rank": 4853},
    {"id": "d3080089-dc4c-4f92-a5e0-138951ab50d0", "word": "campus", "rank": 4854},
    {"id": "410d2bde-448f-4b3b-8960-fd7e9954e580", "word": "condense", "rank": 4855},
    {"id": "c02042a4-64fb-44d7-b618-25dfd7fa848a", "word": "emigrate", "rank": 4856},
    {"id": "1b7745cf-2c1b-4910-857e-e754cdb4bfed", "word": "posture", "rank": 4857},
    {"id": "7f5ce893-2354-49b3-9ab4-78d10467bdc2", "word": "transparent", "rank": 4858},
    {"id": "821e12b3-e6e1-4070-b040-995cdf620406", "word": "bog", "rank": 4859},
    {"id": "0a354232-396f-4dc8-ae37-1759fb5ce0fe", "word": "tram", "rank": 4860},
    {"id": "8eb76d34-7db2-4cba-b59c-5b6cb0911bda", "word": "farewell", "rank": 4861},
    {"id": "c858948a-11d9-4263-90f5-020dd360efa9", "word": "jeopardy", "rank": 4862},
    {"id": "8c53a93d-f827-4522-a6c5-53c66f213263", "word": "obscene", "rank": 4863},
    {"id": "9bb41554-d3b1-4229-81ec-aa212502cb4c", "word": "tolerance", "rank": 4864},
    {"id": "c6f127a4-b087-4e52-9b52-0e4ca9ed6420", "word": "latent", "rank": 4865},
    {"id": "91d81a01-fa25-400b-afc6-59577f9b2137", "word": "beta", "rank": 4866},
    {"id": "ada9bf74-056f-4245-a25f-ad13d377c572", "word": "pastoral", "rank": 4867},
    {"id": "e598ec1a-0bb9-4719-9f9f-9abbed638911", "word": "retort", "rank": 4868},
    {"id": "d1ca356d-e6ab-4aaa-bcf9-2756aca95239", "word": "algorithm", "rank": 4869},
    {"id": "3316eefb-8ba2-441a-ba5f-fb716a0facc0", "word": "amenity", "rank": 4870},
    {"id": "0caeb277-4265-45b0-8eee-8a7da9349573", "word": "booth", "rank": 4871},
]

# Example sentences for each word
examples_dict = {
    "slender": [
        {"sentence": "The slender tree swayed in the wind.", "translation": "その細い木は風でゆれた。"},
        {"sentence": "She has a slender figure.", "translation": "彼女はほっそりとした体つきをしている。"},
        {"sentence": "A slender chance of success remained.", "translation": "成功のわずかな可能性が残っていた。"},
    ],
    "groove": [
        {"sentence": "The wheels fit into the groove on the track.", "translation": "車輪は線路の溝に合った。"},
        {"sentence": "Music makes you want to get in the groove.", "translation": "音楽はあなたをリズムに乗せたくなります。"},
        {"sentence": "He fell into a groove and became stuck in routine.", "translation": "彼は決まった習慣にはまり込んだ。"},
    ],
    "campus": [
        {"sentence": "The university campus is very large.", "translation": "その大学のキャンパスは非常に大きい。"},
        {"sentence": "Students walk across the campus every day.", "translation": "学生たちは毎日キャンパスを歩く。"},
        {"sentence": "The campus has beautiful gardens.", "translation": "そのキャンパスは美しい庭園を持っている。"},
    ],
    "condense": [
        {"sentence": "Heat will condense the steam into water.", "translation": "熱は蒸気を水に凝結させる。"},
        {"sentence": "Can you condense this document into one page?", "translation": "このドキュメントを1ページに圧縮できますか？"},
        {"sentence": "Condense the information before presenting.", "translation": "提示する前に情報を圧縮してください。"},
    ],
    "emigrate": [
        {"sentence": "Many people emigrate to find better opportunities.", "translation": "多くの人々はより良い機会を見つけるために移民する。"},
        {"sentence": "He decided to emigrate from his home country.", "translation": "彼は祖国から移民することに決めた。"},
        {"sentence": "People emigrate for economic reasons.", "translation": "人々は経済的な理由で移民する。"},
    ],
    "posture": [
        {"sentence": "Good posture is important for health.", "translation": "良い姿勢は健康に重要です。"},
        {"sentence": "He maintained an upright posture.", "translation": "彼は直立した姿勢を保った。"},
        {"sentence": "Her posture showed confidence and strength.", "translation": "彼女の姿勢は自信と強さを示した。"},
    ],
    "transparent": [
        {"sentence": "The transparent glass allows you to see through.", "translation": "その透明なガラスは透視することができます。"},
        {"sentence": "The government promised transparent policies.", "translation": "政府は透明な政策を約束した。"},
        {"sentence": "The water in the pool was completely transparent.", "translation": "そのプールの水は完全に透明でした。"},
    ],
    "bog": [
        {"sentence": "The bog is a wetland ecosystem.", "translation": "その沼地は湿地生態系です。"},
        {"sentence": "Don't get bogged down in details.", "translation": "詳細にこだわらないでください。"},
        {"sentence": "The hiker got stuck in the bog.", "translation": "そのハイカーは沼地で立ち往生した。"},
    ],
    "tram": [
        {"sentence": "The tram runs along the main street.", "translation": "そのトラムは主通りを走っている。"},
        {"sentence": "We took the tram to the city center.", "translation": "私たちは市の中心部へトラムで行った。"},
        {"sentence": "The tram was crowded during rush hour.", "translation": "ラッシュアワー中、そのトラムは混雑していた。"},
    ],
    "farewell": [
        {"sentence": "She waved a tearful farewell.", "translation": "彼女は涙の別れを手で振った。"},
        {"sentence": "The farewell party was emotional.", "translation": "その別れのパーティーは感情的だった。"},
        {"sentence": "He said farewell to his friends.", "translation": "彼は友人たちに別れを告げた。"},
    ],
    "jeopardy": [
        {"sentence": "The project is in jeopardy due to budget cuts.", "translation": "予算削減により、そのプロジェクトは危機に瀕している。"},
        {"sentence": "Your health is in jeopardy if you smoke.", "translation": "喫煙すると健康が危険にさらされます。"},
        {"sentence": "The company's future is in jeopardy.", "translation": "その企業の将来は危機に瀕している。"},
    ],
    "obscene": [
        {"sentence": "The language used was obscene and offensive.", "translation": "使用された言語は猥褻で攻撃的でした。"},
        {"sentence": "The movie contained obscene content.", "translation": "その映画は猥褻なコンテンツを含んでいた。"},
        {"sentence": "Such behavior is considered obscene in society.", "translation": "そのような行動は社会で猥褻と見なされます。"},
    ],
    "tolerance": [
        {"sentence": "Religious tolerance is important in diverse societies.", "translation": "宗教的寛容は多様な社会で重要です。"},
        {"sentence": "The body builds tolerance to the medication.", "translation": "体は薬剤への耐性を構築します。"},
        {"sentence": "We need to promote tolerance and understanding.", "translation": "私たちは寛容さと理解を促進する必要があります。"},
    ],
    "latent": [
        {"sentence": "The latent energy in the system will be released.", "translation": "システムの潜在的なエネルギーが解放されるでしょう。"},
        {"sentence": "Her latent talent for singing was discovered.", "translation": "彼女の歌唱の潜在的な才能が発見された。"},
        {"sentence": "The latent heat causes the water to evaporate.", "translation": "潜熱は水を蒸発させる。"},
    ],
    "beta": [
        {"sentence": "The software is still in beta testing.", "translation": "そのソフトウェアはまだベータテスト中です。"},
        {"sentence": "Beta versions often have bugs.", "translation": "ベータ版にはしばしばバグがあります。"},
        {"sentence": "Users can try the beta release for free.", "translation": "ユーザーはベータリリースを無料で試すことができます。"},
    ],
    "pastoral": [
        {"sentence": "The pastoral landscape was peaceful and beautiful.", "translation": "その牧歌的な風景は平和で美しかった。"},
        {"sentence": "She chose a pastoral setting for her home.", "translation": "彼女は彼女の家のために田舎の環境を選んだ。"},
        {"sentence": "The pastoral poem describes rural life.", "translation": "その牧歌的な詩は農村生活を説明する。"},
    ],
    "retort": [
        {"sentence": "She made a sharp retort to his criticism.", "translation": "彼女は彼の批評に対して鋭い返答をした。"},
        {"sentence": "His retort was quick and witty.", "translation": "彼の返答は素早く機知に富んでいた。"},
        {"sentence": "'Not at all,' he retorted angrily.", "translation": "「全くそうではない」と彼は怒って言い返した。"},
    ],
    "algorithm": [
        {"sentence": "The algorithm helps predict market trends.", "translation": "そのアルゴリズムは市場トレンドを予測するのに役立ちます。"},
        {"sentence": "Computer programs use algorithms to solve problems.", "translation": "コンピュータプログラムはアルゴリズムを使用して問題を解決します。"},
        {"sentence": "The new algorithm is more efficient than the old one.", "translation": "新しいアルゴリズムは古いものより効率的です。"},
    ],
    "amenity": [
        {"sentence": "The hotel offers various amenities for guests.", "translation": "そのホテルはゲストのための様々な設備を提供しています。"},
        {"sentence": "Modern apartments include luxury amenities.", "translation": "現代のアパートには高級設備が含まれています。"},
        {"sentence": "The resort has excellent amenities.", "translation": "そのリゾートは優れた設備を持っている。"},
    ],
    "booth": [
        {"sentence": "The photographer set up a booth at the fair.", "translation": "その写真家はフェアブースを設置した。"},
        {"sentence": "We sat in a booth at the restaurant.", "translation": "私たちはレストランのブースに座った。"},
        {"sentence": "The phone booth was old and outdated.", "translation": "その電話ボックスは古く時代遅れでした。"},
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
