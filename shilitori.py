
# (c)2021 Ryo Fujinami.

# インポート
import random
import os
from converters import word_dict, long_dict, voice_dict, kana_dict


# エラーか判定
def judge_error(pword, pwf, cwe, occur):
    if pwf != cwe:
        print('初めの文字を確認してください')
    elif len(pword) <= 1:
        print('１文字の単語は禁止です')
    elif len(pword) > 10:
        print('10文字より多い単語は禁止です')
    elif pword in occur:
        print('その言葉はもう出ています')
    else:
        return False
    return True


# 終了か判定
def judge_end(pword, pwe, word_dict, cwe):
    if pword in word_dict[cwe]:
        word_dict[cwe].remove(pword)
    if pwe == 'ン':
        print('「ン」が付きました\nあなたの負けです\nお疲れ様でした\n')
    elif len(word_dict[pwe]) == 0:
        print('もう言葉を思いつきません\n私の負けです\nお疲れ様でした\n')
    else:
        return False
    return True


# 次の単語を選ぶ
def send_next(pwe, word_dict, occur, long_dict, voice_dict):
    cword = random.choice(word_dict[pwe])
    word_dict[pwe].remove(cword)
    occur.append(cword)
    if cword[-1] == 'ー':
        cwe = long_dict[cword[-2]]
    else:
        cwe = cword[-1]
    cwe = voice_dict[cwe]
    return cword, cwe


# メイン
def main():
    print("ルール")
    print('＊ １文字だけの単語は禁止です')
    print('＊ 10文字以上の単語は禁止です')
    print('＊ 名詞を入力して"Enter"を押してください')
    print('＊ 最後に"ン"がついた時あなたの負けです')
    print('＊ 一度使われた単語は使えません')
    print('＊ 通常音と濁音・破裂音は区別しません')
    print('＊ カタカナ又はひらがなで入力してください\n')

    cwe = 'リ'
    occur = []  # 出現リスト
    num = 1  # 現在の回数
    cword = 'シリトリ'
    pwe = "始"
    occur.append(cword)
    print(" "+str(num)+" 回目")
    print(pwe+"："+cword)

    while True:
        pword = input(cwe+"：")
        if pword == "":
            print('入力してください')
            continue
        else:
            try:
                copy = ''
                for char in pword:
                    copy += kana_dict[char]
                pword = copy
            except Exception:
                print("カタカナ又はひらがなで入力してください")
                continue
            if pword[-1] == 'ー':
                pwe = long_dict[pword[-2]]
                pwf = pword[0]
            else:
                pwe = pword[-1]
                pwf = pword[0]
            pwe = voice_dict[pwe]
            pwf = voice_dict[pwf]
            if judge_error(pword, pwf, cwe, occur) is True:
                continue
            elif judge_end(pword, pwe, word_dict, cwe) is True:
                break
            else:
                occur.append(pword)
                cword, cwe = send_next(
                    pwe, word_dict, occur, long_dict, voice_dict)
                num += 1
                print("\n "+str(num)+" 回目")
                print(pwe+'：'+cword)

    input('このプログラムを終了するには"Enter"を押してください')
    return 0


if __name__ == "__main__":
    directory = os.path.dirname(__file__)
    os.chdir(directory)
    main()
