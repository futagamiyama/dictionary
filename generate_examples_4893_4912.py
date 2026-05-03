#!/usr/bin/env python3
"""Generate example sentences for words ranked 4893-4912"""

from supabase import create_client, Client

# Supabase credentials
url = "https://tvklrujikuanxdddyfcx.supabase.co"
key = "sb_publishable_DLHimQA_Wyt18fOtUH-o3w_1_BGYb0t"
supabase: Client = create_client(url, key)

# Words data
words_data = [
    {"id": "2c1e1978-0e7d-495e-8e67-a17bfde0768c", "word": "clench", "rank": 4893},
    {"id": "0c7100bc-613e-4fd4-97bc-ac1374864606", "word": "sorrow", "rank": 4894},
    {"id": "42b91d8d-2e1a-439b-9247-3b64cf3e1bd1", "word": "discontent", "rank": 4895},
    {"id": "27b6b7e5-b79d-4b74-8a16-e1b2f9a32d50", "word": "intolerable", "rank": 4896},
    {"id": "a5a01b43-cbad-4f69-aa90-e422569ce72f", "word": "consign", "rank": 4897},
    {"id": "7c5ea944-8377-480d-a1bf-93cc803b56df", "word": "testimony", "rank": 4898},
    {"id": "322d0a4f-58f6-496b-bf07-eb2186fcdad4", "word": "propel", "rank": 4899},
    {"id": "2dbd7ef3-6eab-421d-a2dc-19be1dbc2495", "word": "faeces", "rank": 4900},
    {"id": "1788f6a9-1e09-4d2a-9914-76cfec6c189c", "word": "trout", "rank": 4901},
    {"id": "07a9f01b-9a4b-4c80-bfbe-22e9e98017a3", "word": "registrar", "rank": 4902},
    {"id": "a4fbef32-774c-4aca-96cf-2a1854a7ce1d", "word": "rein", "rank": 4903},
    {"id": "21716e15-b84e-40b6-b3c0-c6c0cf8aaa6e", "word": "stove", "rank": 4904},
    {"id": "4dcd7f42-62b5-4fe6-91dc-cac40b944307", "word": "surveillance", "rank": 4905},
    {"id": "d6313e12-283e-4bca-90af-d0a8df4d329f", "word": "trio", "rank": 4906},
    {"id": "2e5ee10c-43ba-4b80-b2b2-ecad0e8c49da", "word": "accessory", "rank": 4907},
    {"id": "c5ad8af3-2180-423c-8517-97d9fc9b0f07", "word": "beloved", "rank": 4908},
    {"id": "ffc36bf6-98d5-47e6-ac06-7e79fc147b48", "word": "construe", "rank": 4909},
    {"id": "eb237a12-e764-497b-817c-0374a70e9f74", "word": "dice", "rank": 4910},
    {"id": "27d0495e-245f-4d85-a0ed-e30745bff6e9", "word": "hum", "rank": 4911},
    {"id": "1d6de709-beda-455c-8db0-87a70de77ec5", "word": "warfare", "rank": 4912},
]

# Example sentences for each word
examples_dict = {
    "clench": [
        {"sentence": "He clenched his fist in anger.", "translation": "彼は怒りで拳を握りしめた。"},
        {"sentence": "She clenched her teeth as the dentist worked.", "translation": "歯医者が治療している間、彼女は歯を食いしばった。"},
        {"sentence": "Clench your stomach muscles and hold for ten seconds.", "translation": "腹筋を収縮させて10秒間保ってください。"},
    ],
    "sorrow": [
        {"sentence": "Her face showed deep sorrow.", "translation": "彼女の顔は深い悲しみを示した。"},
        {"sentence": "The family experienced great sorrow after the loss.", "translation": "その家族は喪失後の大きな悲しみを経験した。"},
        {"sentence": "Music can express feelings of sorrow.", "translation": "音楽は悲しみの感情を表現することができます。"},
    ],
    "discontent": [
        {"sentence": "Workers expressed discontent with the new policies.", "translation": "労働者たちは新しい政策に不満を表現した。"},
        {"sentence": "Growing discontent led to strikes.", "translation": "増加する不満はストライキを引き起こした。"},
        {"sentence": "The discontent was evident in the survey results.", "translation": "その不満は調査結果に明らかでした。"},
    ],
    "intolerable": [
        {"sentence": "The heat was intolerable during summer.", "translation": "夏の間、その暑さは耐えられませんでした。"},
        {"sentence": "Such behavior is intolerable in our workplace.", "translation": "そのような行動は私たちの職場で耐えられません。"},
        {"sentence": "The working conditions were intolerable.", "translation": "その労働条件は耐えられませんでした。"},
    ],
    "consign": [
        {"sentence": "The goods were consigned to a warehouse.", "translation": "その商品は倉庫に預けられた。"},
        {"sentence": "He consigned his old furniture to storage.", "translation": "彼は古い家具を倉庫に預けた。"},
        {"sentence": "The package was consigned to the shipping company.", "translation": "そのパッケージは配送会社に預けられた。"},
    ],
    "testimony": [
        {"sentence": "Her testimony was crucial in the trial.", "translation": "彼女の証言は裁判で重要でした。"},
        {"sentence": "The witness provided testimony against the defendant.", "translation": "その目撃者は被告に対する証言を提供した。"},
        {"sentence": "His testimony confirmed the facts of the case.", "translation": "彼の証言は事件の事実を確認した。"},
    ],
    "propel": [
        {"sentence": "The rocket engine propels the spacecraft.", "translation": "ロケットエンジンは宇宙船を推進する。"},
        {"sentence": "Ambition propelled her towards success.", "translation": "野心は彼女を成功に向かって推し進めた。"},
        {"sentence": "The wind propelled the sailboat forward.", "translation": "風は帆船を前に推し進めた。"},
    ],
    "faeces": [
        {"sentence": "Animals leave faeces as they roam.", "translation": "動物は歩き回る時に糞を残します。"},
        {"sentence": "The doctor analyzed faeces samples.", "translation": "医者は糞の見本を分析した。"},
        {"sentence": "Proper disposal of faeces is important for hygiene.", "translation": "糞の適切な処理は衛生のために重要です。"},
    ],
    "trout": [
        {"sentence": "We caught trout in the mountain stream.", "translation": "私たちは山の小川でマスを捕まえた。"},
        {"sentence": "Trout is a popular fish for cooking.", "translation": "マスは調理に人気のある魚です。"},
        {"sentence": "The angler fished for trout all morning.", "translation": "その釣り人は午前中ずっとマスを釣った。"},
    ],
    "registrar": [
        {"sentence": "Contact the registrar to register for classes.", "translation": "クラスに登録するために登録官に連絡してください。"},
        {"sentence": "The registrar handles student records.", "translation": "その登録官は学生記録を処理します。"},
        {"sentence": "The registrar is located in the administration building.", "translation": "その登録官は管理棟にあります。"},
    ],
    "rein": [
        {"sentence": "The horseman held the rein tightly.", "translation": "その馬上の人は手綱をしっかり握った。"},
        {"sentence": "Keep a tight rein on spending.", "translation": "支出をしっかりコントロールしてください。"},
        {"sentence": "The rider loosened the rein slightly.", "translation": "そのライダーは手綱を少し緩めた。"},
    ],
    "stove": [
        {"sentence": "The pot was heating on the stove.", "translation": "鍋はストーブで加熱されていた。"},
        {"sentence": "Be careful of the hot stove.", "translation": "熱いストーブに注意してください。"},
        {"sentence": "She cooked dinner on the electric stove.", "translation": "彼女は電気ストーブで夕食を作った。"},
    ],
    "surveillance": [
        {"sentence": "The building has 24-hour surveillance cameras.", "translation": "その建物には24時間監視カメラがあります。"},
        {"sentence": "Police increased surveillance in the area.", "translation": "警察はその地域の監視を強化した。"},
        {"sentence": "Surveillance footage showed the incident.", "translation": "監視フッテージは事件を示した。"},
    ],
    "trio": [
        {"sentence": "The musical trio performed beautifully.", "translation": "その音楽三重奏団は美しく演奏した。"},
        {"sentence": "The three friends formed an inseparable trio.", "translation": "その3人の友人は切り離せない三重奏団を形成した。"},
        {"sentence": "The jazz trio played at the club.", "translation": "そのジャズトリオはクラブで演奏した。"},
    ],
    "accessory": [
        {"sentence": "A scarf is an accessory that complements the outfit.", "translation": "スカーフは衣装を補完するアクセサリーです。"},
        {"sentence": "She was charged as an accessory to the crime.", "translation": "彼女は犯罪の従犯として起訴された。"},
        {"sentence": "The phone case is a useful accessory.", "translation": "そのスマートフォンケースは便利なアクセサリーです。"},
    ],
    "beloved": [
        {"sentence": "He was beloved by all who knew him.", "translation": "彼を知る誰もが彼を愛していた。"},
        {"sentence": "The beloved teacher retired after 30 years.", "translation": "その愛されている先生は30年後に引退した。"},
        {"sentence": "Her beloved dog was always by her side.", "translation": "彼女の最愛の犬はいつも彼女のそばにいました。"},
    ],
    "construe": [
        {"sentence": "How do you construe these events?", "translation": "これらのイベントをどのように解釈しますか？"},
        {"sentence": "The lawyer construed the contract differently.", "translation": "その弁護士は契約を異なる方法で解釈した。"},
        {"sentence": "This statement can be construed as an apology.", "translation": "この声明は謝罪と解釈することができます。"},
    ],
    "dice": [
        {"sentence": "We rolled the dice to decide the game.", "translation": "私たちはゲームを決めるためにサイコロを振った。"},
        {"sentence": "Dice are used in many board games.", "translation": "サイコロは多くのボードゲームで使用されます。"},
        {"sentence": "She diced the vegetables for the soup.", "translation": "彼女はスープのために野菜をさいころ状に切った。"},
    ],
    "hum": [
        {"sentence": "She hummed a melody while working.", "translation": "彼女は働きながらメロディーをハミングした。"},
        {"sentence": "The refrigerator produced a low hum.", "translation": "その冷蔵庫は低いハミング音を出していた。"},
        {"sentence": "The crowd began to hum the national anthem.", "translation": "その群衆は国歌をハミングし始めた。"},
    ],
    "warfare": [
        {"sentence": "Modern warfare relies on advanced technology.", "translation": "現代の戦争は高度な技術に依存しています。"},
        {"sentence": "The two nations engaged in economic warfare.", "translation": "その2つの国は経済戦争に従事した。"},
        {"sentence": "Medieval warfare was very different from today.", "translation": "中世の戦争は今日と大きく異なっていました。"},
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
