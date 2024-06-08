print("hello world",end="")
print(" yani selam Dünya")
print("Mustafa","Kemal","Altun")
age = 23
positiveResultText = "18 yaşından büyük"
negativeResultText = "18 yaşından küçük"
resultText= positiveResultText if age > 18 else negativeResultText
resultText2 = negativeResultText if age < 18 else positiveResultText
print(resultText2)