#!/usr/bin/env python3
"""Generate example sentences for words ranked 4750-4769"""

from supabase import create_client, Client

# Supabase credentials
url = "https://tvklrujikuanxdddyfcx.supabase.co"
key = "sb_publishable_DLHimQA_Wyt18fOtUH-o3w_1_BGYb0t"
supabase: Client = create_client(url, key)

# Words data
words_data = [
    {"id": "14d35be5-a649-4b9a-b593-1e6a6d29d314", "word": "composite", "rank": 4750},
    {"id": "2de394b6-6c28-4a42-b619-3fa43c644532", "word": "trait", "rank": 4752},
    {"id": "e57245ea-59e8-4be5-8f80-879ba2be4903", "word": "dazzle", "rank": 4753},
    {"id": "f2b4a1b5-b9ae-437f-b7cb-4392529f380e", "word": "ecology", "rank": 4754},
    {"id": "c87d4aab-cf13-4234-8aba-b6a6ebe6fa5f", "word": "overt", "rank": 4755},
    {"id": "a9675c1e-9555-4e0f-8d4d-85208af669ca", "word": "berry", "rank": 4756},
    {"id": "076c5b3b-084b-4f56-8996-dfa9e565ef04", "word": "excursion", "rank": 4757},
    {"id": "7edba375-ac0c-4e18-9278-92bbca8c47c3", "word": "artefact", "rank": 4758},
    {"id": "2ce51092-6002-44d2-8aef-65fa33896d51", "word": "deceased", "rank": 4759},
    {"id": "aa1d5de1-cfba-4797-8a0a-3ac4597612e3", "word": "depot", "rank": 4760},
    {"id": "0b99078e-f1b0-4813-b910-f8d70cadee64", "word": "probation", "rank": 4761},
    {"id": "cf7522a2-1b64-4155-b451-880653160018", "word": "infringe", "rank": 4762},
    {"id": "da024470-8a9a-419b-a6f6-04dc20304f68", "word": "chamberlain", "rank": 4763},
    {"id": "41142645-200b-471c-aada-d98833dd8336", "word": "hygiene", "rank": 4765},
    {"id": "6a091e3b-33ea-4a46-94f9-f8a4b138e878", "word": "shove", "rank": 4766},
    {"id": "8cfccaf3-b465-43d0-835f-0ca8ca6f4daf", "word": "howl", "rank": 4767},
    {"id": "33c6ca69-17b3-4dd8-b6d3-bdbdcd6712aa", "word": "shorts", "rank": 4768},
    {"id": "3d3dc50a-aca4-41d7-bc5c-0809629a957f", "word": "pesticide", "rank": 4769},
]

# Example sentences for each word
examples_dict = {
    "composite": [
        {"sentence": "The composite material was strong and lightweight.", "translation": "その合成材料は強くて軽かった。"},
        {"sentence": "A composite score combines multiple test results.", "translation": "複合スコアは複数のテスト結果を組み合わせている。"},
        {"sentence": "The artwork is a composite of different styles.", "translation": "その美術作品はさまざまなスタイルの複合物である。"},
    ],
    "trait": [
        {"sentence": "Honesty is an important trait in business.", "translation": "正直さはビジネスにおける重要な特性である。"},
        {"sentence": "She inherited her mother's artistic trait.", "translation": "彼女は彼女の母親の芸術的な特質を相続した。"},
        {"sentence": "Persistence is a common trait of successful people.", "translation": "粘り強さは成功した人々の共通の特性である。"},
    ],
    "dazzle": [
        {"sentence": "The bright lights dazzled her eyes.", "translation": "その明るい光は彼女の目をくらませた。"},
        {"sentence": "The fireworks display dazzled the crowd.", "translation": "その花火ショーは群衆を眩惑させた。"},
        {"sentence": "Her beauty dazzled everyone who met her.", "translation": "彼女の美しさは彼女に会った誰もを眩惑させた。"},
    ],
    "ecology": [
        {"sentence": "Ecology studies the relationships between organisms and their environment.", "translation": "生態学は生物とそれらの環境との関係を研究している。"},
        {"sentence": "The professor teaches ecology at the university.", "translation": "その教授は大学で生態学を教えている。"},
        {"sentence": "Understanding ecology is important for conservation.", "translation": "生態学を理解することは保全にとって重要である。"},
    ],
    "overt": [
        {"sentence": "His overt criticism was not appreciated by the team.", "translation": "彼の公然の批判はチームに評価されなかった。"},
        {"sentence": "There was no overt hostility between the groups.", "translation": "グループ間に公然の敵意はなかった。"},
        {"sentence": "The overt agreement was signed by both parties.", "translation": "その明白な協定は両者によって署名された。"},
    ],
    "berry": [
        {"sentence": "She picked berries from the bush.", "translation": "彼女は茂みからベリーを摘んだ。"},
        {"sentence": "Strawberry is a delicious summer berry.", "translation": "イチゴは美味しい夏のベリーである。"},
        {"sentence": "The blueberry pie was the chef's specialty.", "translation": "そのブルーベリーパイはそのシェフの専門だった。"},
    ],
    "excursion": [
        {"sentence": "The school organized an excursion to the museum.", "translation": "その学校は博物館への小旅行を組織した。"},
        {"sentence": "We took an excursion into the countryside.", "translation": "私たちは田舎への小旅行に行った。"},
        {"sentence": "The travel agency offers discounted excursion packages.", "translation": "その旅行代理店は割引された周遊旅行パッケージを提供している。"},
    ],
    "artefact": [
        {"sentence": "The museum displayed ancient artefacts from Egypt.", "translation": "その博物館はエジプトからの古代遺物を展示していた。"},
        {"sentence": "Archaeologists discovered valuable artefacts at the site.", "translation": "考古学者たちはそのサイトで貴重な遺物を発見した。"},
        {"sentence": "The artefact was carefully restored by experts.", "translation": "その遺物は専門家によって慎重に復元された。"},
    ],
    "deceased": [
        {"sentence": "The deceased was a respected community member.", "translation": "その故人は尊敬されたコミュニティメンバーだった。"},
        {"sentence": "Relatives gathered to mourn the deceased.", "translation": "親族たちは故人を悼むために集まった。"},
        {"sentence": "The deceased left a substantial estate.", "translation": "その故人は相当な遺産を残した。"},
    ],
    "depot": [
        {"sentence": "The train depot was crowded with passengers.", "translation": "その駅は乗客でいっぱいだった。"},
        {"sentence": "The supply depot stores military equipment.", "translation": "その物資集積所は軍事機器を保存している。"},
        {"sentence": "The bus depot is located downtown.", "translation": "そのバス発着所は市街地に位置している。"},
    ],
    "probation": [
        {"sentence": "The new employee is on probation for three months.", "translation": "その新しい従業員は3ヶ月間試用期間中である。"},
        {"sentence": "He was placed on probation after the offense.", "translation": "彼はその違反の後に保護観察に置かれた。"},
        {"sentence": "During probation, performance will be carefully monitored.", "translation": "試用期間中、パフォーマンスは慎重に監視される。"},
    ],
    "infringe": [
        {"sentence": "The company infringe on the copyright.", "translation": "その会社は著作権を侵害した。"},
        {"sentence": "The new law infringe the citizens' rights.", "translation": "その新しい法律は市民の権利を侵害している。"},
        {"sentence": "Do not infringe on other people's property.", "translation": "他の人たちの財産を侵害しないでください。"},
    ],
    "chamberlain": [
        {"sentence": "The chamberlain managed the royal household.", "translation": "その侍従は王室の家計を管理した。"},
        {"sentence": "The chamberlain was responsible for the castle's treasury.", "translation": "その執事は城の財務を担当していた。"},
        {"sentence": "The Lord Chamberlain served the royal family.", "translation": "その大侍従は王族に仕えた。"},
    ],
    "hygiene": [
        {"sentence": "Good hygiene practices prevent disease.", "translation": "良い衛生慣行は病気を防ぐ。"},
        {"sentence": "The school emphasizes proper hygiene to students.", "translation": "その学校は生徒に適切な衛生を強調している。"},
        {"sentence": "Personal hygiene is important for health.", "translation": "個人的な衛生は健康に重要である。"},
    ],
    "shove": [
        {"sentence": "He shoved me out of the way.", "translation": "彼は私を道から強く押した。"},
        {"sentence": "Don't shove in the crowded line.", "translation": "混雑した列で押さないでください。"},
        {"sentence": "She received a shove from the crowd.", "translation": "彼女は群衆から強い押しを受けた。"},
    ],
    "howl": [
        {"sentence": "The wolf howled at the moon.", "translation": "そのオオカミは月に遠ぼえした。"},
        {"sentence": "The wind howled through the canyon.", "translation": "その風は峡谷を通ってうなった。"},
        {"sentence": "The baby let out a howl of protest.", "translation": "その赤ちゃんは抗議のうめき声を出した。"},
    ],
    "shorts": [
        {"sentence": "He wore shorts and a t-shirt in the summer.", "translation": "彼は夏に半ズボンとTシャツを着ていた。"},
        {"sentence": "The athlete changed into fresh shorts.", "translation": "そのアスリートは新しい半ズボンに着替えた。"},
        {"sentence": "Shorts are comfortable for outdoor activities.", "translation": "半ズボンは屋外活動に快適である。"},
    ],
    "pesticide": [
        {"sentence": "The farmer sprayed pesticide on the crops.", "translation": "その農夫は作物に殺虫剤を噴きかけた。"},
        {"sentence": "Excessive pesticide use harms the environment.", "translation": "過度の殺虫剤使用は環境に害をもたらす。"},
        {"sentence": "Organic farming avoids synthetic pesticides.", "translation": "有機農業は合成殺虫剤を避ける。"},
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
