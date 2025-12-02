import locale

print(locale.getpreferredencoding())
# UTF-8と表示される

# ファイルパス
path = 'test.txt'

# ファイル全体を文字列として読み込み
with open(path) as f:
    s = f.read()
    
    #カンマ区切りでリスト化
    #s = "1,"A","ADATA""

    #→mylist = [1,"A","ADATA"]
    items = s.strip().split(",")

    # lines = []
    # for line in s.splitlines():
    #     lines.append(line)


    print(type(s)) 
    print(s)
    print(items[1])
    print(items[2])





# ファイルクローズ
# f.close()




