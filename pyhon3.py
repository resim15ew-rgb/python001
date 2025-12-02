#リストーーーーーーーーーー
mylist =[3,1,4,5,2]
mylist = sorted(1, reverse=True)
# [5,4,3,2,1]

fruits=["バナナ","りんご"]

fruits.append("ブドウ")  # 追加
fruits.remove("バナナ")  # 削除
fruits.pop(1)

fruits.sort() # 昇順
fruits.sort(reverse=True) # 降順S

if mylist[2] > mylist[4]:
    print(mylist[2])
else:
    print(mylist[4])

for fruit in fruits:
    print(fruit)


#辞書ーーーーーーーーーーーー
mydict = {"apple":1,"banana":2,"orange":3,"grape":4}
val = mydict["apple"]
print(val) 

mydict["peach"]=5 # 追加
# apple":1,"banana":2,"orange":3,"grape":4,"peach":5
print(mydict)

mydict1 = {"apple":1,"banana":2,"orange":3}
mydict2 = {"grape":4,"melon":5,"cherry":6}
mydict1["dict"] = mydict2
print(mydict1)
# "apple":1,'dict':{"grape":4,"melon":5,"cherry":6}, "banana":2,"orange":3

for subject, no in mydict.items():
    print(f'{subject}: {no}')
    s = f.read()
    print(type(s))
    print(s)
    
