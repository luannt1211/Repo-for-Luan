import MeCab


STOP_WORDS = '''
あそこ
あっ
あの
あのかた
あの人
あり
あります
ある
あれ
い
いう
います
いる
う
うち
え
お
および
おり
おります
か
かつて
から
が
き
ここ
こちら
こと
この
これ
これら
さ
さらに
し
しかし
する
ず
せ
せる
そこ
そして
その
その他
その後
それ
それぞれ
それで
た
ただし
たち
ため
たり
だ
だっ
だれ
つ
て
で
でき
できる
です
では
でも
と
という
といった
とき
ところ
として
とともに
とも
と共に
どこ
どの
な
ない
なお
なかっ
ながら
なく
なっ
など
なに
なら
なり
なる
なん
に
において
における
について
にて
によって
により
による
に対して
に対する
に関する
の
ので
のみ
は
ば
へ
ほか
ほとんど
ほど
ます
また
または
まで
も
もの
ものの
や
よう
より
ら
られ
られる
れ
れる
を
ん
何
及び
彼
彼女
我々
特に
私
私達
。
、
・
「
」
'''.strip().split('\n')


def tokenize(text, stop_words=None):
    '''Break a sentence into many words (tokenize).
    Inputs:
        a text
        stop_words: optional.
    
    Return:
    -------
        A list of words.
    '''
    # Prepare stop words
    stop_words = stop_words if stop_words else []
    # Tokenize input text into list of keywords
    wakati = MeCab.Tagger("-Owakati")
    tokens = wakati.parse(text).split()
    # Remove stop words
    tokens = [word for word in tokens if word not in stop_words]
    return tokens
