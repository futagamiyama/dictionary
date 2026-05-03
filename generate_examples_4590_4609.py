#!/usr/bin/env python3
"""Generate example sentences for words ranked 4590-4609"""

from supabase import create_client, Client

# Supabase credentials
url = "https://tvklrujikuanxdddyfcx.supabase.co"
key = "sb_publishable_DLHimQA_Wyt18fOtUH-o3w_1_BGYb0t"
supabase: Client = create_client(url, key)

# Words data
words_data = [
    {"id": "dc18dbe9-c398-40f7-aaa2-5d4e3de00b97", "word": "blush", "rank": 4590},
    {"id": "4d1d5d6d-2706-48a0-bcd1-9f7934eff8fe", "word": "voucher", "rank": 4591},
    {"id": "a76a5115-16bb-4933-841f-6b45e2502d12", "word": "idiot", "rank": 4592},
    {"id": "d9de6121-1178-4d77-b5e0-12a43fb46319", "word": "fixture", "rank": 4593},
    {"id": "89a0f74d-0c76-4e4d-a74c-2bb13bf64233", "word": "harness", "rank": 4594},
    {"id": "dd01aa91-e1e5-43b1-84cf-77ee15426422", "word": "smuggle", "rank": 4595},
    {"id": "583e7719-ea46-4218-84a0-647098c81368", "word": "fume", "rank": 4596},
    {"id": "b5d7dc07-1c35-4815-9fb7-c654f7a41385", "word": "hack", "rank": 4597},
    {"id": "9447f820-0527-44c3-b89a-54e74db0e899", "word": "brandy", "rank": 4598},
    {"id": "33f15135-7e2c-4eca-b1fb-eeeede4b49c6", "word": "excise", "rank": 4599},
    {"id": "0404eca4-8828-44aa-af33-ac6d2f212d26", "word": "apprehend", "rank": 4600},
    {"id": "57faf60f-5ae0-4942-a68b-3aca39317371", "word": "slash", "rank": 4601},
    {"id": "c329004c-f54a-4702-8845-4eae24790746", "word": "zoo", "rank": 4602},
    {"id": "fa788e5a-103c-400c-b6fa-38611affc971", "word": "lotus", "rank": 4603},
    {"id": "709a4d34-d273-49ce-abfc-1a35a5689caf", "word": "massage", "rank": 4604},
    {"id": "8b5c5e79-a9b1-4477-aa30-c96c173cb6f3", "word": "slaughter", "rank": 4605},
    {"id": "299bf965-33f2-4a1c-b683-eaf2d66d3226", "word": "automate", "rank": 4606},
    {"id": "5daccba6-3c21-44c3-a85d-ab22257370e3", "word": "laden", "rank": 4607},
    {"id": "79febdea-6917-465d-97b7-740b51d8ede4", "word": "lateral", "rank": 4608},
    {"id": "04df9b1f-802c-43d2-9c5b-77cc405c3185", "word": "prose", "rank": 4609},
]

# Example sentences for each word
examples_dict = {
    "blush": [
        {"sentence": "The young woman began to blush when the man complimented her.", "translation": "その若い女性はその男性がその彼女を褒めたときに赤面し始めた。"},
        {"sentence": "He felt a blush rise to his cheeks during the presentation.", "translation": "彼はプレゼンテーション中に頬に赤みが上ったのを感じた。"},
        {"sentence": "She tried not to blush in front of her classmates.", "translation": "彼女はクラスメイトの前で赤面しないようにしようとした。"},
    ],
    "voucher": [
        {"sentence": "The store issued a voucher for the returned merchandise.", "translation": "その店は返品された商品に対する証書を発行した。"},
        {"sentence": "She used a discount voucher to buy the book.", "translation": "彼女は割引証書を使って本を買った。"},
        {"sentence": "The hotel provided a voucher for a free breakfast.", "translation": "そのホテルは無料朝食のための証書を提供した。"},
    ],
    "idiot": [
        {"sentence": "He called himself an idiot for making such a mistake.", "translation": "彼はそのような間違いを犯したために自分自身をばかと呼んだ。"},
        {"sentence": "It was idiot's behavior to drive without a seatbelt.", "translation": "シートベルトなしで運転するのはばかげた行動だった。"},
        {"sentence": "The book criticized the idiot politicians for their decisions.", "translation": "その本はその決定についてばかげた政治家たちを批判した。"},
    ],
    "fixture": [
        {"sentence": "The bathroom fixtures were installed by the contractor.", "translation": "浴室設備は請負業者によってインストールされた。"},
        {"sentence": "The old lamp is a fixture in the living room.", "translation": "その古いランプはリビングルームの付属物だ。"},
        {"sentence": "The basketball game is a fixture of the season schedule.", "translation": "そのバスケットボールゲームはシーズンスケジュールの定番だ。"},
    ],
    "harness": [
        {"sentence": "The farmer harnessed the horses to the plow.", "translation": "その農夫は馬を鋤に着けた。"},
        {"sentence": "They harnessed the power of the wind to generate electricity.", "translation": "彼らは電気を生成するために風の力を利用した。"},
        {"sentence": "A safety harness prevents workers from falling.", "translation": "安全帯は労働者の転落を防ぐ。"},
    ],
    "smuggle": [
        {"sentence": "Customs officers caught the smugglers trying to smuggle diamonds.", "translation": "税関職員はダイヤモンドを密輸しようとしていた密輸業者を捕まえた。"},
        {"sentence": "He tried to smuggle the package into the country illegally.", "translation": "彼は違法にその小包を国に密輸しようとしたした。"},
        {"sentence": "They smuggled the refugees across the border at night.", "translation": "彼らは夜間に難民を国境を越えてこっそり運んだ。"},
    ],
    "fume": [
        {"sentence": "Smoke and fumes came from the factory chimneys.", "translation": "工場の煙突から煙とガスが出ていた。"},
        {"sentence": "He fumed with anger at the unfair decision.", "translation": "彼はその不公正な決定に怒りで燃えていた。"},
        {"sentence": "The chemical fumes were harmful to workers.", "translation": "その化学ガスは労働者に有害だった。"},
    ],
    "hack": [
        {"sentence": "The writer was hired as a hack journalist for the newspaper.", "translation": "その作家は新聞のつまらない記者として雇われた。"},
        {"sentence": "He could hear the child hack as he coughed.", "translation": "彼は子どもが咳をするのが聞こえた。"},
        {"sentence": "The programmer was arrested for trying to hack the system.", "translation": "そのプログラマーはシステムにハッキングしようとしたために逮捕された。"},
    ],
    "brandy": [
        {"sentence": "After dinner, he enjoyed a glass of brandy.", "translation": "食事の後、彼はブランデーのグラスを楽しんだ。"},
        {"sentence": "The restaurant had an excellent selection of brandy.", "translation": "そのレストランは素晴らしいブランデーの選択肢を持っていた。"},
        {"sentence": "She preserved the fruit in brandy for the winter.", "translation": "彼女は冬のためにブランデーで果物を保存した。"},
    ],
    "excise": [
        {"sentence": "The government placed an excise tax on alcohol and tobacco.", "translation": "政府はアルコールとタバコに物品税を課した。"},
        {"sentence": "The surgeon decided to excise the tumor from the patient.", "translation": "その医者は患者から腫瘍を切除することを決めた。"},
        {"sentence": "The editor decided to excise that paragraph from the article.", "translation": "その編集者は記事からその段落を削除することを決めた。"},
    ],
    "apprehend": [
        {"sentence": "The police apprehended the criminal at the airport.", "translation": "警察は空港でその犯人を逮捕した。"},
        {"sentence": "Officers apprehend suspects based on eyewitness descriptions.", "translation": "警察官は目撃者の説明に基づいて容疑者を逮捕する。"},
        {"sentence": "She apprehended the danger and warned everyone.", "translation": "彼女は危険に気づいてみんなに警告した。"},
    ],
    "slash": [
        {"sentence": "He slashed the price of the goods by half.", "translation": "彼は商品の価格を半分削減した。"},
        {"sentence": "The company will slash its workforce by 20 percent.", "translation": "その会社は労働力を20パーセント削減する予定だ。"},
        {"sentence": "The storm slashed trees and damaged buildings.", "translation": "その嵐は木を切り倒し建物に損害を与えた。"},
    ],
    "zoo": [
        {"sentence": "The children were excited to visit the zoo.", "translation": "その子どもたちは動物園を訪問することに興奮していた。"},
        {"sentence": "Many endangered animals are protected in the zoo.", "translation": "多くの絶滅危機に瀕した動物は動物園で保護されている。"},
        {"sentence": "The zoo offers guided tours for visitors.", "translation": "その動物園は訪問者向けのガイド付きツアーを提供している。"},
    ],
    "lotus": [
        {"sentence": "The lotus flower is sacred in many Asian cultures.", "translation": "ハスの花は多くのアジア文化で神聖である。"},
        {"sentence": "She sat in a lotus position during meditation.", "translation": "彼女は瞑想中にハスのポーズに座った。"},
        {"sentence": "The lotus plant grows in shallow water and ponds.", "translation": "ハスの植物は浅い水と池で成長する。"},
    ],
    "massage": [
        {"sentence": "After the workout, she got a massage to relax her muscles.", "translation": "ワークアウトの後、彼女は彼女の筋肉をリラックスするためにマッサージを受けた。"},
        {"sentence": "The massage therapist had many satisfied customers.", "translation": "そのマッサージセラピストは多くの満足した顧客を持っていた。"},
        {"sentence": "He massaged his sore shoulders after the long day.", "translation": "彼は長い一日の後に彼の痛む肩をマッサージした。"},
    ],
    "slaughter": [
        {"sentence": "The factory processes cattle for slaughter.", "translation": "その工場は屠殺のために牛を処理する。"},
        {"sentence": "The war resulted in the slaughter of thousands.", "translation": "その戦争は何千人もの虐殺をもたらした。"},
        {"sentence": "The team was slaughtered in the championship game.", "translation": "そのチームはチャンピオンシップゲームで完敗した。"},
    ],
    "automate": [
        {"sentence": "The company decided to automate its production line.", "translation": "その会社は生産ラインを自動化することを決めた。"},
        {"sentence": "Banks now automate many routine financial transactions.", "translation": "銀行は現在多くの日常的な金融取引を自動化している。"},
        {"sentence": "They automated the system to reduce human error.", "translation": "彼らは人為的エラーを減らすためにシステムを自動化した。"},
    ],
    "laden": [
        {"sentence": "The ship was laden with cargo from the port.", "translation": "その船は港からの貨物を積み込んでいた。"},
        {"sentence": "He carried a laden backpack up the mountain.", "translation": "彼は重い荷物を背負ったバックパックを山まで運んだ。"},
        {"sentence": "The trees were laden with fruit after the harvest.", "translation": "収穫後、木々は果実で満ち溢れていた。"},
    ],
    "lateral": [
        {"sentence": "The lateral movement of the earthquake caused structural damage.", "translation": "地震の横方向の動きは構造的な損害を引き起こした。"},
        {"sentence": "A lateral transfer allowed him to change departments.", "translation": "横方向の転勤により、彼は部門を変更することができた。"},
        {"sentence": "The lateral view shows the complete side profile.", "translation": "その側面図は完全な側面を示している。"},
    ],
    "prose": [
        {"sentence": "The novel is written in clear, engaging prose.", "translation": "その小説は明確で魅力的な散文で書かれている。"},
        {"sentence": "She prefers reading poetry to prose.", "translation": "彼女は散文よりも詩を読むことを好む。"},
        {"sentence": "The author's prose style is distinctive and memorable.", "translation": "その著者の散文スタイルは独特で記憶に残る。"},
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
