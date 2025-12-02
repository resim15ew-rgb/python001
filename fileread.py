import locale

print(locale.getpreferredencoding())
# UTF-8と表示される

# ファイルパス
path = 'test.txt'

# ファイルオープン
# f = open(path)

# ファイルクローズ
# f.close()

# ファイル全体を文字列として読み込み
with open(path) as f:
    s = f.read()
    print(type(s)) 
    print(s)


# ファイル全体をリストとして読み込み
with open(path) as f:
    l = f.readlines()
    print(type(l)) 
    print(l)

# ファイルを1行ずつ読み込み
with open(path) as f:
    for r_line in f:
        print(repr(r_line)) 

# 文字列を書き込み
with open(path,mode="w") as f:
    f.write(s)



