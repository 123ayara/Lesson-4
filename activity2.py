amount=int(input("enter amount for withdraw:"))
note1=amount//100
note2=(amount%100)//50
note3=((amount%100)%50)//10
print("notes of 100 are:",note1)
print("notes of 50 are:",note2)
print("notes of 10 are:",note3)
