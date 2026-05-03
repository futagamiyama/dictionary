#!/usr/bin/env python3
"""Generate example sentences for words ranked 4550-4569"""

import json
from supabase import create_client, Client

# Supabase credentials
url = "https://tvklrujikuanxdddyfcx.supabase.co"
key = "sb_publishable_DLHimQA_Wyt18fOtUH-o3w_1_BGYb0t"
supabase: Client = create_client(url, key)

# Words data - already retrieved
words_data = [
    {"id": "7f5014e3-2bb6-4133-864b-dadc9542d47a", "word": "corpus", "rank": 4550},
    {"id": "a7509f30-27f2-4486-b459-01682cf17fad", "word": "distil", "rank": 4551},
    {"id": "8b1d2651-30b9-4e9c-b160-5b0d4e0cbf03", "word": "commemorate", "rank": 4552},
    {"id": "4ff0de79-7079-4036-91ba-548b786dc80b", "word": "seam", "rank": 4553},
    {"id": "34c299a8-3241-431e-96d1-722dbe0d1c20", "word": "skeleton", "rank": 4554},
    {"id": "ca572ca5-71d4-401f-a345-e464560a39e9", "word": "mama", "rank": 4555},
    {"id": "e09d34d7-df14-4b7c-8fb9-d3c630a869cb", "word": "stray", "rank": 4556},
    {"id": "83e10de7-a0d8-4643-86a3-9f46201e1db8", "word": "refurbish", "rank": 4557},
    {"id": "4315246e-d549-42ef-acb0-e8ee82271515", "word": "chunk", "rank": 4559},
    {"id": "98b7c941-035c-4e33-9c8b-52c86e90e997", "word": "gallon", "rank": 4560},
    {"id": "b891c81c-55c5-4d4e-a2f7-c2138fc5d87c", "word": "boycott", "rank": 4561},
    {"id": "50ad64e7-52cb-44cd-9bc9-0a77a2c1f26d", "word": "fend", "rank": 4562},
    {"id": "bf2d43a2-07e2-4841-abff-14d2594157e3", "word": "convene", "rank": 4564},
    {"id": "d85b2327-f300-4710-bc42-234da07da642", "word": "rim", "rank": 4565},
    {"id": "58129d20-f05c-4a40-ae6d-3d0db92d5bd2", "word": "intercourse", "rank": 4566},
    {"id": "61d4d604-9c91-4eb4-9468-12e613705fd0", "word": "armchair", "rank": 4567},
    {"id": "ae91cb80-4725-401e-8bbc-35446a2fa347", "word": "maxim", "rank": 4568},
    {"id": "bb7ac84c-5b0b-4896-966d-03df2fdef78a", "word": "coroner", "rank": 4569},
]

# Example sentences for each word
examples_dict = {
    "corpus": [
        {"sentence": "The research team analyzed a large corpus of text to understand language patterns.", "translation": "研究チームは言語パターンを理解するために大量のテキスト資料を分析した。"},
        {"sentence": "A corpus of medical records was used to study disease trends.", "translation": "病気の傾向を研究するために医学記録の集成が使用された。"},
        {"sentence": "This corpus contains millions of words from newspapers and books.", "translation": "この資料集には新聞と本から数百万語が含まれている。"},
    ],
    "distil": [
        {"sentence": "The factory distils crude oil into gasoline and other products.", "translation": "その工場は原油をガソリンと他の製品に蒸留する。"},
        {"sentence": "We need to distil the key points from this long report.", "translation": "この長い報告書から重要なポイントを引き出す必要がある。"},
        {"sentence": "Distilled water is used in many scientific experiments.", "translation": "蒸留水は多くの科学実験で使用される。"},
    ],
    "commemorate": [
        {"sentence": "The city will commemorate the founding day with a festival.", "translation": "その都市は創設記念日を祭りで祝う予定だ。"},
        {"sentence": "A statue was built to commemorate the famous leader.", "translation": "有名な指導者を記念するために像が建てられた。"},
        {"sentence": "The book commemorates the lives of soldiers who died in the war.", "translation": "その本は戦争で亡くなった兵士たちの人生を記念している。"},
    ],
    "seam": [
        {"sentence": "The seam of the shirt came apart after washing.", "translation": "シャツの縫い目は洗濯後に破れた。"},
        {"sentence": "Coal miners work deep underground to find seams of coal.", "translation": "炭鉱労働者は石炭の層を見つけるために深い地下で働く。"},
        {"sentence": "There are visible seams in the stone wall where two pieces meet.", "translation": "2つの石が合わさる場所に目に見える継ぎ目がある。"},
    ],
    "skeleton": [
        {"sentence": "The museum displays the skeleton of a dinosaur.", "translation": "博物館は恐竜の骨格を展示している。"},
        {"sentence": "The building's skeleton was completed before the walls were added.", "translation": "建物の骨組みは壁が追加される前に完成した。"},
        {"sentence": "The skeleton of the novel was based on a true story.", "translation": "その小説の骨子は実話に基づいていた。"},
    ],
    "mama": [
        {"sentence": "The little child called out 'Mama!' when she got lost.", "translation": "小さな子どもが迷ったときに『ママ！』と叫んだ。"},
        {"sentence": "Mama bear protects her cubs from danger.", "translation": "ママ熊は危険から子グマを守る。"},
        {"sentence": "My mama always gives me good advice.", "translation": "私のママはいつも良いアドバイスをくれる。"},
    ],
    "stray": [
        {"sentence": "The stray dog was hungry and looked for food.", "translation": "野良犬は空腹で食べ物を探していた。"},
        {"sentence": "Don't let your attention stray from the important task.", "translation": "重要な仕事から注意をそらしてはいけない。"},
        {"sentence": "A few stray hairs were left on the pillow.", "translation": "枕には何本かの落ちた毛が残っていた。"},
    ],
    "refurbish": [
        {"sentence": "The company decided to refurbish the old office building.", "translation": "その会社は古いオフィスビルを修復することを決めた。"},
        {"sentence": "They refurbished the vintage car to look like new.", "translation": "彼らはビンテージ車を修復して新しく見えるようにした。"},
        {"sentence": "The furniture was refurbished with fresh paint and new handles.", "translation": "家具は新しい塗料と新しい取手で修復された。"},
    ],
    "chunk": [
        {"sentence": "She cut a large chunk of cheese for the party.", "translation": "彼女はパーティーのために大きなチーズの塊を切った。"},
        {"sentence": "A chunk of ice broke off from the glacier.", "translation": "氷河から氷の塊が砕けて落ちた。"},
        {"sentence": "Learning a language requires working through a large chunk of grammar.", "translation": "言語を学ぶには大量の文法を学習する必要がある。"},
    ],
    "gallon": [
        {"sentence": "The paint bucket holds about one gallon of paint.", "translation": "ペンキの缶は約1ガロンのペンキを入れることができる。"},
        {"sentence": "This car uses one gallon of gasoline every 25 miles.", "translation": "この車は25マイルごとに1ガロンのガソリンを使う。"},
        {"sentence": "A gallon of milk was purchased at the store.", "translation": "1ガロンの牛乳が店で購入された。"},
    ],
    "boycott": [
        {"sentence": "Consumers decided to boycott the company due to poor practices.", "translation": "消費者たちは悪い実践のためにその会社をボイコットすることを決めた。"},
        {"sentence": "The students boycott the cafeteria to protest the food quality.", "translation": "学生たちは食事の質に抗議するためにカフェテリアをボイコットしている。"},
        {"sentence": "Many people support the boycott of products made with unfair labor.", "translation": "多くの人々は不公正な労働で作られた製品のボイコットを支持している。"},
    ],
    "fend": [
        {"sentence": "Wild animals must fend for themselves in nature.", "translation": "野生動物は自然界では自分たちを養わなければならない。"},
        {"sentence": "The boxer fended off multiple attacks during the fight.", "translation": "そのボクサーは試合中に複数の攻撃をかわした。"},
        {"sentence": "We need to fend off the competition by improving our product.", "translation": "製品を改善することで競争に対抗する必要がある。"},
    ],
    "convene": [
        {"sentence": "The committee will convene next Monday to discuss the project.", "translation": "委員会はプロジェクトについて議論するために来週月曜日に召集される。"},
        {"sentence": "The president convened an emergency meeting with the cabinet.", "translation": "大統領は内閣と緊急会議を召集した。"},
        {"sentence": "Members convene annually to share research findings.", "translation": "メンバーたちは研究成果を共有するために毎年開会する。"},
    ],
    "rim": [
        {"sentence": "The rim of the cup was decorated with gold.", "translation": "カップの縁は金で装飾されていた。"},
        {"sentence": "The car's rims were shiny and new.", "translation": "車のホイールは光沢があり新しかった。"},
        {"sentence": "She stood at the rim of the canyon and looked down.", "translation": "彼女は峡谷の縁に立ってその下を見た。"},
    ],
    "intercourse": [
        {"sentence": "There is regular intercourse between the two countries through trade agreements.", "translation": "2つの国の間に貿易協定を通じた定期的な交流がある。"},
        {"sentence": "Cultural intercourse helps people understand each other better.", "translation": "文化交流は人々が互いをよりよく理解するのに役立つ。"},
        {"sentence": "The company maintains intercourse with its overseas partners.", "translation": "その会社は海外のパートナーとの連絡を保つ。"},
    ],
    "armchair": [
        {"sentence": "Grandpa sat in his armchair reading the newspaper.", "translation": "おじいさんはひじ掛けいすに座って新聞を読んでいた。"},
        {"sentence": "The armchair was comfortable and perfect for relaxing.", "translation": "そのひじ掛けいすは快適でリラックスするのに完璧だった。"},
        {"sentence": "I fell asleep in the armchair while watching TV.", "translation": "私はテレビを見ながらひじ掛けいすで眠りに落ちた。"},
    ],
    "maxim": [
        {"sentence": "The maxim 'honesty is the best policy' is widely accepted.", "translation": "『正直さが最善の政策である』という格言は広く受け入れられている。"},
        {"sentence": "She lived by the maxim that hard work pays off.", "translation": "彼女は努力が報われるという格言に従って生きていた。"},
        {"sentence": "The business founder's maxim was 'customer satisfaction first.'", "translation": "ビジネス創業者の金言は『顧客満足が第一』だった。"},
    ],
    "coroner": [
        {"sentence": "The coroner examined the body to determine the cause of death.", "translation": "検死官は死因を判定するために遺体を調べた。"},
        {"sentence": "A coroner's inquest was held to investigate the accident.", "translation": "その事故を調査するために検死官による調査が行われた。"},
        {"sentence": "The coroner concluded that the death was from natural causes.", "translation": "検死官は死亡が自然死によるものであると結論付けた。"},
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
