#!/usr/bin/env python3
"""Generate example sentences for words ranked 4770-4789"""

from supabase import create_client, Client

# Supabase credentials
url = "https://tvklrujikuanxdddyfcx.supabase.co"
key = "sb_publishable_DLHimQA_Wyt18fOtUH-o3w_1_BGYb0t"
supabase: Client = create_client(url, key)

# Words data
words_data = [
    {"id": "c6dd128d-2b52-43b7-b1c1-049e61afd5b6", "word": "sprinkle", "rank": 4770},
    {"id": "c9d7c5d3-fbcf-4c6c-a154-e85d6ee4b350", "word": "merry", "rank": 4771},
    {"id": "ba53eed2-97fa-4554-88d5-9c64c958520e", "word": "deplete", "rank": 4772},
    {"id": "8e85c050-b7d8-4d24-ac0a-649c8b776a8c", "word": "mint", "rank": 4773},
    {"id": "fa09ed27-2470-4bc7-b370-03030dace5e5", "word": "dismay", "rank": 4774},
    {"id": "9fae7463-db94-44cb-85a1-62e57265e0fa", "word": "overthrow", "rank": 4775},
    {"id": "55e8ba26-5b6e-478c-8668-16d5d8d604aa", "word": "poise", "rank": 4776},
    {"id": "420da3a4-69a8-4551-9139-53a5ba696356", "word": "postgraduate", "rank": 4777},
    {"id": "ea3f63e7-c909-43b1-8cd1-4a1b9576be7d", "word": "bilateral", "rank": 4778},
    {"id": "db78b888-2c80-4c2e-9c71-d403cf24a4ff", "word": "grape", "rank": 4779},
    {"id": "18ee1584-dd70-4d7e-a474-5824f3c98644", "word": "drunken", "rank": 4780},
    {"id": "4e72db74-7621-48b0-858b-2a3a36c7a5ab", "word": "recollect", "rank": 4781},
    {"id": "b3175a29-ff18-4f69-beab-c9fea9706074", "word": "sanctuary", "rank": 4782},
    {"id": "2b725725-c6a2-4006-99e5-1b4fc2197043", "word": "vandal", "rank": 4783},
    {"id": "8fc7b5fc-29f8-4eec-8084-5adee30d7220", "word": "onset", "rank": 4784},
    {"id": "0e4ecf07-1843-4089-98e0-9149497677d7", "word": "vase", "rank": 4785},
    {"id": "fc298de4-d222-4a94-9442-35c36f822c63", "word": "cocktail", "rank": 4787},
    {"id": "6d762f29-468d-4af6-8f16-a7a89a40d13b", "word": "sprint", "rank": 4788},
    {"id": "67da74f4-8e80-43e4-a1f7-0abc2bef7fdf", "word": "technician", "rank": 4789},
]

# Example sentences for each word
examples_dict = {
    "sprinkle": [
        {"sentence": "She sprinkled sugar on the dessert.", "translation": "彼女はデザートに砂糖を振りかけた。"},
        {"sentence": "A light sprinkle of rain fell this morning.", "translation": "今朝、小雨がぱらぱら降った。"},
        {"sentence": "Sprinkle salt on the vegetables before cooking.", "translation": "調理する前に野菜に塩を振りかけてください。"},
    ],
    "merry": [
        {"sentence": "The children had a merry time at the party.", "translation": "その子どもたちはパーティーで楽しい時を過ごした。"},
        {"sentence": "She greeted everyone with a merry laugh.", "translation": "彼女は陽気な笑いでみんなを挨拶した。"},
        {"sentence": "We wish you a merry Christmas.", "translation": "楽しいクリスマスをお祈りします。"},
    ],
    "deplete": [
        {"sentence": "The drought depleted the water supply.", "translation": "その干ばつは水供給を激減させた。"},
        {"sentence": "Overfishing will deplete fish stocks.", "translation": "過度な漁業は魚の在庫を使い果たすだろう。"},
        {"sentence": "The resources were depleted by the war.", "translation": "その資源は戦争によって枯渇した。"},
    ],
    "mint": [
        {"sentence": "The mojito is a drink made with mint.", "translation": "モヒートはハッカで作られた飲み物である。"},
        {"sentence": "The government minted new coins last year.", "translation": "政府は去年新しい硬貨を鋳造した。"},
        {"sentence": "This antique is worth a mint.", "translation": "このアンティークはかなりの値打ちがある。"},
    ],
    "dismay": [
        {"sentence": "The bad news caused dismay among the team.", "translation": "その悪いニュースはチームに落胆をもたらした。"},
        {"sentence": "His sudden departure dismayed everyone.", "translation": "彼の突然の出発はみんなをうろたえさせた。"},
        {"sentence": "She watched in dismay as the accident happened.", "translation": "彼女はその事故が起きたとき、落胆して見ていた。"},
    ],
    "overthrow": [
        {"sentence": "The revolution led to the overthrow of the government.", "translation": "その革命は政府の転覆につながった。"},
        {"sentence": "The general planned to overthrow the dictator.", "translation": "その将軍は独裁者を倒すための計画をしていた。"},
        {"sentence": "The vase was accidentally overthrown.", "translation": "その花びんは誤ってひっくり返された。"},
    ],
    "poise": [
        {"sentence": "The gymnast maintained perfect poise on the beam.", "translation": "その体操選手は梁の上で完璧なバランスを保った。"},
        {"sentence": "Despite stress, she maintained her poise.", "translation": "ストレスにもかかわらず、彼女は彼女の平静を保った。"},
        {"sentence": "The dancer moved with grace and poise.", "translation": "そのダンサーは優雅さと平衡で動いた。"},
    ],
    "postgraduate": [
        {"sentence": "He is pursuing a postgraduate degree in chemistry.", "translation": "彼は化学の大学院の学位を追求している。"},
        {"sentence": "The postgraduate program is two years long.", "translation": "その大学院プログラムは2年間である。"},
        {"sentence": "Postgraduate studies require advanced research skills.", "translation": "大学院の研究は高度な研究スキルを必要とする。"},
    ],
    "bilateral": [
        {"sentence": "The two countries signed a bilateral trade agreement.", "translation": "その2つの国は二国間貿易協定に署名した。"},
        {"sentence": "The treaty requires bilateral approval.", "translation": "その条約は双方の承認を必要とする。"},
        {"sentence": "Bilateral talks were held to resolve the dispute.", "translation": "紛争を解決するために二国間協議が行われた。"},
    ],
    "grape": [
        {"sentence": "She picked a ripe grape from the vine.", "translation": "彼女はつるから熟したぶどうを摘んだ。"},
        {"sentence": "Grapes are rich in antioxidants.", "translation": "ぶどうは抗酸化物質が豊富である。"},
        {"sentence": "Wine is made from fermented grapes.", "translation": "ワインは発酵したぶどうから作られている。"},
    ],
    "drunken": [
        {"sentence": "The drunken man stumbled down the street.", "translation": "その酔った男は通りを蹌踉と歩いた。"},
        {"sentence": "He made a drunken mistake at the party.", "translation": "彼はパーティーで酔ったあげくの間違いをした。"},
        {"sentence": "Drunken driving is illegal and dangerous.", "translation": "飲酒運転は違法で危険である。"},
    ],
    "recollect": [
        {"sentence": "I can't recollect what happened that day.", "translation": "私はその日に何が起きたかを思い出すことができない。"},
        {"sentence": "She paused to recollect her thoughts.", "translation": "彼女は彼女の考えを整理するために一時停止した。"},
        {"sentence": "As I recollect, the meeting was on Tuesday.", "translation": "思い出すところでは、その会議は火曜日だった。"},
    ],
    "sanctuary": [
        {"sentence": "The church provided sanctuary for the refugees.", "translation": "その教会は難民に保護を提供した。"},
        {"sentence": "The wildlife sanctuary protects endangered animals.", "translation": "その野生動物保護区は絶滅危機に瀕した動物を保護している。"},
        {"sentence": "She found sanctuary in her studies during difficult times.", "translation": "彼女は困難な時期に研究に避難を見つけた。"},
    ],
    "vandal": [
        {"sentence": "A vandal destroyed the public monument.", "translation": "その破壊者は公共のモニュメントを破壊した。"},
        {"sentence": "The vandals spray-painted the bridge.", "translation": "その破壊者たちは橋にスプレーペイントをした。"},
        {"sentence": "The security camera caught the vandal on film.", "translation": "そのセキュリティカメラはその破壊者をフィルムに捉えた。"},
    ],
    "onset": [
        {"sentence": "The onset of winter brings cold temperatures.", "translation": "冬の始まりは寒い気温をもたらす。"},
        {"sentence": "The onset of the disease was sudden.", "translation": "その病気の始まりは突然だった。"},
        {"sentence": "At the onset of the attack, soldiers fought back.", "translation": "その攻撃の始まりに、兵士たちは反撃した。"},
    ],
    "vase": [
        {"sentence": "She placed fresh flowers in the vase.", "translation": "彼女は花びんに新鮮な花を置いた。"},
        {"sentence": "The antique vase was worth thousands of dollars.", "translation": "そのアンティークの花びんは何千ドルもの値打ちがあった。"},
        {"sentence": "The vase was decorated with blue patterns.", "translation": "その花びんは青いパターンで装飾されていた。"},
    ],
    "cocktail": [
        {"sentence": "They served cocktails at the reception.", "translation": "彼らはレセプションでカクテルを出した。"},
        {"sentence": "A margarita is a popular cocktail.", "translation": "マルガリータは人気のあるカクテルである。"},
        {"sentence": "The bartender mixed an excellent cocktail.", "translation": "そのバーテンダーは素晴らしいカクテルをミックスした。"},
    ],
    "sprint": [
        {"sentence": "The runner sprinted the final 100 meters.", "translation": "そのランナーは最後の100メートルを全速力で走った。"},
        {"sentence": "A sprint is a short-distance race.", "translation": "短距離競走は短距離レースである。"},
        {"sentence": "The cyclist sprinted towards the finish line.", "translation": "そのサイクリストはフィニッシュラインに向かって全速力で走った。"},
    ],
    "technician": [
        {"sentence": "The technician repaired the broken equipment.", "translation": "その技術者は壊れた機器を修理した。"},
        {"sentence": "A skilled technician is needed for this job.", "translation": "この仕事には熟練した技術者が必要である。"},
        {"sentence": "The lab technician analyzed the samples.", "translation": "そのラボの技術者はサンプルを分析した。"},
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

    print(f"\n📊 Total examples inserted: {total_inserted}/57")

if __name__ == "__main__":
    insert_examples()
