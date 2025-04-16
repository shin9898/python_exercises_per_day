# Day5 解答テンプレート

# sample.txt から単語の出現頻度をカウントして出力するプログラムを書いてください。
# 以下のヒントを活用しても構いません。

# ヒント:
# - open("sample.txt", "r") でファイルを読み込めます
# - line.lower().split() で単語リストに変換できます
# - collections.Counter を使うと便利です

from collections import Counter


def count_words(filename: str) -> None:
    with open(filename, 'r', encoding="utf-8") as f:
        word_list_counter = []
        while True:
            lines = f.readline()
            if lines != '':
                word_list = lines.rstrip("\n").lower().split(' ')
                for word in word_list:
                    word_list_counter.append(word)
            else:
                break
    result_dict = Counter(word_list_counter)
    num = 1
    for k, v in result_dict.items():
        if num <= 5:
          print(f"{k}: {v}")
          num += 1



if __name__ == "__main__":
    count_words("sample.txt")
