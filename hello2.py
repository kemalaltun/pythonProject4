import random
import time
def bekle():
    time.sleep(0.5)
gameStatus = input("Oynamak istiyor musun?\n").lower()
while gameStatus=="evet":
    bekle()
    randomNumber = random.randrange(1,11)
    print("aklımdan 1 ile 10 arasında bir sayı tuttum bil bakalım")
    bekle()
    userInput = int(input("tahminini gir\n"))
    bekle()
    while userInput != randomNumber :
        userInput = int(input("bilemedin tekrar tahmin et\n"))
    bekle()
    print("tebrikler bildin!","sayımız ->", str(randomNumber))
    gameStatus = input("Oynamak istiyor musun?\n").lower()
bekle()
print("Hoşçakal!")


