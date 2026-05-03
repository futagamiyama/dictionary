#!/usr/bin/env python3
"""Generate example sentences for words ranked 4730-4749"""

from supabase import create_client, Client

# Supabase credentials
url = "https://tvklrujikuanxdddyfcx.supabase.co"
key = "sb_publishable_DLHimQA_Wyt18fOtUH-o3w_1_BGYb0t"
supabase: Client = create_client(url, key)

# Words data
words_data = [
    {"id": "4e4ed68b-7524-4635-8af7-cab0f1e95a29", "word": "tow", "rank": 4730},
    {"id": "cf6c92d6-56c7-4fe1-8eaf-d77f451416fb", "word": "manifesto", "rank": 4731},
    {"id": "680e6e43-941a-4f26-8b2f-97bb903b3701", "word": "elf", "rank": 4732},
    {"id": "5a9c7137-5b8b-4e49-84ca-fadff946f4d4", "word": "violin", "rank": 4733},
    {"id": "1fccbebf-3ed6-4ddb-a885-e5c592511701", "word": "ecclesiastic", "rank": 4734},
    {"id": "4bcb2a8c-8b02-49e0-9637-21e690051736", "word": "abdomen", "rank": 4735},
    {"id": "25975837-19ea-46c8-b525-275aff7095fc", "word": "oversee", "rank": 4736},
    {"id": "c7d2c16f-5244-4e9b-8093-921645fef064", "word": "lime", "rank": 4737},
    {"id": "17295e17-e267-4c24-bb9f-f9285dbdd2ca", "word": "swamp", "rank": 4738},
    {"id": "5b92d958-2a86-4ab2-a04e-3864281c812f", "word": "allot", "rank": 4739},
    {"id": "5e997668-1b88-475e-b0be-47d3e81239b2", "word": "Oscar", "rank": 4740},
    {"id": "5636583e-e2db-4692-9b39-8a1591699821", "word": "tsar", "rank": 4741},
    {"id": "cef399ca-b279-4d06-a691-bf3afff11610", "word": "aggravate", "rank": 4742},
    {"id": "3c057c40-f299-4461-8701-e40b51c294d2", "word": "clamp", "rank": 4743},
    {"id": "ecdbb918-b788-4fcb-845d-4925f0a261d3", "word": "cosy", "rank": 4744},
    {"id": "6ed9c52c-3ece-4f25-bc0c-f159a5177145", "word": "solitary", "rank": 4745},
    {"id": "fc2e5e7c-aa17-4955-a405-2f3d015c0e1b", "word": "asthma", "rank": 4746},
    {"id": "9895d6e3-86de-49f3-9200-865bb64f18cb", "word": "prudent", "rank": 4747},
    {"id": "101f6c29-13d8-43f0-9ea4-69dde2c8ab32", "word": "bibliography", "rank": 4748},
    {"id": "f0e1167a-6884-4e98-9991-e18402b203e1", "word": "badge", "rank": 4749},
]

# Example sentences for each word
examples_dict = {
    "tow": [
        {"sentence": "The truck had to tow the broken-down car.", "translation": "そのトラックは壊れた車を引っ張らなければならなかった。"},
        {"sentence": "The boat was put in tow by the rescue vessel.", "translation": "そのボートは救助船に引かれた。"},
        {"sentence": "The towing service charged fifty dollars for towing.", "translation": "その牽引サービスは牽引に50ドルを請求した。"},
    ],
    "manifesto": [
        {"sentence": "The political party released a manifesto before the election.", "translation": "その政党は選挙前に宣言書を発表した。"},
        {"sentence": "The manifesto outlined the party's main policies.", "translation": "その宣言書は党の主な政策を概説した。"},
        {"sentence": "She signed the manifesto supporting environmental protection.", "translation": "彼女は環境保護を支援する宣言書に署名した。"},
    ],
    "elf": [
        {"sentence": "In the story, the elf lived in the magical forest.", "translation": "その話では、小妖精は魔法の森に住んでいた。"},
        {"sentence": "The children dressed up as elves for the holiday.", "translation": "その子どもたちはホリデーのために小妖精として仮装した。"},
        {"sentence": "The elf's magic helped the characters complete their quest.", "translation": "その小妖精の魔法はキャラクターが彼らの探求を完了するのを助けた。"},
    ],
    "violin": [
        {"sentence": "She played a beautiful piece on the violin.", "translation": "彼女はバイオリンで美しい曲を演奏した。"},
        {"sentence": "The violin is one of the most expressive instruments.", "translation": "バイオリンは最も表現力のある楽器の一つである。"},
        {"sentence": "He started learning violin at age five.", "translation": "彼は5歳でバイオリンの学習を始めた。"},
    ],
    "ecclesiastic": [
        {"sentence": "The ecclesiastic blessed the congregation.", "translation": "その聖職者は信者を祝福した。"},
        {"sentence": "The ecclesiastic authority approved the ceremony.", "translation": "その教会当局は式典を承認した。"},
        {"sentence": "He became an ecclesiastic after years of study.", "translation": "彼は長年の研究の後、聖職者になった。"},
    ],
    "abdomen": [
        {"sentence": "The doctor examined the patient's abdomen.", "translation": "その医者は患者の腹部を調べた。"},
        {"sentence": "She felt pain in her abdomen.", "translation": "彼女は彼女の腹部に痛みを感じた。"},
        {"sentence": "The insect has a segmented abdomen.", "translation": "その昆虫は分節された腹部を持っている。"},
    ],
    "oversee": [
        {"sentence": "The manager will oversee the project.", "translation": "そのマネージャーはそのプロジェクトを監督する。"},
        {"sentence": "She oversees a team of ten employees.", "translation": "彼女は10人の従業員のチームを監督している。"},
        {"sentence": "The director overseers all production activities.", "translation": "その監督はすべての製作活動を監督している。"},
    ],
    "lime": [
        {"sentence": "Add lime juice to the cocktail.", "translation": "カクテルにライムジュースを追加してください。"},
        {"sentence": "Lime is often used in cooking and baking.", "translation": "ライムはしばしば料理と焼き菓子に使用される。"},
        {"sentence": "The farmers applied lime to the acidic soil.", "translation": "その農夫たちは酸性の土壌に石灰をまいた。"},
    ],
    "swamp": [
        {"sentence": "The alligator lived in the swamp.", "translation": "そのワニは沼地に住んでいた。"},
        {"sentence": "Heavy rain swamped the basement with water.", "translation": "大雨は地下室を水で浸した。"},
        {"sentence": "Too many tasks swamped her during the busy season.", "translation": "多くのタスクは忙しい季節に彼女を圧倒した。"},
    ],
    "allot": [
        {"sentence": "The government allotted funds for the new school.", "translation": "政府は新しい学校に資金を割り当てた。"},
        {"sentence": "Each student is allotted one computer.", "translation": "各学生に1台のコンピュータが割り当てられる。"},
        {"sentence": "The company allotted time for employee training.", "translation": "その会社は従業員訓練のために時間を割り当てた。"},
    ],
    "Oscar": [
        {"sentence": "She won an Oscar for Best Actress.", "translation": "彼女は最優秀女優賞のオスカー賞を獲得した。"},
        {"sentence": "The Oscar ceremony is held every year in February.", "translation": "オスカー式典は毎年2月に開催される。"},
        {"sentence": "Many actors dream of winning an Oscar.", "translation": "多くの俳優はオスカー賞を獲得することを夢見ている。"},
    ],
    "tsar": [
        {"sentence": "The tsar ruled Russia for many years.", "translation": "そのツァーは長年ロシアを統治した。"},
        {"sentence": "The tsar's family was executed during the revolution.", "translation": "そのツァーの家族は革命中に処刑された。"},
        {"sentence": "Peter the Great was a famous tsar.", "translation": "ピョートル大帝は有名なツァーだった。"},
    ],
    "aggravate": [
        {"sentence": "The noise aggravated her headache.", "translation": "その音は彼女の頭痛を悪化させた。"},
        {"sentence": "The situation was aggravated by poor communication.", "translation": "その状況は貧弱なコミュニケーションによって悪化した。"},
        {"sentence": "His behavior aggravates everyone around him.", "translation": "彼の行動はまわりの誰もをいらいらさせる。"},
    ],
    "clamp": [
        {"sentence": "He used a clamp to hold the wood together.", "translation": "彼は木を一緒に保つために万力を使用した。"},
        {"sentence": "The clamp tightened as she turned the handle.", "translation": "彼女がハンドルを回したとき、万力は締まった。"},
        {"sentence": "The mechanic clamped the metal in the vice.", "translation": "その機械工は金属をバイスに締めた。"},
    ],
    "cosy": [
        {"sentence": "The cottage had a cosy atmosphere.", "translation": "そのコテージは居ごこちの良い雰囲気を持っていた。"},
        {"sentence": "The living room was warm and cosy.", "translation": "そのリビングルームは暖かく居ごこちが良かった。"},
        {"sentence": "She used a tea cosy to keep the pot warm.", "translation": "彼女はティーポットを温かく保つために紅茶カバーを使用した。"},
    ],
    "solitary": [
        {"sentence": "He preferred a solitary walk in nature.", "translation": "彼は自然の中で一人の散歩を好んだ。"},
        {"sentence": "The prisoner was kept in solitary confinement.", "translation": "その囚人は独房に閉じ込められていた。"},
        {"sentence": "There was not a solitary person in the street.", "translation": "通りに唯一の人さえもいなかった。"},
    ],
    "asthma": [
        {"sentence": "She uses an inhaler to manage her asthma.", "translation": "彼女は吸入器を使って彼女の喘息を管理している。"},
        {"sentence": "Asthma attacks can be triggered by exercise.", "translation": "喘息発作は運動によって引き起こされることができる。"},
        {"sentence": "Many children suffer from asthma.", "translation": "多くの子どもたちは喘息に苦しんでいる。"},
    ],
    "prudent": [
        {"sentence": "A prudent investor diversifies their portfolio.", "translation": "慎重な投資家はポートフォリオを多様化する。"},
        {"sentence": "It is prudent to save money for emergencies.", "translation": "緊急事態のためにお金を保存することは慎重である。"},
        {"sentence": "The prudent decision was to wait and see.", "translation": "慎重な決定は待って見ることだった。"},
    ],
    "bibliography": [
        {"sentence": "The research paper included a comprehensive bibliography.", "translation": "その研究論文は包括的な参考文献リストを含んでいた。"},
        {"sentence": "Students must cite all sources in the bibliography.", "translation": "学生たちは参考文献リストのすべてのソースを引用する必要がある。"},
        {"sentence": "The bibliography section listed twenty sources.", "translation": "その参考文献セクションには20のソースがリストされた。"},
    ],
    "badge": [
        {"sentence": "The police officer wore a badge on his uniform.", "translation": "その警察官は彼のユニフォームに記章をつけていた。"},
        {"sentence": "Scout members earn badges for their achievements.", "translation": "スカウトメンバーは彼らの成果に対してバッジを獲得する。"},
        {"sentence": "The security guard's badge identified him as an employee.", "translation": "そのセキュリティガードのバッジは彼を従業員として特定した。"},
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
