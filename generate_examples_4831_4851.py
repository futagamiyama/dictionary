#!/usr/bin/env python3
"""Generate example sentences for words ranked 4831-4851"""

from supabase import create_client, Client

# Supabase credentials
url = "https://tvklrujikuanxdddyfcx.supabase.co"
key = "sb_publishable_DLHimQA_Wyt18fOtUH-o3w_1_BGYb0t"
supabase: Client = create_client(url, key)

# Words data
words_data = [
    {"id": "6e3f2007-0241-4e61-af67-747431c68404", "word": "automobile", "rank": 4831},
    {"id": "39239ef2-d652-448b-b581-7aa50ab938ca", "word": "temperament", "rank": 4832},
    {"id": "35bb8b4f-9272-43e3-bd75-494495a3f5a3", "word": "accrue", "rank": 4833},
    {"id": "97015d83-3c1d-4bd5-b296-8285b92616db", "word": "reef", "rank": 4835},
    {"id": "6468d945-b15c-4f53-a3ae-e79ece853bca", "word": "advent", "rank": 4836},
    {"id": "c00bddc9-c884-4565-bc18-68bb7325fc94", "word": "lesion", "rank": 4837},
    {"id": "4df89feb-a656-4b02-90ba-92c0496e07d5", "word": "picnic", "rank": 4838},
    {"id": "c112e635-f6b3-483d-bb40-34501b42b3d7", "word": "silicon", "rank": 4839},
    {"id": "a94463ae-2069-4a79-82e7-d2a7145f886c", "word": "thermal", "rank": 4840},
    {"id": "c83afa51-bd9b-4386-a12e-0723c052ec9d", "word": "grit", "rank": 4841},
    {"id": "8d4a0a31-d51f-460e-8d9c-e238f4f1932a", "word": "deviant", "rank": 4842},
    {"id": "fb5c2879-8776-4ef8-b762-2c57ba5f8e43", "word": "diarrhoea", "rank": 4843},
    {"id": "80a45d76-cda2-40ab-a297-9338d2b143ed", "word": "gilt", "rank": 4844},
    {"id": "4ea22548-dfec-4b92-89a9-5833f6ab79af", "word": "surf", "rank": 4845},
    {"id": "342be0d6-ef3d-41ca-b749-1937903aaf04", "word": "thump", "rank": 4846},
    {"id": "aa130704-9648-424c-88f0-f8774c754128", "word": "conquest", "rank": 4847},
    {"id": "a06bae72-9836-4e71-878c-4647d2ba3ab3", "word": "feudal", "rank": 4848},
    {"id": "7c5b4dea-2884-423c-a9f1-eec2a923df9b", "word": "violet", "rank": 4849},
    {"id": "05ecd4e3-9853-4f4a-89a6-b442413e8334", "word": "circus", "rank": 4850},
    {"id": "417c23f6-b1ac-4f00-88a2-93fcbbaef7b9", "word": "mortar", "rank": 4851},
]

# Example sentences for each word
examples_dict = {
    "automobile": [
        {"sentence": "The automobile industry is growing rapidly.", "translation": "自動車産業は急速に成長している。"},
        {"sentence": "He parked his automobile in the garage.", "translation": "彼は彼の自動車をガレージに駐車した。"},
        {"sentence": "Modern automobiles have advanced safety features.", "translation": "現代の自動車は高度な安全機能を備えている。"},
    ],
    "temperament": [
        {"sentence": "She has a calm temperament despite stressful situations.", "translation": "彼女はストレスの多い状況にもかかわらず穏やかな気質を持っている。"},
        {"sentence": "His temperament is suited for leadership.", "translation": "彼の気質はリーダーシップに適している。"},
        {"sentence": "The dog has a friendly temperament.", "translation": "その犬は友好的な気質を持っている。"},
    ],
    "accrue": [
        {"sentence": "Interest will accrue on your savings account.", "translation": "利息はあなたの普通預金口座に計上されるでしょう。"},
        {"sentence": "Unused vacation days accrue each year.", "translation": "未使用の休暇日は毎年計上されます。"},
        {"sentence": "Penalties accrue if you don't pay on time.", "translation": "期限内に支払わないと罰金が課されます。"},
    ],
    "reef": [
        {"sentence": "The coral reef is home to many fish species.", "translation": "サンゴ礁は多くの魚の種の家です。"},
        {"sentence": "Divers explored the colorful reef.", "translation": "ダイバーたちは色彩豊かなサンゴ礁を探索した。"},
        {"sentence": "The reef protects the coast from strong waves.", "translation": "そのサンゴ礁は海岸を強い波から守る。"},
    ],
    "advent": [
        {"sentence": "The advent of technology changed our lives.", "translation": "技術の出現は私たちの人生を変えた。"},
        {"sentence": "The advent of winter brings cold weather.", "translation": "冬の到来は寒い天気をもたらす。"},
        {"sentence": "Since the advent of the internet, communication has been easier.", "translation": "インターネットの出現以来、コミュニケーションはより簡単になっています。"},
    ],
    "lesion": [
        {"sentence": "The doctor examined the lesion on the patient's skin.", "translation": "医者は患者の皮膚の病変を調べた。"},
        {"sentence": "A brain lesion can affect cognitive function.", "translation": "脳の病変は認知機能に影響を与えることができます。"},
        {"sentence": "The lesion has started to heal.", "translation": "その病変は治癒し始めた。"},
    ],
    "picnic": [
        {"sentence": "We had a picnic in the park last Sunday.", "translation": "先週の日曜日、私たちは公園でピクニックをしました。"},
        {"sentence": "The family brought a basket of food for the picnic.", "translation": "家族はピクニックのために食べ物のバスケットを持ってきた。"},
        {"sentence": "It was a perfect day for a picnic.", "translation": "それはピクニックに最適な日でした。"},
    ],
    "silicon": [
        {"sentence": "Silicon is used in computer chips.", "translation": "シリコンはコンピュータチップで使用されます。"},
        {"sentence": "The valley is known for its silicon industry.", "translation": "その谷はシリコン産業で知られている。"},
        {"sentence": "Silicon wafers are essential for electronics.", "translation": "シリコンウェーハは電子機器に不可欠です。"},
    ],
    "thermal": [
        {"sentence": "Thermal imaging helps detect heat sources.", "translation": "サーマルイメージングは熱源の検出を支援する。"},
        {"sentence": "The thermal power plant generates electricity.", "translation": "その火力発電所は電気を生成します。"},
        {"sentence": "Thermal energy can be converted to electricity.", "translation": "熱エネルギーは電気に変換できます。"},
    ],
    "grit": [
        {"sentence": "She showed grit and determination to finish the race.", "translation": "彼女はレースを終わらせるための根性と決意を示した。"},
        {"sentence": "The road was covered with sand and grit.", "translation": "その道路は砂と砂利で覆われていた。"},
        {"sentence": "Success requires hard work and grit.", "translation": "成功には努力と根性が必要です。"},
    ],
    "deviant": [
        {"sentence": "His behavior was considered deviant by society.", "translation": "彼の行動は社会によって逸脱していると考えられていた。"},
        {"sentence": "The deviant path led to problems.", "translation": "その逸脱した道は問題につながった。"},
        {"sentence": "Scientists study deviant cases to understand patterns.", "translation": "科学者たちはパターンを理解するために逸脱したケースを研究する。"},
    ],
    "diarrhoea": [
        {"sentence": "The patient suffered from diarrhoea for three days.", "translation": "患者は3日間下痢に苦しんだ。"},
        {"sentence": "Drinking contaminated water can cause diarrhoea.", "translation": "汚染された水を飲むと下痢を引き起こす可能性があります。"},
        {"sentence": "The doctor prescribed medicine to treat diarrhoea.", "translation": "医者は下痢を治療するための薬を処方した。"},
    ],
    "gilt": [
        {"sentence": "The frame was covered with gilt.", "translation": "そのフレームは金メッキで覆われていた。"},
        {"sentence": "Gilt edges added elegance to the book.", "translation": "金箔の端は本に優雅さを加えた。"},
        {"sentence": "The gilt decorations on the ceiling were beautiful.", "translation": "天井の金メッキの装飾は美しかった。"},
    ],
    "surf": [
        {"sentence": "We went to surf at the beach.", "translation": "私たちはビーチでサーフィンをしに行きました。"},
        {"sentence": "The surfer rode the big waves.", "translation": "そのサーファーは大きな波に乗った。"},
        {"sentence": "Surfing requires skill and balance.", "translation": "サーフィンにはスキルとバランスが必要です。"},
    ],
    "thump": [
        {"sentence": "He heard a loud thump from the next room.", "translation": "彼は隣の部屋から大きなドスンという音を聞いた。"},
        {"sentence": "The box fell with a thump.", "translation": "その箱はドスンと落ちた。"},
        {"sentence": "Her heart began to thump with excitement.", "translation": "彼女の心臓は興奮してドキドキしていた。"},
    ],
    "conquest": [
        {"sentence": "The conquest of the territory took many years.", "translation": "その領土の征服には多くの年がかかりました。"},
        {"sentence": "Napoleon's conquest of Europe is well documented.", "translation": "ナポレオンのヨーロッパ征服は十分に記録されている。"},
        {"sentence": "The conquest of Mount Everest is a great achievement.", "translation": "エベレスト山頂への到達は素晴らしい成就です。"},
    ],
    "feudal": [
        {"sentence": "The feudal system was common in medieval Europe.", "translation": "封建制度は中世ヨーロッパで一般的でした。"},
        {"sentence": "Feudal lords had control over the land.", "translation": "封建領主は土地を支配していた。"},
        {"sentence": "The feudal hierarchy defined social relationships.", "translation": "封建階級制度は社会関係を定義した。"},
    ],
    "violet": [
        {"sentence": "She wore a violet dress to the party.", "translation": "彼女はパーティーに紫色のドレスを着ていった。"},
        {"sentence": "The violet flower has a sweet fragrance.", "translation": "スミレの花は甘い香りを持っている。"},
        {"sentence": "The sunset painted the sky violet.", "translation": "夕焼けは空を紫色に染めた。"},
    ],
    "circus": [
        {"sentence": "The children enjoyed the acrobats at the circus.", "translation": "子どもたちはサーカスの軽業師を楽しんだ。"},
        {"sentence": "The circus featured lions and elephants.", "translation": "そのサーカスはライオンとゾウを特集していた。"},
        {"sentence": "Clowns entertained the audience at the circus.", "translation": "ピエロたちはサーカスで観客を楽しませた。"},
    ],
    "mortar": [
        {"sentence": "Mortar is used to hold bricks together.", "translation": "セメントはレンガを一緒に保つために使用されます。"},
        {"sentence": "The soldiers used mortar to shell the enemy position.", "translation": "兵士たちはモルタルを使用して敵の陣地を砲撃した。"},
        {"sentence": "Mix mortar with water before applying it.", "translation": "それを適用する前に水とセメントを混ぜてください。"},
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
