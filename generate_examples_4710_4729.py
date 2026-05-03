#!/usr/bin/env python3
"""Generate example sentences for words ranked 4710-4729"""

from supabase import create_client, Client

# Supabase credentials
url = "https://tvklrujikuanxdddyfcx.supabase.co"
key = "sb_publishable_DLHimQA_Wyt18fOtUH-o3w_1_BGYb0t"
supabase: Client = create_client(url, key)

# Words data
words_data = [
    {"id": "b8347db9-a81a-4dbf-a643-08c597026d78", "word": "lightning", "rank": 4710},
    {"id": "da0612c9-8f05-4edd-954e-ee16449c0be1", "word": "massacre", "rank": 4711},
    {"id": "45452182-10f2-4b62-a688-b4a113a79639", "word": "pea", "rank": 4712},
    {"id": "1c3015ad-ae29-47a7-9e4a-2bbdff4761ff", "word": "header", "rank": 4713},
    {"id": "fea1980b-dc97-4a9b-a64b-98ef65e806b6", "word": "larva", "rank": 4714},
    {"id": "e4bcf570-af31-403b-915e-e33531a16335", "word": "cop", "rank": 4716},
    {"id": "1db3cb75-8479-4208-9ecd-be3154f4efa8", "word": "vacant", "rank": 4717},
    {"id": "c060a36c-b517-4d74-8208-6beec04f61a0", "word": "syllabus", "rank": 4718},
    {"id": "1e979bb5-519c-49f6-87c5-6f218cc58fe4", "word": "bribe", "rank": 4719},
    {"id": "d361df08-254b-45e7-b475-b4d1f9fb781a", "word": "comb", "rank": 4720},
    {"id": "d0ad7f72-a2a9-4679-8590-03ff9d6dc893", "word": "revert", "rank": 4721},
    {"id": "e2294391-7711-49d1-8406-e29e29b38300", "word": "fake", "rank": 4722},
    {"id": "84a9cc63-a6f3-4b34-ba18-f73681a2e053", "word": "intrude", "rank": 4723},
    {"id": "2245a65e-afb3-4348-b09a-0dc68f76d9a0", "word": "disregard", "rank": 4724},
    {"id": "b5b47cfd-a00b-45d7-a1d1-fc142bbd2f7f", "word": "pest", "rank": 4725},
    {"id": "2438ed07-a0b6-499a-8b72-901367eec0ba", "word": "tack", "rank": 4727},
    {"id": "ed1f92a2-a678-4625-8a4f-dc0bd25a63a0", "word": "aristocrat", "rank": 4728},
    {"id": "e6ce846a-9e40-45fe-b877-885d0d05a55c", "word": "tangible", "rank": 4729},
]

# Example sentences for each word
examples_dict = {
    "lightning": [
        {"sentence": "The lightning struck the tree during the storm.", "translation": "その嵐の間にいなずまが木を襲った。"},
        {"sentence": "Lightning flashed across the dark sky.", "translation": "いなずまは暗い空を横切ってひらめいた。"},
        {"sentence": "The lightning was so bright it lit up the entire town.", "translation": "そのいなずまはとても明るく町全体を照らした。"},
    ],
    "massacre": [
        {"sentence": "The massacre resulted in thousands of casualties.", "translation": "その虐殺は何千人もの死傷者をもたらした。"},
        {"sentence": "Historians documented the horrible massacre.", "translation": "歴史家たちはその恐ろしい虐殺を記録した。"},
        {"sentence": "The government investigated the massacre thoroughly.", "translation": "政府はその虐殺を徹底的に調査した。"},
    ],
    "pea": [
        {"sentence": "The farmer harvested fresh peas from the garden.", "translation": "その農夫は庭から新鮮なエンドウ豆を収穫した。"},
        {"sentence": "Pea soup is a traditional comfort food.", "translation": "エンドウ豆のスープは伝統的なコンフォートフードだ。"},
        {"sentence": "She planted pea seeds in early spring.", "translation": "彼女は早春にエンドウ豆の種を植えた。"},
    ],
    "header": [
        {"sentence": "The soccer player made a powerful header.", "translation": "そのサッカー選手は強力なヘッダーを行った。"},
        {"sentence": "He took a header into the pool.", "translation": "彼はプールに逆さ飛び込みをした。"},
        {"sentence": "The document header contained important information.", "translation": "そのドキュメントヘッダーは重要な情報を含んでいた。"},
    ],
    "larva": [
        {"sentence": "The butterfly larva ate the leaf.", "translation": "その蝶の幼虫は葉を食べた。"},
        {"sentence": "The larva transforms into a pupa.", "translation": "その幼虫はサナギに変わる。"},
        {"sentence": "Scientists study the larva of different insects.", "translation": "科学者たちはさまざまな昆虫の幼虫を研究している。"},
    ],
    "cop": [
        {"sentence": "The cop arrested the suspect.", "translation": "その警官は容疑者を逮捕した。"},
        {"sentence": "She called a cop when she saw the accident.", "translation": "彼女は事故を見たときに警官を呼んだ。"},
        {"sentence": "The cop directed traffic at the intersection.", "translation": "その警官は交差点で交通を指導した。"},
    ],
    "vacant": [
        {"sentence": "The vacant apartment is available for rent.", "translation": "その空いているアパートは賃貸で利用可能である。"},
        {"sentence": "He had a vacant expression on his face.", "translation": "彼の顔に放心した表情があった。"},
        {"sentence": "The vacant position was filled last month.", "translation": "その空席は先月埋められた。"},
    ],
    "syllabus": [
        {"sentence": "The syllabus outlined the course requirements.", "translation": "そのシラバスはコース要件を概説した。"},
        {"sentence": "Students received the syllabus on the first day.", "translation": "学生たちは初日にシラバスを受け取った。"},
        {"sentence": "The syllabus included reading assignments and exams.", "translation": "そのシラバスは読書課題と試験を含んでいた。"},
    ],
    "bribe": [
        {"sentence": "He refused to accept the bribe.", "translation": "彼はわいろを受け入れることを拒否した。"},
        {"sentence": "The official was arrested for taking bribes.", "translation": "その職員はわいろを受け取ったために逮捕された。"},
        {"sentence": "She tried to bribe the guard to let her pass.", "translation": "彼女は彼女を通さすためにガードにわいろを贈ろうとした。"},
    ],
    "comb": [
        {"sentence": "She used a comb to brush her hair.", "translation": "彼女は彼女の髪をとくためにくしを使用した。"},
        {"sentence": "The comb had fine teeth for detangling.", "translation": "そのくしはもつれをほどくための細かい歯を持っていた。"},
        {"sentence": "Police will comb the area for evidence.", "translation": "警察はその地域を証拠のために捜索するだろう。"},
    ],
    "revert": [
        {"sentence": "The system reverted to the previous version.", "translation": "そのシステムは以前のバージョンに戻った。"},
        {"sentence": "After the diet, she reverted to her old eating habits.", "translation": "その食事の後、彼女は彼女の古い食習慣に戻った。"},
        {"sentence": "The property will revert to the state.", "translation": "その財産は州に復帰する。"},
    ],
    "fake": [
        {"sentence": "The painting turned out to be a fake.", "translation": "その絵はにせ物であることが判明した。"},
        {"sentence": "He faked an illness to avoid work.", "translation": "彼は仕事を避けるために病気を装った。"},
        {"sentence": "The document was identified as a fake.", "translation": "そのドキュメントはにせ物として識別された。"},
    ],
    "intrude": [
        {"sentence": "I don't want to intrude on your privacy.", "translation": "私はあなたのプライバシーに侵入したくない。"},
        {"sentence": "The noise intruded on our peaceful evening.", "translation": "その音は私たちの平和な夜をじゃました。"},
        {"sentence": "He intrudes into other people's conversations.", "translation": "彼は他の人たちの会話に侵入する。"},
    ],
    "disregard": [
        {"sentence": "The driver disregarded the speed limit.", "translation": "そのドライバーは制限速度を無視した。"},
        {"sentence": "She showed complete disregard for the rules.", "translation": "彼女はルールに対する完全な無視を示した。"},
        {"sentence": "He disregarded the warning signs.", "translation": "彼は警告標識を無視した。"},
    ],
    "pest": [
        {"sentence": "The pest control service eliminated the insects.", "translation": "害虫駆除サービスは昆虫を排除した。"},
        {"sentence": "That child is a pest to his siblings.", "translation": "その子どもは彼の兄弟姉妹にとってやっかい者だ。"},
        {"sentence": "Mosquitoes are common garden pests.", "translation": "蚊は一般的な庭の害虫だ。"},
    ],
    "tack": [
        {"sentence": "He used a tack to hang the poster on the wall.", "translation": "彼は壁にポスターを掛けるためにびょうを使用した。"},
        {"sentence": "The ship had to tack several times in the wind.", "translation": "その船は風の中で何度も針路を変える必要があった。"},
        {"sentence": "I'll tack on an additional fee for shipping.", "translation": "私は送料の追加料金を付け加えるだろう。"},
    ],
    "aristocrat": [
        {"sentence": "The aristocrat lived in a grand mansion.", "translation": "その貴族は壮大な邸宅に住んでいた。"},
        {"sentence": "Many aristocrats lost their titles after the revolution.", "translation": "多くの貴族は革命後彼らのタイトルを失った。"},
        {"sentence": "She comes from an old aristocrat family.", "translation": "彼女は古い貴族の家から来ている。"},
    ],
    "tangible": [
        {"sentence": "The company achieved tangible results this year.", "translation": "その会社は今年実体のある結果を達成した。"},
        {"sentence": "There is tangible evidence of global warming.", "translation": "地球温暖化の実体のある証拠がある。"},
        {"sentence": "The benefits of the program are tangible and measurable.", "translation": "そのプログラムの利益は実体的で測定可能である。"},
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
