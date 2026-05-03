#!/usr/bin/env python3
"""Generate example sentences for words ranked 4630-4649"""

from supabase import create_client, Client

# Supabase credentials
url = "https://tvklrujikuanxdddyfcx.supabase.co"
key = "sb_publishable_DLHimQA_Wyt18fOtUH-o3w_1_BGYb0t"
supabase: Client = create_client(url, key)

# Words data
words_data = [
    {"id": "0e9d4be3-71db-4661-8e9f-188d3c9f15fb", "word": "hostel", "rank": 4630},
    {"id": "cf1caa4d-88e2-4353-8738-90034238fcf5", "word": "ecological", "rank": 4631},
    {"id": "c2fa599b-547c-460b-a21c-e59c80b8feac", "word": "cellar", "rank": 4632},
    {"id": "6c4f15ec-ca28-451f-a7f1-4e6bef844829", "word": "pal", "rank": 4633},
    {"id": "24ab0c3f-03a4-4370-a0da-ea8cea2f81c4", "word": "surgical", "rank": 4634},
    {"id": "98874347-97fc-41ea-a340-6312dd2888cf", "word": "diversify", "rank": 4635},
    {"id": "6b5a2de4-cee2-450c-b0ed-cc23b079c94f", "word": "underwrite", "rank": 4636},
    {"id": "9656a6f8-ad0a-4a00-bd4e-bb8d775a27db", "word": "denounce", "rank": 4637},
    {"id": "6de7dab7-00d6-4f40-a3df-fbb4efb8cc9a", "word": "petty", "rank": 4638},
    {"id": "ac659797-b708-4d9b-b22a-03385907a913", "word": "transcend", "rank": 4639},
    {"id": "4acebbd2-8342-438b-b1d1-e03e40234441", "word": "diverge", "rank": 4640},
    {"id": "a20920e6-c21a-4200-a820-372244063365", "word": "lag", "rank": 4641},
    {"id": "388ca4d1-3f60-4e3b-975a-40de563bc5ea", "word": "optimal", "rank": 4642},
    {"id": "815da74a-3233-45ed-bbb1-e6db13b5dfe1", "word": "denote", "rank": 4643},
    {"id": "6555ea93-7b7f-4e61-b80e-10eb5108eb90", "word": "retention", "rank": 4644},
    {"id": "a4de9a46-4993-4e9d-9751-ab6c3f5677c4", "word": "sterile", "rank": 4645},
    {"id": "1285bfe4-9940-45e6-ab99-1bc3765b9a31", "word": "invalid", "rank": 4646},
    {"id": "20ae4939-f4dc-455e-ade4-02d4b4952756", "word": "banner", "rank": 4647},
    {"id": "cd01329b-75b7-4ee0-a8d7-d3bb1ebef2da", "word": "chef", "rank": 4648},
    {"id": "6590c3f8-056d-4d52-8550-8375906f2514", "word": "crook", "rank": 4649},
]

# Example sentences for each word
examples_dict = {
    "hostel": [
        {"sentence": "She stayed at a youth hostel during her backpacking trip.", "translation": "彼女はバックパッキング旅行中にユースホステルに泊まった。"},
        {"sentence": "The hostel provides affordable accommodation for travelers.", "translation": "そのホステルは旅行者に手頃な宿泊を提供している。"},
        {"sentence": "Many students prefer hostels to hotels because they are cheaper.", "translation": "多くの学生はホテルよりもホステルを好む理由はそれらがより安いからである。"},
    ],
    "ecological": [
        {"sentence": "The ecological system of the forest depends on biodiversity.", "translation": "森の生態系は生物多様性に依存している。"},
        {"sentence": "Climate change has ecological impacts on wildlife.", "translation": "気候変動は野生動物に生態学的な影響を与えている。"},
        {"sentence": "The organization focuses on ecological preservation.", "translation": "その組織は生態学的保全に焦点を当てている。"},
    ],
    "cellar": [
        {"sentence": "The wine was stored in the cellar for many years.", "translation": "そのワインは多くの年の間、地下室に保管された。"},
        {"sentence": "They discovered an old cellar beneath the house.", "translation": "彼らは家の下に古い地下室を発見した。"},
        {"sentence": "The cellar was dark and cool, perfect for storage.", "translation": "その地下室は暗くて涼しく、保管に最適だった。"},
    ],
    "pal": [
        {"sentence": "He and his best pal had been friends since childhood.", "translation": "彼と彼の親友は子供の頃からの友人だった。"},
        {"sentence": "She palled around with her classmates after school.", "translation": "彼女は放課後、彼女のクラスメイトと仲良くなった。"},
        {"sentence": "My pal invited me to his birthday party.", "translation": "私の友人は私を彼の誕生日パーティーに招待した。"},
    ],
    "surgical": [
        {"sentence": "The surgeon prepared for the surgical procedure.", "translation": "その外科医は手術の準備をしていた。"},
        {"sentence": "She wore surgical gloves during the operation.", "translation": "彼女は手術中に外科用手袋を着けていた。"},
        {"sentence": "Surgical instruments were sterilized before use.", "translation": "外科器具は使用前に滅菌された。"},
    ],
    "diversify": [
        {"sentence": "The company decided to diversify its product line.", "translation": "その会社は製品ラインを多様化することを決めた。"},
        {"sentence": "Investors should diversify their portfolio to reduce risk.", "translation": "投資家はリスクを減らすためにポートフォリオを多様化すべきである。"},
        {"sentence": "The farmer diversified his crops to improve profit.", "translation": "その農夫は利益を改善するために彼の作物を多様化した。"},
    ],
    "underwrite": [
        {"sentence": "The insurance company will underwrite the policy.", "translation": "その保険会社はその保険証書を引き受ける。"},
        {"sentence": "Banks underwrite mortgages for home buyers.", "translation": "銀行は住宅購入者のための抵当権を引き受ける。"},
        {"sentence": "The government underwrite the cost of the project.", "translation": "政府はそのプロジェクトの費用を引き受ける。"},
    ],
    "denounce": [
        {"sentence": "The activist denounced the government's policies.", "translation": "その活動家は政府の政策を非難した。"},
        {"sentence": "She was denounced for her controversial statements.", "translation": "彼女は彼女の物議を醸す声明のために非難された。"},
        {"sentence": "The country denounced the trade agreement.", "translation": "その国は貿易協定を廃棄宣言した。"},
    ],
    "petty": [
        {"sentence": "Don't argue over petty disagreements.", "translation": "取るに足らない不一致について議論しないでください。"},
        {"sentence": "He was arrested for petty theft.", "translation": "彼は軽微な窃盗で逮捕された。"},
        {"sentence": "Her petty behavior annoyed everyone in the office.", "translation": "彼女の狭量な行動はオフィスのみんなをいらいらさせた。"},
    ],
    "transcend": [
        {"sentence": "The artist's work transcends cultural boundaries.", "translation": "その芸術家の作品は文化的境界を超越している。"},
        {"sentence": "His talent transcends his age.", "translation": "彼の才能は彼の年齢をしのぐ。"},
        {"sentence": "Love transcends all obstacles.", "translation": "愛はすべての障害を超越している。"},
    ],
    "diverge": [
        {"sentence": "The two paths diverge at the intersection.", "translation": "その2つの道は交差点で分岐する。"},
        {"sentence": "Their opinions began to diverge on the issue.", "translation": "その問題について彼らの見解は分かれ始めた。"},
        {"sentence": "The river diverges into two branches.", "translation": "その川は2つの枝に分かれている。"},
    ],
    "lag": [
        {"sentence": "The company's sales lag behind its competitors.", "translation": "その会社の販売は競合他社に遅れている。"},
        {"sentence": "There is a lag between the question and the answer.", "translation": "質問と答えの間に遅延がある。"},
        {"sentence": "The old computer tends to lag when running multiple programs.", "translation": "その古いコンピュータは複数のプログラムを実行するときに遅れることがある。"},
    ],
    "optimal": [
        {"sentence": "The optimal temperature for storage is 25 degrees.", "translation": "保管の最適温度は25度である。"},
        {"sentence": "We need to find the optimal solution to this problem.", "translation": "この問題への最適な解決策を見つける必要がある。"},
        {"sentence": "The optimal time to plant seeds is in spring.", "translation": "種を植える最適な時期は春である。"},
    ],
    "denote": [
        {"sentence": "The red color denotes danger in traffic signals.", "translation": "赤い色は交通信号で危険を示す。"},
        {"sentence": "The asterisk denotes a footnote in the document.", "translation": "アスタリスクはドキュメント内の脚注を示す。"},
        {"sentence": "This symbol denotes multiplication in mathematics.", "translation": "このシンボルは数学で乗算を示す。"},
    ],
    "retention": [
        {"sentence": "The company focuses on employee retention.", "translation": "その会社は従業員の保持に焦点を当てている。"},
        {"sentence": "Water retention in soil is important for plants.", "translation": "土壌の保水は植物にとって重要である。"},
        {"sentence": "His retention of information impressed his teachers.", "translation": "彼の情報保持は彼の教師たちを感動させた。"},
    ],
    "sterile": [
        {"sentence": "The surgical environment must be completely sterile.", "translation": "その手術環境は完全に無菌である必要がある。"},
        {"sentence": "Sterile soil cannot support plant growth.", "translation": "不毛の土壌は植物の成長を支えることができない。"},
        {"sentence": "The discussion became sterile and unproductive.", "translation": "その議論はありきたりで非生産的になった。"},
    ],
    "invalid": [
        {"sentence": "An invalid passport cannot be used for travel.", "translation": "法的効力のないパスポートは旅行に使用できない。"},
        {"sentence": "The invalid argument did not convince anyone.", "translation": "その説得力のない議論は誰もを説得しなかった。"},
        {"sentence": "The accident left him as an invalid for months.", "translation": "その事故は彼を数ヶ月の間病人にした。"},
    ],
    "banner": [
        {"sentence": "The banner was hung across the stadium.", "translation": "そのバナーはスタジアムに掛けられた。"},
        {"sentence": "They marched under the banner of freedom.", "translation": "彼らは自由の旗印の下で行進した。"},
        {"sentence": "The newspaper displayed a banner headline.", "translation": "その新聞は全段抜き大見出しを表示した。"},
    ],
    "chef": [
        {"sentence": "The chef prepared a delicious meal for the guests.", "translation": "そのシェフはゲスト向けのおいしい食事を準備した。"},
        {"sentence": "She works as a head chef in a famous restaurant.", "translation": "彼女は有名なレストランの料理長として働いている。"},
        {"sentence": "The chef's special dish was highly praised.", "translation": "そのシェフの特別料理は高く評価された。"},
    ],
    "crook": [
        {"sentence": "The thief is a notorious crook wanted by police.", "translation": "その泥棒は警察に指名手配されている悪名高い詐欺師だ。"},
        {"sentence": "He bent the crook of his arm to support his head.", "translation": "彼は彼の頭をサポートするために彼の腕のかぎ状の部分を曲げた。"},
        {"sentence": "The shepherd used a crook to guide the sheep.", "translation": "その羊飼いは羊を導くためにかぎを使用した。"},
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
