#!/usr/bin/env python3
"""Generate example sentences for words ranked 4872-4892"""

from supabase import create_client, Client

# Supabase credentials
url = "https://tvklrujikuanxdddyfcx.supabase.co"
key = "sb_publishable_DLHimQA_Wyt18fOtUH-o3w_1_BGYb0t"
supabase: Client = create_client(url, key)

# Words data
words_data = [
    {"id": "f83a8fd0-61da-4b02-a956-764db0d13b81", "word": "practicable", "rank": 4872},
    {"id": "ec37d949-8254-40f0-9f90-a2569d7b1d3b", "word": "deception", "rank": 4873},
    {"id": "58870cb5-8615-48b9-a10f-81bf9de611c7", "word": "reel", "rank": 4874},
    {"id": "2be3e46b-b8f4-4763-a053-1361c198d26b", "word": "sewage", "rank": 4875},
    {"id": "39ddc2a9-8081-4259-9fdf-e783ae0d8fab", "word": "socialise", "rank": 4876},
    {"id": "508cc574-f450-4787-8db0-236d5c64a300", "word": "hound", "rank": 4877},
    {"id": "33b5b042-184c-4c31-9aad-fde724a4b805", "word": "theological", "rank": 4878},
    {"id": "96e460ad-dcae-4e87-a400-2b9198b59419", "word": "ramble", "rank": 4879},
    {"id": "a0331099-9041-448c-989d-340a3a9b3daa", "word": "cholesterol", "rank": 4881},
    {"id": "a4c6b374-2fcc-484e-b7d0-7e2e8ec7701e", "word": "renown", "rank": 4882},
    {"id": "a3c78db6-5eaf-4a7a-b83c-6cf122873686", "word": "dissolution", "rank": 4883},
    {"id": "50d616ea-1825-4dca-bf46-c6f2e4645b32", "word": "cripple", "rank": 4884},
    {"id": "1e42f8bd-382b-4e3e-8a29-e2f75dcab213", "word": "aerospace", "rank": 4885},
    {"id": "d534d583-0cdf-4db7-ae10-e42cb65f960e", "word": "convoy", "rank": 4886},
    {"id": "8fc9b63c-1c33-4dac-a6cf-e6130675dd38", "word": "charitable", "rank": 4887},
    {"id": "f4e5d911-7fa6-4532-84fa-4588910a6d44", "word": "dubious", "rank": 4888},
    {"id": "8b7bfeec-9b28-4fc5-8afc-89dd5d0cdb39", "word": "embroider", "rank": 4889},
    {"id": "6ab3ddd1-a7c8-46f8-96d8-90a6dc37cf1f", "word": "trinity", "rank": 4890},
    {"id": "b83ed4d6-fcf7-4705-9b6f-3266bb01671d", "word": "duodenum", "rank": 4891},
    {"id": "1693ae45-625d-4b55-bc3b-cfd5cca2d808", "word": "assimilate", "rank": 4892},
]

# Example sentences for each word
examples_dict = {
    "practicable": [
        {"sentence": "The plan is practicable and achievable.", "translation": "その計画は実行可能で達成可能です。"},
        {"sentence": "We need a practicable solution to the problem.", "translation": "私たちは問題に対して実行可能な解決策を必要としています。"},
        {"sentence": "Is this approach practicable with current resources?", "translation": "この方法は現在のリソースで実行可能ですか？"},
    ],
    "deception": [
        {"sentence": "The deception was eventually discovered.", "translation": "その詐欺は最終的に発見された。"},
        {"sentence": "He was accused of deception in his business dealings.", "translation": "彼は彼のビジネス取引で詐欺の疑いをかけられた。"},
        {"sentence": "Deception undermines trust in relationships.", "translation": "詐欺は関係の信頼を損なう。"},
    ],
    "reel": [
        {"sentence": "The fishing reel spun as he cast the line.", "translation": "彼が糸を投げると、釣りのリールが回転した。"},
        {"sentence": "She danced a Scottish reel.", "translation": "彼女はスコットランドのリールダンスを踊った。"},
        {"sentence": "The film reel contained old movie footage.", "translation": "そのフィルムリールは古い映画のフッテージを含んでいた。"},
    ],
    "sewage": [
        {"sentence": "The sewage treatment plant processes wastewater.", "translation": "その下水処理場は廃水を処理します。"},
        {"sentence": "Proper sewage disposal is important for public health.", "translation": "適切な下水処理は公衆衛生に重要です。"},
        {"sentence": "The sewage system needs upgrading.", "translation": "その下水システムはアップグレードが必要です。"},
    ],
    "socialise": [
        {"sentence": "They went out to socialise with friends.", "translation": "彼らは友人と付き合うために出かけた。"},
        {"sentence": "Young children need to socialise with peers.", "translation": "小さな子どもたちは同い年の子どもと付き合う必要があります。"},
        {"sentence": "The event allows people to socialise and network.", "translation": "そのイベントは人々が付き合いネットワーキングできるようにします。"},
    ],
    "hound": [
        {"sentence": "The hound chased the rabbit into the woods.", "translation": "その狩犬はウサギを森に追いかけた。"},
        {"sentence": "Reporters hounded the celebrity for interviews.", "translation": "記者たちはその著名人にインタビューのために付きまとった。"},
        {"sentence": "The hound has a keen sense of smell.", "translation": "その狩犬は鋭い嗅覚を持っている。"},
    ],
    "theological": [
        {"sentence": "Theological debates have influenced history.", "translation": "神学的な議論は歴史に影響を与えました。"},
        {"sentence": "He studied theological concepts in seminary.", "translation": "彼は神学校で神学的な概念を研究した。"},
        {"sentence": "The book examines theological implications.", "translation": "その本は神学的な含意を調べます。"},
    ],
    "ramble": [
        {"sentence": "We took a ramble through the countryside.", "translation": "私たちは田舎を散歩しました。"},
        {"sentence": "He began to ramble about his childhood memories.", "translation": "彼は彼の幼少期の思い出について長々と話し始めた。"},
        {"sentence": "The ramble was interrupted by bad weather.", "translation": "その散歩は悪い天気で中断された。"},
    ],
    "cholesterol": [
        {"sentence": "High cholesterol can lead to heart disease.", "translation": "高いコレステロール値は心臓病につながる可能性があります。"},
        {"sentence": "The doctor recommended lowering cholesterol levels.", "translation": "医者はコレステロール値を下げることを勧めた。"},
        {"sentence": "Diet affects cholesterol production in the body.", "translation": "食事は体のコレステロール生成に影響を与えます。"},
    ],
    "renown": [
        {"sentence": "The artist achieved international renown.", "translation": "そのアーティストは国際的な名声を得た。"},
        {"sentence": "She is of great renown in her field.", "translation": "彼女はその分野で大きな名声を持っている。"},
        {"sentence": "His renown spread throughout the region.", "translation": "彼の名声は地域全体に広がった。"},
    ],
    "dissolution": [
        {"sentence": "The dissolution of the company was announced.", "translation": "その企業の解散が発表されました。"},
        {"sentence": "The dissolution of marriage requires legal proceedings.", "translation": "結婚の解散には法的手続きが必要です。"},
        {"sentence": "Political dissolution led to governmental reform.", "translation": "政治的な解散は政府改革につながった。"},
    ],
    "cripple": [
        {"sentence": "The injury may cripple his athletic career.", "translation": "その怪我は彼の運動競技のキャリアを麻痺させるかもしれません。"},
        {"sentence": "Economic sanctions cripple the nation's economy.", "translation": "経済制裁はその国の経済を麻痺させます。"},
        {"sentence": "The disease can cripple mobility.", "translation": "その病気は移動性を麻痺させる可能性があります。"},
    ],
    "aerospace": [
        {"sentence": "The aerospace industry is advancing rapidly.", "translation": "航空宇宙産業は急速に進歩している。"},
        {"sentence": "Aerospace engineers design aircraft and spacecraft.", "translation": "航空宇宙エンジニアは航空機と宇宙船を設計します。"},
        {"sentence": "The company specializes in aerospace technology.", "translation": "その企業は航空宇宙技術を専門としています。"},
    ],
    "convoy": [
        {"sentence": "Military trucks traveled in convoy for protection.", "translation": "軍用トラックは保護のために列をなして移動した。"},
        {"sentence": "The supply convoy arrived safely.", "translation": "その補給列は安全に到着した。"},
        {"sentence": "Ships traveled in convoy during wartime.", "translation": "戦時中、船は列をなして移動した。"},
    ],
    "charitable": [
        {"sentence": "She made a large charitable donation.", "translation": "彼女は大きな慈善寄付をした。"},
        {"sentence": "The organization has charitable status.", "translation": "その組織は慈善ステータスを持っている。"},
        {"sentence": "He is known for his charitable work.", "translation": "彼は彼の慈善活動で知られている。"},
    ],
    "dubious": [
        {"sentence": "The claim seems dubious and unverified.", "translation": "その主張は疑わしく検証されていないようです。"},
        {"sentence": "He gave a dubious explanation for his absence.", "translation": "彼は彼の欠席に対して疑わしい説明を与えた。"},
        {"sentence": "The results are dubious and need further testing.", "translation": "その結果は疑わしく、さらなるテストが必要です。"},
    ],
    "embroider": [
        {"sentence": "She learned to embroider from her grandmother.", "translation": "彼女は祖母から刺繍することを学びました。"},
        {"sentence": "He tends to embroider the truth in his stories.", "translation": "彼は彼の話で真実を大げさに言う傾向があります。"},
        {"sentence": "The artist will embroider the design on the fabric.", "translation": "そのアーティストは生地にデザインを刺繍します。"},
    ],
    "trinity": [
        {"sentence": "The trinity concept appears in various religions.", "translation": "その三位一体の概念は様々な宗教に現れます。"},
        {"sentence": "The holy trinity is central to Christian theology.", "translation": "聖なる三位一体はキリスト教神学の中心です。"},
        {"sentence": "The trinity of values guides our organization.", "translation": "その3つの価値観の組み合わせが私たちの組織を導きます。"},
    ],
    "duodenum": [
        {"sentence": "The duodenum is part of the small intestine.", "translation": "十二指腸は小腸の一部です。"},
        {"sentence": "Food enters the duodenum after leaving the stomach.", "translation": "胃を離れた後、食物は十二指腸に入ります。"},
        {"sentence": "The duodenum has important digestive functions.", "translation": "十二指腸は重要な消化機能を持っています。"},
    ],
    "assimilate": [
        {"sentence": "Immigrants must assimilate into the new culture.", "translation": "移民は新しい文化に同化する必要があります。"},
        {"sentence": "Students assimilate information through study.", "translation": "学生たちは研究を通じて情報を同化します。"},
        {"sentence": "The body assimilates nutrients from food.", "translation": "体は食べ物から栄養を同化させます。"},
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
