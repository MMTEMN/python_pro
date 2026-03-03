import random
sec=random.randint(1,20)
print("1 le 20 arasinda bir sayi tuttum hadi bil bakalim")
print(sec)
for i in range(5):
    bil=int(input("tahminini yaz: "))
    if bil==sec:
        print("dogru bildin")
        break
    elif bil>sec:
        print("in asagi")
    else:
        print("cik yukari")





if bil!=sec:
    print("hakkin bitti tuttugum sayi ",sec)

