#!/usr/bin/env python3
"""Generate example sentences for words ranked 4650-4669"""

from supabase import create_client, Client

# Supabase credentials
url = "https://tvklrujikuanxdddyfcx.supabase.co"
key = "sb_publishable_DLHimQA_Wyt18fOtUH-o3w_1_BGYb0t"
supabase: Client = create_client(url, key)

# Words data
words_data = [
    {"id": "880ec6dc-2561-49c3-867c-ac1f0c3899c1", "word": "procession", "rank": 4650},
    {"id": "f619278e-22b7-4dc0-88a7-07125237b106", "word": "trot", "rank": 4651},
    {"id": "79c6f541-7faf-46dd-a9f8-c051c1da3bb7", "word": "zip", "rank": 4652},
    {"id": "33e3f83a-b9c1-4f05-a61b-72ef1e52378e", "word": "cannon", "rank": 4653},
    {"id": "f20ca3b5-2b00-4493-9e74-03bd4d85d729", "word": "marital", "rank": 4654},
    {"id": "805bd8ff-829c-47cd-bd4a-909d14984723", "word": "underestimate", "rank": 4655},
    {"id": "cc55fc9c-92bd-41fd-ae57-f79e107b5592", "word": "cartoon", "rank": 4656},
    {"id": "91ee4059-74bf-4f5d-b93b-d256ebf0b906", "word": "artery", "rank": 4657},
    {"id": "895c5369-123c-4dbe-b191-784adc49e15a", "word": "saturate", "rank": 4658},
    {"id": "093da289-2815-445e-af16-f1e340a403b7", "word": "stud", "rank": 4659},
    {"id": "9d4e4f49-32d2-47d8-8f3a-307f94eaf58e", "word": "verge", "rank": 4660},
    {"id": "6c71b264-e348-422b-967d-7cd45a64d74d", "word": "ascend", "rank": 4661},
    {"id": "6116c974-4a6f-420a-b458-03fb8ec6ad70", "word": "expel", "rank": 4662},
    {"id": "c7b0ca17-a89e-4074-b938-4a136d0897cc", "word": "wedge", "rank": 4663},
    {"id": "7f78f24c-b8f2-43ac-9d84-541b0f7f1cbd", "word": "papal", "rank": 4664},
    {"id": "9e710978-f103-4ac0-bcd9-c2cb67dcfa3a", "word": "bug", "rank": 4665},
    {"id": "38c4d02a-5b1f-41ae-b252-37b0fb24ced1", "word": "daunt", "rank": 4666},
    {"id": "ae1db0ca-ba0e-44c5-95a8-1ffebae202b9", "word": "coarse", "rank": 4667},
    {"id": "2b0ed545-ed95-4533-830c-5129127d08a2", "word": "conclusive", "rank": 4668},
    {"id": "3227147a-79c5-47a3-8ff4-e1d2d0c39420", "word": "diagnostic", "rank": 4669},
]

# Example sentences for each word
examples_dict = {
    "procession": [
        {"sentence": "A solemn procession moved through the city streets.", "translation": "荘厳な行列が街を通り抜けた。"},
        {"sentence": "The wedding procession began at noon.", "translation": "結婚式の行列は正午に始まった。"},
        {"sentence": "Thousands joined the procession to honor the leader.", "translation": "その指導者を敬礼するために数千人が行列に参加した。"},
    ],
    "trot": [
        {"sentence": "The horse began to trot along the path.", "translation": "その馬は小道に沿って速足で走り始めた。"},
        {"sentence": "He went for a morning trot in the park.", "translation": "彼は公園で朝の急ぎ足の散歩に行った。"},
        {"sentence": "She could not keep up with his trot.", "translation": "彼女は彼の小走りについていくことができなかった。"},
    ],
    "zip": [
        {"sentence": "He zipped his jacket against the cold.", "translation": "彼は寒さに対して彼のジャケットをチャックで締めた。"},
        {"sentence": "The bullet zipped past his head.", "translation": "その弾丸は彼の頭を通り過ぎた。"},
        {"sentence": "She zipped through the report in minutes.", "translation": "彼女は数分でその報告書を素早く完了した。"},
    ],
    "cannon": [
        {"sentence": "The old cannon sat in the fort as a relic.", "translation": "その古い大砲は砦に遺物として座っていた。"},
        {"sentence": "Cannons were fired to celebrate the victory.", "translation": "勝利を祝うために大砲が発射された。"},
        {"sentence": "The fighter jet's cannons could penetrate armor.", "translation": "その戦闘機の機関砲は装甲を貫通できた。"},
    ],
    "marital": [
        {"sentence": "Marital problems often lead to conflicts.", "translation": "結婚問題はしばしば紛争につながる。"},
        {"sentence": "They sought marital counseling to save their relationship.", "translation": "彼らは彼らの関係を救うために結婚カウンセリングを求めた。"},
        {"sentence": "The marital bond is sacred in many cultures.", "translation": "その結婚の絆は多くの文化で神聖である。"},
    ],
    "underestimate": [
        {"sentence": "Never underestimate your opponent in a competition.", "translation": "競争であなたの相手を過小評価してはいけません。"},
        {"sentence": "The team underestimated the difficulty of the task.", "translation": "そのチームはタスクの難しさを過小評価した。"},
        {"sentence": "Do not underestimate her intelligence.", "translation": "彼女の知性を過小評価しないでください。"},
    ],
    "cartoon": [
        {"sentence": "The children watched cartoons on Saturday morning.", "translation": "子どもたちは土曜の朝にアニメ映画を見た。"},
        {"sentence": "This newspaper features a political cartoon daily.", "translation": "この新聞は毎日政治風刺漫画を特集している。"},
        {"sentence": "He drew a cartoon of the mayor in the magazine.", "translation": "彼は雑誌でその市長の漫画を描いた。"},
    ],
    "artery": [
        {"sentence": "The coronary artery supplies blood to the heart.", "translation": "その冠状動脈は心臓に血液を供給する。"},
        {"sentence": "The main artery was congested during rush hour.", "translation": "その幹線道路はラッシュ時間に混雑していた。"},
        {"sentence": "Clogged arteries can lead to heart attacks.", "translation": "詰まった動脈は心臓発作につながる可能性がある。"},
    ],
    "saturate": [
        {"sentence": "Heavy rain will saturate the soil.", "translation": "大雨は土壌を飽和させるでしょう。"},
        {"sentence": "The fabric was saturated with water.", "translation": "その布は水で浸されていた。"},
        {"sentence": "The market is saturated with similar products.", "translation": "その市場は同様の製品で満ちあふれている。"},
    ],
    "stud": [
        {"sentence": "The fence posts are connected by studs.", "translation": "その柵の柱はスタッドで接続されている。"},
        {"sentence": "She wore diamond studs in her ears.", "translation": "彼女は彼女の耳にダイヤモンド飾りを着けていた。"},
        {"sentence": "The thoroughbred was a prize stud at the farm.", "translation": "そのサラブレッドはその農場の賞受賞した種馬だった。"},
    ],
    "verge": [
        {"sentence": "The two nations stood on the verge of war.", "translation": "その2つの国は戦争の寸前に立っていた。"},
        {"sentence": "He is on the verge of bankruptcy.", "translation": "彼は破産の寸前にいる。"},
        {"sentence": "The discovery verges on the impossible.", "translation": "その発見は不可能に近い。"},
    ],
    "ascend": [
        {"sentence": "The climbers ascended the mountain early in the morning.", "translation": "その登山者たちは朝早く山に登った。"},
        {"sentence": "The balloon ascended into the clear sky.", "translation": "そのバルーンは澄んだ空に上昇した。"},
        {"sentence": "He ascended to the throne after his father's death.", "translation": "彼は彼の父親の死後、王位についた。"},
    ],
    "expel": [
        {"sentence": "The school decided to expel the troublemaking student.", "translation": "その学校は問題を起こしている学生を除名することを決めた。"},
        {"sentence": "The plant expels oxygen as part of photosynthesis.", "translation": "その植物は光合成の一部として酸素を吐き出す。"},
        {"sentence": "The government expels foreign diplomats for espionage.", "translation": "政府はスパイ行為のために外国の外交官を追い出す。"},
    ],
    "wedge": [
        {"sentence": "He drove a wedge into the log to split it.", "translation": "彼はそれを分割するために丸太にくさびを打ち込んだ。"},
        {"sentence": "The wedge-shaped clouds indicated changing weather.", "translation": "そのくさび形の雲は天気の変化を示した。"},
        {"sentence": "She wedged herself between the two boxes.", "translation": "彼女は2つのボックスの間に無理に押し込んだ。"},
    ],
    "papal": [
        {"sentence": "The papal authority is respected by millions.", "translation": "その教皇の権威は何百万人に尊重されている。"},
        {"sentence": "The papal residence is in Vatican City.", "translation": "その教皇の住居はバチカン市国にある。"},
        {"sentence": "She received a papal blessing from the Pope.", "translation": "彼女は教皇から教皇の祝福を受けた。"},
    ],
    "bug": [
        {"sentence": "A bug landed on the window.", "translation": "虫が窓に着地した。"},
        {"sentence": "The software has a bug that needs to be fixed.", "translation": "そのソフトウェアには修正が必要なバグがある。"},
        {"sentence": "That travel bug influenced her life choices.", "translation": "その旅行熱は彼女の人生の選択に影響を与えた。"},
    ],
    "daunt": [
        {"sentence": "The difficult challenge did not daunt her.", "translation": "その難しい課題は彼女をおびえさせなかった。"},
        {"sentence": "His experience will not daunt him from trying.", "translation": "彼の経験は彼が試みるのをおびえさせないだろう。"},
        {"sentence": "The massive project daunted even the experienced team.", "translation": "その巨大なプロジェクトは経験豊富なチームさえもおびえさせた。"},
    ],
    "coarse": [
        {"sentence": "The coarse texture of the fabric was uncomfortable.", "translation": "その布の粗い質感は不快だった。"},
        {"sentence": "He made a coarse joke that offended people.", "translation": "彼は人々を不快にさせた下品なジョークをした。"},
        {"sentence": "The coarse sand was unsuitable for the beach.", "translation": "その粗い砂はビーチに適していなかった。"},
    ],
    "conclusive": [
        {"sentence": "The DNA test provided conclusive evidence.", "translation": "そのDNAテストは決定的な証拠を提供した。"},
        {"sentence": "His argument was conclusive and ended the debate.", "translation": "彼の議論は結論的で議論を終わらせた。"},
        {"sentence": "The study reached conclusive findings.", "translation": "その研究は結論的な発見に達した。"},
    ],
    "diagnostic": [
        {"sentence": "The diagnostic test revealed the disease.", "translation": "その診断テストは病気を明かした。"},
        {"sentence": "Diagnostic imaging helps doctors identify problems.", "translation": "診断イメージングは医師が問題を特定するのに役立つ。"},
        {"sentence": "The diagnostic results confirmed his suspicion.", "translation": "その診断結果は彼の疑いを確認した。"},
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
