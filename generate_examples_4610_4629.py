#!/usr/bin/env python3
"""Generate example sentences for words ranked 4610-4629"""

from supabase import create_client, Client

# Supabase credentials
url = "https://tvklrujikuanxdddyfcx.supabase.co"
key = "sb_publishable_DLHimQA_Wyt18fOtUH-o3w_1_BGYb0t"
supabase: Client = create_client(url, key)

# Words data
words_data = [
    {"id": "520d496d-d23c-41b7-b35e-33254c574af0", "word": "inordinate", "rank": 4610},
    {"id": "402644cc-98bb-4916-849e-5fd3dab2eff5", "word": "anomaly", "rank": 4611},
    {"id": "3f96f183-639d-491c-bc05-43b0a7d540d3", "word": "prototype", "rank": 4612},
    {"id": "7a87fca8-1a8b-4e30-bf4b-79612b94b06b", "word": "spouse", "rank": 4613},
    {"id": "95c5b96b-23e8-492e-ae23-e6d7419059b8", "word": "scout", "rank": 4614},
    {"id": "73f41b6d-fc7d-4d65-9c5b-1c7206995b1e", "word": "dumb", "rank": 4615},
    {"id": "0b06d848-fbdd-4b23-ac4e-78e8b31db21c", "word": "limp", "rank": 4616},
    {"id": "90d51c57-73cc-4c95-b70a-e80a41bcfb51", "word": "carrot", "rank": 4617},
    {"id": "0c08ad4f-806d-4d25-b427-841d2b996081", "word": "pending", "rank": 4618},
    {"id": "d1ee964c-e7f2-4f3e-8042-804eb0194fd4", "word": "slab", "rank": 4619},
    {"id": "c42471b3-0056-4c36-a44d-0c3b5fa6e024", "word": "withhold", "rank": 4620},
    {"id": "0ec26d3b-9b77-40be-a7a2-1cbb09f2afd3", "word": "trolley", "rank": 4621},
    {"id": "2daf7788-d5ba-463e-927c-4e735a06080f", "word": "assay", "rank": 4622},
    {"id": "d2be8598-479a-40cb-ac08-8c8db494e3fb", "word": "rap", "rank": 4623},
    {"id": "7cf8e1bf-42ab-4064-b4c1-3b1251018d39", "word": "catastrophe", "rank": 4624},
    {"id": "6777713e-2556-4bc3-a1b1-ba068cd80aa1", "word": "handkerchief", "rank": 4625},
    {"id": "b8b62aaf-04c6-48d8-a9cf-49f2562c0517", "word": "overview", "rank": 4626},
    {"id": "bc105a23-5f72-467d-b9a1-6b18a06600b0", "word": "canoe", "rank": 4627},
    {"id": "0ab4e9ab-d046-4683-8da6-b2f0fd0f31f1", "word": "eccentric", "rank": 4628},
    {"id": "2473527f-a20f-474d-8cee-67f378f0446e", "word": "patronage", "rank": 4629},
]

# Example sentences for each word
examples_dict = {
    "inordinate": [
        {"sentence": "He spent an inordinate amount of time on the project.", "translation": "彼はそのプロジェクトに過度な時間を費やした。"},
        {"sentence": "The company charged inordinate fees for the service.", "translation": "その会社はそのサービスに法外な料金を請求した。"},
        {"sentence": "She has an inordinate fondness for chocolate.", "translation": "彼女はチョコレートに対する過度な好みを持っている。"},
    ],
    "anomaly": [
        {"sentence": "The test results showed an anomaly that needed investigation.", "translation": "テスト結果は調査が必要な異常を示した。"},
        {"sentence": "The weather pattern was an anomaly for this season.", "translation": "その天気パターンはこの季節の異常だった。"},
        {"sentence": "Scientists detected an anomaly in the data.", "translation": "科学者たちはデータの異常を検出した。"},
    ],
    "prototype": [
        {"sentence": "The engineer created a prototype of the new machine.", "translation": "その技術者は新しい機械のプロトタイプを作成した。"},
        {"sentence": "This prototype will be tested before production.", "translation": "このプロトタイプは生産前にテストされる。"},
        {"sentence": "The prototype of the car impressed the investors.", "translation": "その車のプロトタイプは投資家を感動させた。"},
    ],
    "spouse": [
        {"sentence": "He introduced his spouse to his colleagues.", "translation": "彼は彼の配偶者を彼の同僚に紹介した。"},
        {"sentence": "Both spouses work in different industries.", "translation": "両方の配偶者は異なる業界で働いている。"},
        {"sentence": "She remained by her spouse's side during the illness.", "translation": "彼女は病気の間、彼女の配偶者のそばにいた。"},
    ],
    "scout": [
        {"sentence": "The scout reported enemy movements to the commander.", "translation": "その斥候は司令官に敵の動きを報告した。"},
        {"sentence": "The talent scout discovered a new singer.", "translation": "その才能スカウトは新しい歌手を発見した。"},
        {"sentence": "Boy scouts helped clean up the park.", "translation": "ボーイスカウトは公園の清掃を助けた。"},
    ],
    "dumb": [
        {"sentence": "The dumb patient could not speak after the surgery.", "translation": "その手術後、口がきけない患者は話すことができなかった。"},
        {"sentence": "He remained dumb about what he had seen.", "translation": "彼は彼が見たことについて黙りのままだった。"},
        {"sentence": "That was a dumb mistake on his part.", "translation": "それは彼の部分での愚かな間違いだった。"},
    ],
    "limp": [
        {"sentence": "He limped into the room after injuring his leg.", "translation": "彼は彼の足に怪我をした後、びっこを引いて部屋に入った。"},
        {"sentence": "The limp was barely noticeable after a few weeks.", "translation": "その跛行は数週間後にはほとんど気づかれなかった。"},
        {"sentence": "The flag hung limp in the still air.", "translation": "その旗は静かな空気の中でぐにゃぐにゃに垂れていた。"},
    ],
    "carrot": [
        {"sentence": "Rabbits love to eat carrots from the garden.", "translation": "ウサギは庭からニンジンを食べるのが好きだ。"},
        {"sentence": "She used a carrot as a tempting reward for the horse.", "translation": "彼女は馬への誘惑的な報酬としてニンジンを使用した。"},
        {"sentence": "Carrots are rich in vitamin A.", "translation": "ニンジンはビタミンAが豊富である。"},
    ],
    "pending": [
        {"sentence": "The decision is pending the approval of the board.", "translation": "その決定は委員会の承認を待っている。"},
        {"sentence": "There are several pending applications for the position.", "translation": "その職位に対して複数の保留中の申請がある。"},
        {"sentence": "The lawsuit is pending in the court.", "translation": "その訴訟は裁判所で保留中である。"},
    ],
    "slab": [
        {"sentence": "The builder laid concrete slabs for the foundation.", "translation": "その建設業者は基礎のためにコンクリート平板を敷いた。"},
        {"sentence": "She cut a thick slab of bread for the sandwich.", "translation": "彼女はサンドイッチのためにパンの厚い平切りを切った。"},
        {"sentence": "The stone slab marked the grave of the ancient king.", "translation": "その石の板は古代の王の墓をマークした。"},
    ],
    "withhold": [
        {"sentence": "The government decided to withhold the report from the public.", "translation": "政府は報告書を一般に与えないことを決めた。"},
        {"sentence": "Tax withholding is automatically deducted from employees' paychecks.", "translation": "税金の源泉徴収は従業員の給与から自動的に控除される。"},
        {"sentence": "She could not withhold her excitement about the news.", "translation": "彼女はそのニュースについて興奮を抑えることができなかった。"},
    ],
    "trolley": [
        {"sentence": "She pushed the trolley through the supermarket.", "translation": "彼女はスーパーマーケットを通じてトロリーを押した。"},
        {"sentence": "The waiter brought the dessert trolley to the table.", "translation": "そのウェイターはデザートワゴンをテーブルに持ってきた。"},
        {"sentence": "The old trolley car still runs on weekends.", "translation": "その古いトロリー車はまだ週末に走っている。"},
    ],
    "assay": [
        {"sentence": "The assay showed the gold content of the ore.", "translation": "その分析は鉱石の金含有量を示した。"},
        {"sentence": "Scientists assayed the water sample for pollution.", "translation": "科学者たちは汚染のために水サンプルを分析した。"},
        {"sentence": "The assay results confirmed the authenticity of the diamond.", "translation": "その分析結果はダイヤモンドの真正性を確認した。"},
    ],
    "rap": [
        {"sentence": "He gave a sharp rap on the door.", "translation": "彼はドアに強くノックした。"},
        {"sentence": "She rapped her knuckles on the table for attention.", "translation": "彼女は注意を引くために彼女の関節をテーブルの上で叩いた。"},
        {"sentence": "The musician started to rap on stage.", "translation": "そのミュージシャンはステージ上でラップを始めた。"},
    ],
    "catastrophe": [
        {"sentence": "The accident was a catastrophe that could have been prevented.", "translation": "その事故は防ぐことができたはずの大災害だった。"},
        {"sentence": "The financial crisis led to a catastrophe for many families.", "translation": "その金融危機は多くの家族にとって大変動につながった。"},
        {"sentence": "The explosion caused a catastrophe in the village.", "translation": "その爆発はその村で大災害を引き起こした。"},
    ],
    "handkerchief": [
        {"sentence": "She pulled out a handkerchief to wipe her tears.", "translation": "彼女は彼女の涙をぬぐうためにハンカチを引き出した。"},
        {"sentence": "The handkerchief was embroidered with initials.", "translation": "そのハンカチはイニシャルが刺繍されていた。"},
        {"sentence": "He always carries a clean handkerchief in his pocket.", "translation": "彼はいつもポケットにきれいなハンカチを持ち歩いている。"},
    ],
    "overview": [
        {"sentence": "The report provided an overview of the company's performance.", "translation": "その報告書は会社の業績の概観を提供した。"},
        {"sentence": "This chapter gives an overview of the main topics.", "translation": "この章は主なトピックの概観を示している。"},
        {"sentence": "From the hilltop, we had a good overview of the valley.", "translation": "丘の上から、私たちは谷の良い眺めを持っていた。"},
    ],
    "canoe": [
        {"sentence": "They paddled the canoe across the calm lake.", "translation": "彼らは穏やかな湖を横切ってカヌーを漕いだ。"},
        {"sentence": "The native people used canoes for fishing and transportation.", "translation": "その先住民はカヌーを釣りと輸送に使用していた。"},
        {"sentence": "He learned to canoe during summer camp.", "translation": "彼は夏のキャンプ中にカヌーを学んだ。"},
    ],
    "eccentric": [
        {"sentence": "His eccentric behavior made him stand out in the group.", "translation": "彼の風変わりな行動はグループで目立つようにした。"},
        {"sentence": "The old professor was known for his eccentric personality.", "translation": "その老教授は彼の風変わりな性格で知られていた。"},
        {"sentence": "She wore eccentric fashion choices that surprised everyone.", "translation": "彼女はみんなを驚かせた風変わりなファッション選択を着ていた。"},
    ],
    "patronage": [
        {"sentence": "The artist survived through the patronage of wealthy sponsors.", "translation": "その芸術家は裕福なスポンサーの後援を通じて生き残った。"},
        {"sentence": "The business relies on the patronage of loyal customers.", "translation": "そのビジネスは忠実な顧客の後援に依存している。"},
        {"sentence": "The church received patronage from the royal family.", "translation": "その教会は王族からの後援を受けた。"},
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
