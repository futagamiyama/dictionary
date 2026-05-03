#!/usr/bin/env python3
"""Generate example sentences for words ranked 4670-4689"""

from supabase import create_client, Client

# Supabase credentials
url = "https://tvklrujikuanxdddyfcx.supabase.co"
key = "sb_publishable_DLHimQA_Wyt18fOtUH-o3w_1_BGYb0t"
supabase: Client = create_client(url, key)

# Words data
words_data = [
    {"id": "0a64fc1c-eb3d-44bf-821f-15d1a13774fc", "word": "Scandinavia", "rank": 4670},
    {"id": "afecb47b-6c8b-4e32-a73b-d760f760268f", "word": "coronation", "rank": 4671},
    {"id": "3c59efb3-c26e-49de-943b-0c5d6a20d59d", "word": "heave", "rank": 4672},
    {"id": "4ec8666b-f96a-400e-b7ec-ba5cc9cf8304", "word": "quantum", "rank": 4673},
    {"id": "5be6c244-e3e9-485a-a477-1ecfa9d4c7ec", "word": "mare", "rank": 4674},
    {"id": "c9178814-b34d-4fee-ae2a-d4241539e2be", "word": "omission", "rank": 4675},
    {"id": "4a7e4e64-2569-4f44-b78a-f7c4bf9fa704", "word": "basement", "rank": 4676},
    {"id": "3431e802-e56d-4c53-bb50-ae4b822f0dd6", "word": "dismantle", "rank": 4677},
    {"id": "6f9bc7d6-4f49-487d-8a36-72e24386cd3c", "word": "factual", "rank": 4678},
    {"id": "f5bee502-89c1-4245-8809-2320144d1f6a", "word": "hinder", "rank": 4679},
    {"id": "463bf90b-ede9-4527-b781-83cf579ad663", "word": "soothe", "rank": 4680},
    {"id": "eeff014f-ec86-4521-8002-0681848a64aa", "word": "tweed", "rank": 4681},
    {"id": "e0a51ec6-d13e-4539-9347-b4b4d868480c", "word": "jog", "rank": 4682},
    {"id": "c0fb9e68-edcb-4c5b-8bc5-ee917970a946", "word": "moulding", "rank": 4683},
    {"id": "72e87b85-363b-4edf-aaed-b8f3e9e4684b", "word": "colon", "rank": 4684},
    {"id": "dbbe6165-6427-4702-a3d0-d4eb70966aec", "word": "insolvent", "rank": 4685},
    {"id": "3afaaa18-1f20-46f2-a8c3-6a616a6c4d51", "word": "flip", "rank": 4686},
    {"id": "6d415413-19db-44a1-b690-8f0bf78cd670", "word": "icing", "rank": 4687},
    {"id": "8deadf04-93ad-4f10-90ed-63dbca42d3d4", "word": "crest", "rank": 4688},
    {"id": "68a178fb-6f03-4138-9ef7-0ba67e37b06a", "word": "sever", "rank": 4689},
]

# Example sentences for each word
examples_dict = {
    "Scandinavia": [
        {"sentence": "Scandinavia includes Norway, Sweden, and Denmark.", "translation": "スカンジナビアはノルウェー、スウェーデン、デンマークを含む。"},
        {"sentence": "The countries in Scandinavia are known for high living standards.", "translation": "スカンジナビアの国々は高い生活水準で知られている。"},
        {"sentence": "Many tourists visit Scandinavia to see the Northern Lights.", "translation": "多くの観光客はオーロラを見るためにスカンジナビアを訪問する。"},
    ],
    "coronation": [
        {"sentence": "The coronation ceremony was broadcast to millions worldwide.", "translation": "その戴冠式は世界中の何百万人に放映された。"},
        {"sentence": "She wore a magnificent gown at her coronation.", "translation": "彼女は彼女の戴冠式で壮大なガウンを着ていた。"},
        {"sentence": "The coronation took place in the historic cathedral.", "translation": "その戴冠式は歴史的な大聖堂で行われた。"},
    ],
    "heave": [
        {"sentence": "He heaved a sigh of relief when the test was over.", "translation": "テストが終わったときに、彼は安堵のため息をついた。"},
        {"sentence": "The sailors had to heave the anchor aboard the ship.", "translation": "その船乗りたちは船に錨を持ち上げなければならなかった。"},
        {"sentence": "Her chest began to heave as she cried.", "translation": "彼女が泣いたとき、彼女の胸は波打ち始めた。"},
    ],
    "quantum": [
        {"sentence": "Quantum mechanics explains the behavior of atoms.", "translation": "量子力学は原子の挙動を説明している。"},
        {"sentence": "The quantum leap in technology changed everything.", "translation": "技術の量子的飛躍はすべてを変えた。"},
        {"sentence": "Scientists study quantum particles in the laboratory.", "translation": "科学者たちは実験室で量子粒子を研究している。"},
    ],
    "mare": [
        {"sentence": "The mare gave birth to a healthy foal.", "translation": "その雌馬は健康な子馬を出産した。"},
        {"sentence": "Farmers breed mares for quality horses.", "translation": "農夫たちは良い馬のために雌馬を育種する。"},
        {"sentence": "The dark mare on the moon was visible through the telescope.", "translation": "月の暗い平原は望遠鏡を通して見えた。"},
    ],
    "omission": [
        {"sentence": "The omission of important details made the report incomplete.", "translation": "重要な詳細の省略は報告書を不完全にした。"},
        {"sentence": "His omission of the fact was a serious mistake.", "translation": "彼の事実の脱落は深刻な間違いだった。"},
        {"sentence": "The report contained several omissions that needed correction.", "translation": "その報告書は修正が必要な複数の脱落を含んでいた。"},
    ],
    "basement": [
        {"sentence": "The basement of the building was dark and damp.", "translation": "その建物の地下室は暗くて湿度が高かった。"},
        {"sentence": "She stored old boxes in the basement.", "translation": "彼女は地下室に古いボックスを保管した。"},
        {"sentence": "The basement flooded during the heavy storm.", "translation": "その地下室は大嵐の間に浸水した。"},
    ],
    "dismantle": [
        {"sentence": "They decided to dismantle the old machinery.", "translation": "彼らは古い機械を解体することを決めた。"},
        {"sentence": "Workers had to dismantle the scaffolding after construction.", "translation": "労働者たちは建設後に足場を解体しなければならなかった。"},
        {"sentence": "The government will dismantle the nuclear weapons.", "translation": "政府は核兵器を廃棄するだろう。"},
    ],
    "factual": [
        {"sentence": "The news report should be factual and accurate.", "translation": "そのニュース報告は事実的で正確であるべきである。"},
        {"sentence": "He presented a factual analysis of the situation.", "translation": "彼は状況の事実的分析を提示した。"},
        {"sentence": "Factual errors in the document need to be corrected.", "translation": "ドキュメント内の事実的エラーを修正する必要がある。"},
    ],
    "hinder": [
        {"sentence": "The weather will not hinder our plans.", "translation": "その天気は私たちの計画を妨げません。"},
        {"sentence": "Bad timing hindered her success in the project.", "translation": "悪いタイミングは彼女のプロジェクトでの成功を妨げた。"},
        {"sentence": "Obstacles hindered the progress of the construction.", "translation": "障害物は建設の進行を妨げた。"},
    ],
    "soothe": [
        {"sentence": "The soft music helped soothe her nerves.", "translation": "その柔らかい音楽は彼女の神経をなだめるのに役立った。"},
        {"sentence": "A warm bath can soothe tired muscles.", "translation": "温かいお風呂は疲れた筋肉をなだめることができる。"},
        {"sentence": "She tried to soothe the crying baby.", "translation": "彼女は泣いている赤ちゃんをなだめようとした。"},
    ],
    "tweed": [
        {"sentence": "He wore a tweed jacket to the formal event.", "translation": "彼は正式なイベントにツイードジャケットを着ていた。"},
        {"sentence": "Tweed is a durable fabric popular in Scotland.", "translation": "ツイードはスコットランドで人気のある耐久性のある布地です。"},
        {"sentence": "She bought a tweed coat for the winter.", "translation": "彼女は冬のためにツイードコートを買った。"},
    ],
    "jog": [
        {"sentence": "He jogs in the park every morning.", "translation": "彼は毎朝公園で走る。"},
        {"sentence": "A light jog can help with fitness.", "translation": "軽いジョギングはフィットネスに役立つことができる。"},
        {"sentence": "She jogs her memory with old photographs.", "translation": "彼女は古い写真で彼女の記憶を呼び起こす。"},
    ],
    "moulding": [
        {"sentence": "The decorative moulding around the ceiling was ornate.", "translation": "天井周辺の装飾的なモールディングは華麗だった。"},
        {"sentence": "Plastic moulding is used in modern furniture.", "translation": "プラスチック成形は現代家具で使用されている。"},
        {"sentence": "The artist was skilled at stone moulding.", "translation": "その芸術家は石の形成に熟練していた。"},
    ],
    "colon": [
        {"sentence": "A colon is used to introduce a list or explanation.", "translation": "コロンはリストまたは説明を導入するために使用される。"},
        {"sentence": "The doctor examined her colon during the procedure.", "translation": "その医者は処置中に彼女の結腸を調べた。"},
        {"sentence": "Use a colon before a long quotation.", "translation": "長い引用符の前にコロンを使用してください。"},
    ],
    "insolvent": [
        {"sentence": "The company became insolvent after the economic crisis.", "translation": "その会社は経済危機後に支払い不能になった。"},
        {"sentence": "An insolvent business must declare bankruptcy.", "translation": "支払い不能なビジネスは破産を宣言する必要がある。"},
        {"sentence": "The insolvent debtor could not repay his loans.", "translation": "その支払い不能な債務者は彼のローンを返済できなかった。"},
    ],
    "flip": [
        {"sentence": "He flipped the coin to decide heads or tails.", "translation": "彼は表か裏かを決めるためにコインをはじいた。"},
        {"sentence": "She flipped through the magazine quickly.", "translation": "彼女は素早く雑誌をぱらぱらとめくった。"},
        {"sentence": "The acrobat flipped gracefully in the air.", "translation": "そのアクロバットは空中で優雅に宙返りした。"},
    ],
    "icing": [
        {"sentence": "The cake was decorated with pink icing.", "translation": "そのケーキはピンクの糖衣で装飾されていた。"},
        {"sentence": "Ice buildup and icing are dangerous for aircraft.", "translation": "着氷と氷の蓄積は航空機に危険である。"},
        {"sentence": "She spread the icing evenly on the cupcakes.", "translation": "彼女はカップケーキに糖衣を均等に広げた。"},
    ],
    "crest": [
        {"sentence": "The bird's colorful crest rose when it was excited.", "translation": "その鳥の色彩豊かなとさかは興奮したときに上がった。"},
        {"sentence": "Climbers finally reached the crest of the mountain.", "translation": "登山者たちはついに山頂に到達した。"},
        {"sentence": "The family crest was displayed on the shield.", "translation": "その家紋は盾に表示されていた。"},
    ],
    "sever": [
        {"sentence": "The accident severed the power lines in the area.", "translation": "その事故はその地域の電力線を切断した。"},
        {"sentence": "She decided to sever her relationship with him.", "translation": "彼女は彼との関係を断つことを決めた。"},
        {"sentence": "The two countries severed diplomatic ties.", "translation": "その2つの国は外交関係を断った。"},
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
