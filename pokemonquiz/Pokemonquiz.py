import random

class PokemonQuiz:
    def __init__(self):
        self.questions = [
            {
                "question": "草タイプが含まれるポケモンは？",
                "choices": ["ピカチュウ", "ヒトカゲ", "フシギダネ", "ゼニガメ"],
                "answer": "フシギダネ"
            },
            {
                "question": "ピカチュウの進化形は？",
                "choices": ["ライチュウ", "サンダース", "エレブー", "カイリュー"],
                "answer": "ライチュウ"
            },
            {
                "question": "初代ポケモンの数は？",
                "choices": ["100", "150", "151", "200"],
                "answer": "151"
            },
            {
                "question": "『ポケットモンスター 赤・緑』の最初の舞台は？",
                "choices": ["ジョウト地方", "カントー地方", "ホウエン地方", "シンオウ地方"],
                "answer": "カントー地方"
            },
            {
                "question": "ポケモン図鑑001のポケモンは？",
                "choices": ["ピカチュウ", "フシギダネ", "ゼニガメ", "ヒトカゲ"],
                "answer": "フシギダネ"
            },
            {
                "question":"サトシのピカチュウが使ったことのない技は？",
                "choices":["エレキボール","アイアンテール","ワイルドボルト","10まんボルト"],
                "answer":"ワイルドボルト"
            },
            {
                "question":"命中が100ではない技はどれ？",
                "choices":["じしん","げきりん","フレアドライブ","じゃれつく"],
                "answer":"じゃれつく"
            },
            {
                "question":"この中でシロナが使っているポケモンは？",
                "choices":["ガブリアス","グライオン","ドラピオン","ゲンガー"],
                "answer":"ガブリアス"
            },
            {
                "question":"クロガネシティのジムリーダーの名前は？",
                "choices":["ソウタ","ヒョウタ","コウタ","ケンタ"],
                "answer":"ヒョウタ"
            },
            {
                "question":"サトシが捕まえた色違いのポケモンは？",
                "choices":["ヨルノズク","トゲキッス","シンボラー","ウォーグル"],
                "answer":"ヨルノズク"
            }
        ]
        self.score = 0

    def start_quiz(self):
        print("ポケモンクイズへようこそ！")
        random.shuffle(self.questions)
        
        for idx, question in enumerate(self.questions):
            print(f"\n質問 {idx + 1}: {question['question']}")
            for i, choice in enumerate(question['choices']):
                print(f"{i + 1}. {choice}")
            
            answer = input("答えを数字で選んでください: ")

            if not answer.isdigit() or int(answer) < 1 or int(answer) > len(question['choices']):
                print("無効な入力です。正しい数字を入力してください。")
                continue
            
            if question['choices'][int(answer) - 1] == question['answer']:
                print("正解です！")
                self.score += 1
            else:
                print(f"不正解です。正解は {question['answer']} です。")

        print(f"\nクイズ終了！あなたのスコアは {self.score}/{len(self.questions)} です。")

if __name__ == "__main__":
    quiz = PokemonQuiz()
    quiz.start_quiz()
