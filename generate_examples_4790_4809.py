#!/usr/bin/env python3
"""Generate example sentences for words ranked 4790-4809"""

from supabase import create_client, Client

# Supabase credentials
url = "https://tvklrujikuanxdddyfcx.supabase.co"
key = "sb_publishable_DLHimQA_Wyt18fOtUH-o3w_1_BGYb0t"
supabase: Client = create_client(url, key)

# Words data
words_data = [
    {"id": "ce04ec11-0150-48fc-ae7d-62cda73bf0bf", "word": "scorn", "rank": 4790},
    {"id": "efb597d9-73a0-49fb-85cc-f3d98e0b977b", "word": "paddle", "rank": 4792},
    {"id": "c7050984-f840-406b-bc70-0439a23cc343", "word": "perfume", "rank": 4793},
    {"id": "5a2c7378-9b3d-432d-95f6-71e01715ff32", "word": "purse", "rank": 4794},
    {"id": "67689dda-9576-448a-a0ab-8baefcc889c2", "word": "adjoin", "rank": 4795},
    {"id": "946a948a-2c2b-4c64-958c-86978533c64f", "word": "devolve", "rank": 4796},
    {"id": "a3aec1d4-88f8-48a1-8040-50d29baad3dd", "word": "parson", "rank": 4797},
    {"id": "73b6f31b-7af6-4af1-a7b3-e7a42a264fb2", "word": "collision", "rank": 4798},
    {"id": "9d95f4d8-6e17-4822-86aa-8251a6c7dcb8", "word": "conversely", "rank": 4799},
    {"id": "2318f428-36ef-49bc-a9af-d965af872f17", "word": "coupon", "rank": 4800},
    {"id": "201472b4-32c3-4042-8694-2fd1562abd52", "word": "multinational", "rank": 4801},
    {"id": "3cdedf57-2c45-4aec-898d-6d41683e02ce", "word": "synthetic", "rank": 4802},
    {"id": "e4164f75-debb-4cce-b791-b80c60a5ce55", "word": "robe", "rank": 4803},
    {"id": "f1cea282-80cb-4570-82a5-7778249c1379", "word": "robust", "rank": 4804},
    {"id": "d35830c4-90f2-4731-b8cb-c5e4c6eff6fa", "word": "barrister", "rank": 4805},
    {"id": "ffb53d92-add5-4e1d-843e-3c7174e39c59", "word": "vacancy", "rank": 4807},
    {"id": "9a51d67d-130c-4483-a368-0406b6e23649", "word": "comrade", "rank": 4808},
    {"id": "ad47ddec-c2ee-4ee4-8164-95435a4859eb", "word": "mansion", "rank": 4809},
]

# Example sentences for each word
examples_dict = {
    "scorn": [
        {"sentence": "She showed scorn for his excuses.", "translation": "彼女は彼の言い訳に軽べつを示した。"},
        {"sentence": "The critics treated his work with scorn.", "translation": "評論家たちは彼の作品をさげすんだ。"},
        {"sentence": "He scorned the offer to help.", "translation": "彼は助けるという申し出をはねつけた。"},
    ],
    "paddle": [
        {"sentence": "She used a paddle to row the canoe.", "translation": "彼女はカヌーをこぐためにパドルを使用した。"},
        {"sentence": "The children played with a paddle in the water.", "translation": "その子どもたちは水でパドルで遊んだ。"},
        {"sentence": "Swimmers paddle in shallow water.", "translation": "水泳選手たちは浅瀬をパシャパシャさせて歩く。"},
    ],
    "perfume": [
        {"sentence": "She wore her favorite perfume to the party.", "translation": "彼女はパーティーに彼女のお気に入りの香水を着けていった。"},
        {"sentence": "The garden is filled with the perfume of roses.", "translation": "その庭はバラの香りでいっぱいである。"},
        {"sentence": "The perfume smells wonderful.", "translation": "その香水は素晴らしい香りがする。"},
    ],
    "purse": [
        {"sentence": "She reached into her purse for her keys.", "translation": "彼女は彼女の鍵のためにハンドバッグに手を入れた。"},
        {"sentence": "The purse contained all her important documents.", "translation": "そのハンドバッグは彼女のすべての重要なドキュメントを含んでいた。"},
        {"sentence": "The prize purse for the competition was generous.", "translation": "その競争の賞金は太っぱいものだった。"},
    ],
    "adjoin": [
        {"sentence": "The property adjoins the national park.", "translation": "その財産は国立公園に隣接している。"},
        {"sentence": "Two rooms adjoin each other in the apartment.", "translation": "2つの部屋はアパートで隣り合っている。"},
        {"sentence": "The fields adjoin the river.", "translation": "その畑は川に隣接している。"},
    ],
    "devolve": [
        {"sentence": "The responsibility devolved to the manager.", "translation": "その責任はマネージャーに掛かってきた。"},
        {"sentence": "The task devolves upon the committee.", "translation": "そのタスクは委員会に帰属する。"},
        {"sentence": "Power devolves to local governments.", "translation": "権力は地方政府にゆだねられる。"},
    ],
    "parson": [
        {"sentence": "The parson delivered a sermon to the congregation.", "translation": "その牧師は信者に説教を行った。"},
        {"sentence": "The parson performed the wedding ceremony.", "translation": "その牧師は結婚式を行った。"},
        {"sentence": "The parson lived in the church house.", "translation": "その牧師は教会の家に住んでいた。"},
    ],
    "collision": [
        {"sentence": "The car accident was caused by a collision between two vehicles.", "translation": "その自動車事故は2台の車の衝突によって引き起こされた。"},
        {"sentence": "There was a collision of opinions during the meeting.", "translation": "その会議中に意見の衝突があった。"},
        {"sentence": "The collision happened at the intersection.", "translation": "その衝突は交差点で起きた。"},
    ],
    "conversely": [
        {"sentence": "Some people prefer coffee; conversely, others prefer tea.", "translation": "何人かの人々はコーヒーを好む。逆に、他の人々は紅茶を好む。"},
        {"sentence": "Young people like modern music; conversely, older people prefer classical.", "translation": "若い人々は現代音楽が好きだ。逆に、年配の人々はクラシックを好む。"},
        {"sentence": "This approach is expensive; conversely, it is very effective.", "translation": "このアプローチは高価である。逆に、それは非常に効果的である。"},
    ],
    "coupon": [
        {"sentence": "She used a coupon to get a discount at the store.", "translation": "彼女はその店で割引を受けるためにクーポンを使用した。"},
        {"sentence": "The coupon expires at the end of the month.", "translation": "そのクーポンは月末に期限切れになる。"},
        {"sentence": "Customers can redeem coupons for free products.", "translation": "顧客は無料製品のクーポンを引き換えることができる。"},
    ],
    "multinational": [
        {"sentence": "The multinational company operates in fifty countries.", "translation": "その多国籍企業は50カ国で事業を展開している。"},
        {"sentence": "Multinational corporations have a global presence.", "translation": "多国籍企業はグローバルな存在を持っている。"},
        {"sentence": "The job requires experience with multinational teams.", "translation": "その仕事は多国籍チームの経験を必要とする。"},
    ],
    "synthetic": [
        {"sentence": "The synthetic material is durable and affordable.", "translation": "その合成材料は耐久性があり手頃な価格である。"},
        {"sentence": "Synthetic diamonds are now used in jewelry.", "translation": "人造ダイヤモンドは現在宝飾品で使用されている。"},
        {"sentence": "The synthetic fabric is easy to care for.", "translation": "その合成布は手入れが簡単である。"},
    ],
    "robe": [
        {"sentence": "The judge wore a black robe in court.", "translation": "その裁判官は法廷で黒いローブを着ていた。"},
        {"sentence": "She put on her silk robe after the shower.", "translation": "彼女はシャワーの後にシルクのローブを着た。"},
        {"sentence": "The ceremonial robe was decorated with gold embroidery.", "translation": "その儀式用ローブは金の刺繍で装飾されていた。"},
    ],
    "robust": [
        {"sentence": "The robust economy showed strong growth.", "translation": "その堅調な経済は強い成長を示した。"},
        {"sentence": "He built a robust framework for the project.", "translation": "彼はプロジェクトのための堅牢なフレームワークを構築した。"},
        {"sentence": "The robust health of the athlete impressed everyone.", "translation": "そのアスリートの強壮な健康はみんなを感動させた。"},
    ],
    "barrister": [
        {"sentence": "The barrister presented the case in court.", "translation": "その弁護士は法廷でケースを提示した。"},
        {"sentence": "She hired an experienced barrister for her case.", "translation": "彼女は彼女のケースのために経験豊富な弁護士を雇った。"},
        {"sentence": "The barrister won the trial for his client.", "translation": "その弁護士は彼のクライアントのための裁判に勝った。"},
    ],
    "vacancy": [
        {"sentence": "The hotel has a vacancy for next week.", "translation": "そのホテルは来週のあき部屋がある。"},
        {"sentence": "There is a vacancy in the marketing department.", "translation": "マーケティング部門に空席がある。"},
        {"sentence": "The sign 'No Vacancy' indicated the hotel was full.", "translation": "「満室」という標識はそのホテルが満杯であることを示した。"},
    ],
    "comrade": [
        {"sentence": "He fought alongside his comrades in the war.", "translation": "彼は戦争で彼の仲間と一緒に戦った。"},
        {"sentence": "The soldiers shared food with their comrades.", "translation": "その兵士たちは彼らの仲間と食べ物を共有した。"},
        {"sentence": "His comrade helped him escape from danger.", "translation": "彼の仲間は彼が危険から逃げるのを助けた。"},
    ],
    "mansion": [
        {"sentence": "The wealthy family lived in a grand mansion.", "translation": "その富裕な家族は壮大な大邸宅に住んでいた。"},
        {"sentence": "The mansion had twenty rooms and beautiful gardens.", "translation": "その大邸宅は20の部屋と美しい庭を持っていた。"},
        {"sentence": "The historic mansion was open to the public.", "translation": "その歴史的な大邸宅は一般に開放されていた。"},
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

    print(f"\n📊 Total examples inserted: {total_inserted}/54")

if __name__ == "__main__":
    insert_examples()
