#!/usr/bin/env python3
"""Generate example sentences for words ranked 5017-5036"""

from supabase import create_client, Client

# Supabase credentials
url = "https://tvklrujikuanxdddyfcx.supabase.co"
key = "sb_publishable_DLHimQA_Wyt18fOtUH-o3w_1_BGYb0t"
supabase: Client = create_client(url, key)

# Words data
words_data = [
    {"id": "f1f0b2e0-b1c1-4cb4-945d-d0828712c8ca", "word": "annex", "rank": 5017},
    {"id": "c01c7d66-2767-4bf9-95c3-d7bdafe3c67a", "word": "invert", "rank": 5018},
    {"id": "0173c845-ff03-4e05-a02e-c0faff911443", "word": "maternal", "rank": 5019},
    {"id": "d0617f30-8e8f-4e37-8806-1d9a497d085c", "word": "therapeutic", "rank": 5020},
    {"id": "4710fd39-265e-49dd-9fc7-ba52807e3ac4", "word": "bungalow", "rank": 5021},
    {"id": "f452c79d-ecb2-4f24-991e-3dbd7a50154a", "word": "peck", "rank": 5022},
    {"id": "7f125b32-c267-474b-a6e2-2ba71892aa16", "word": "fungus", "rank": 5023},
    {"id": "13c351ec-ca58-4002-813e-c04ea3b09591", "word": "pyramid", "rank": 5024},
    {"id": "87891073-5ea1-47b0-a295-dae2bade2fab", "word": "escalate", "rank": 5025},
    {"id": "e4665771-0dd7-496c-88f1-0a2e8b97e942", "word": "scoop", "rank": 5026},
    {"id": "bc3e8264-acb7-4c11-865a-b7293f25392f", "word": "degenerate", "rank": 5027},
    {"id": "074aa602-c66e-41be-ab01-84afe865ab27", "word": "hymn", "rank": 5028},
    {"id": "aa7eee41-f670-4444-95e4-ec8d0d290ef8", "word": "rhyme", "rank": 5029},
    {"id": "b78de949-f903-4718-97ed-f217d82294d2", "word": "anguish", "rank": 5030},
    {"id": "5ad70599-86e1-4155-ad62-d6b3a583f4ee", "word": "tenure", "rank": 5031},
    {"id": "e8ab6210-2a21-43fa-a818-6c3e7a43f57e", "word": "mend", "rank": 5032},
    {"id": "cbcacdc2-484a-4ac6-8ebc-fae802dce2e3", "word": "partition", "rank": 5033},
    {"id": "46b3787b-34b2-41d5-b087-64a7ce4c8842", "word": "radar", "rank": 5034},
    {"id": "0b277a36-0362-4de0-ab79-164070309e83", "word": "notwithstanding", "rank": 5035},
    {"id": "90121908-b518-4641-889f-0db99307fdb6", "word": "estuary", "rank": 5036},
]

# Example sentences for each word
examples_dict = {
    "annex": [
        {"sentence": "The country decided to annex the territory.", "translation": "その国はその領土を併合することに決めました。"},
        {"sentence": "An annex was added to the building.", "translation": "その建物に附属棟が追加されました。"},
        {"sentence": "The annex contains additional office space.", "translation": "その附属棟には追加のオフィススペースが含まれています。"},
    ],
    "invert": [
        {"sentence": "Invert the image to see it differently.", "translation": "イメージを反転させて異なる見方をしてください。"},
        {"sentence": "She inverted the vase to clean it.", "translation": "彼女はそれをきれいにするために花瓶を反転させました。"},
        {"sentence": "The instructions say to invert the mixture.", "translation": "その指示は混合物を反転させることを述べています。"},
    ],
    "maternal": [
        {"sentence": "Her maternal instincts were strong.", "translation": "彼女の母性本能は強かった。"},
        {"sentence": "The maternal bond between mother and child.", "translation": "母と子の間の母性の絆。"},
        {"sentence": "Maternal care is important for infants.", "translation": "母親のケアは乳幼児にとって重要です。"},
    ],
    "therapeutic": [
        {"sentence": "Swimming is therapeutic for many people.", "translation": "水泳は多くの人々にとって治療的です。"},
        {"sentence": "The therapeutic benefits of exercise are well-known.", "translation": "運動の治療的利益は周知の事実です。"},
        {"sentence": "She used music as a therapeutic tool.", "translation": "彼女は音楽を治療的なツールとして使用しました。"},
    ],
    "bungalow": [
        {"sentence": "They bought a small bungalow near the beach.", "translation": "彼らはビーチの近くの小さなバンガローを購入しました。"},
        {"sentence": "The bungalow has three bedrooms.", "translation": "そのバンガローは3つの寝室を持っています。"},
        {"sentence": "The bungalow was surrounded by gardens.", "translation": "そのバンガローは庭に囲まれていました。"},
    ],
    "peck": [
        {"sentence": "The bird began to peck at the seeds.", "translation": "その鳥は種をつつき始めました。"},
        {"sentence": "She gave him a peck on the cheek.", "translation": "彼女は彼の頬に軽いキスをしました。"},
        {"sentence": "The pecking order of the chickens was clear.", "translation": "その鶏のつつく順序は明確でした。"},
    ],
    "fungus": [
        {"sentence": "Fungus grew on the damp wall.", "translation": "湿った壁にキノコが育ちました。"},
        {"sentence": "The fungal infection required treatment.", "translation": "そのキノコの感染には治療が必要でした。"},
        {"sentence": "Various fungi live in the forest.", "translation": "様々なキノコが森に住んでいます。"},
    ],
    "pyramid": [
        {"sentence": "The Egyptian pyramids are ancient wonders.", "translation": "エジプトのピラミッドは古代の不思議です。"},
        {"sentence": "A pyramid has a square base.", "translation": "ピラミッドは四角形のベースを持っています。"},
        {"sentence": "The pyramid scheme was illegal.", "translation": "そのピラミッド構造は違法でした。"},
    ],
    "escalate": [
        {"sentence": "The conflict began to escalate.", "translation": "その紛争は増加し始めました。"},
        {"sentence": "Do not escalate the situation further.", "translation": "状況をこれ以上エスカレートしないでください。"},
        {"sentence": "Prices continued to escalate.", "translation": "価格は引き続き上昇しました。"},
    ],
    "scoop": [
        {"sentence": "The reporter got the scoop on the story.", "translation": "そのレポーターは物語のスクープを得ました。"},
        {"sentence": "Use a scoop to measure the flour.", "translation": "小麦粉を測定するためにスクープを使用してください。"},
        {"sentence": "He scooped the ice cream into a bowl.", "translation": "彼はアイスクリームをボウルにすくいました。"},
    ],
    "degenerate": [
        {"sentence": "The situation began to degenerate.", "translation": "その状況は悪化し始めました。"},
        {"sentence": "Degenerate behavior was not tolerated.", "translation": "その堕落した行動は容認されませんでした。"},
        {"sentence": "The area seemed to degenerate over time.", "translation": "その地域は時間とともに悪化するようでした。"},
    ],
    "hymn": [
        {"sentence": "The choir sang a beautiful hymn.", "translation": "そのコーラスは美しい讃美歌を歌いました。"},
        {"sentence": "Hymns are sung in church services.", "translation": "讃美歌は教会の礼拝で歌われます。"},
        {"sentence": "The hymn was written centuries ago.", "translation": "その讃美歌は数百年前に書かれました。"},
    ],
    "rhyme": [
        {"sentence": "The poem uses rhyme and rhythm.", "translation": "その詩は韻と韻律を使用しています。"},
        {"sentence": "Does 'cat' rhyme with 'bat'?", "translation": "「cat」は「bat」と韻を踏んでいますか？"},
        {"sentence": "She composed a rhyming verse.", "translation": "彼女は韻を踏んだ詩句を作成しました。"},
    ],
    "anguish": [
        {"sentence": "She felt deep anguish over the loss.", "translation": "彼女は喪失に対する深い苦しみを感じました。"},
        {"sentence": "The anguish was visible on his face.", "translation": "その苦しみは彼の顔に見えました。"},
        {"sentence": "He writhed in anguish.", "translation": "彼は苦しみでのたうち回りました。"},
    ],
    "tenure": [
        {"sentence": "His tenure as president lasted ten years.", "translation": "彼の大統領としての任期は10年続きました。"},
        {"sentence": "She achieved tenure at the university.", "translation": "彼女は大学で終身在職権を達成しました。"},
        {"sentence": "During his tenure, many reforms were made.", "translation": "彼の任期中に多くの改革が行われました。"},
    ],
    "mend": [
        {"sentence": "I need to mend the torn shirt.", "translation": "破れたシャツを修理する必要があります。"},
        {"sentence": "Time will mend the broken relationship.", "translation": "時間が破損した関係を修復するでしょう。"},
        {"sentence": "She mended the fence in the garden.", "translation": "彼女は庭の塀を修理しました。"},
    ],
    "partition": [
        {"sentence": "A partition divides the room into two spaces.", "translation": "仕切りは部屋を2つのスペースに分割します。"},
        {"sentence": "The partition of India occurred in 1947.", "translation": "インドの分割は1947年に発生しました。"},
        {"sentence": "They erected a partition to separate areas.", "translation": "彼らはエリアを分離するために仕切りを立てました。"},
    ],
    "radar": [
        {"sentence": "The airport uses radar to track planes.", "translation": "その空港はレーダーを使用して飛行機を追跡しています。"},
        {"sentence": "Radar technology has improved significantly.", "translation": "レーダー技術は大幅に改善されました。"},
        {"sentence": "The ship detected another vessel on radar.", "translation": "その船はレーダーで別の船を検出しました。"},
    ],
    "notwithstanding": [
        {"sentence": "Notwithstanding the difficulties, they succeeded.", "translation": "困難にもかかわらず、彼らは成功しました。"},
        {"sentence": "Notwithstanding the cost, it's worth buying.", "translation": "コストにもかかわらず、購入する価値があります。"},
        {"sentence": "Notwithstanding her youth, she was wise.", "translation": "彼女の若さにもかかわらず、彼女は賢かった。"},
    ],
    "estuary": [
        {"sentence": "The estuary is where the river meets the sea.", "translation": "その河口は川が海と出会う場所です。"},
        {"sentence": "Many fish breed in the estuary.", "translation": "多くの魚が河口で繁殖します。"},
        {"sentence": "The estuary ecosystem is diverse.", "translation": "その河口の生態系は多様です。"},
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
