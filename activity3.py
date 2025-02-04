print("enter marks obtained in 4 subjects:")
math=int(input("maths marks:"))
science=int(input("science marks:"))
history=int(input("history marks:"))
language=int(input("language marks:"))
sum=math+science+history+language
print("sum of all 4 subjects is:",sum)
perc=(sum/400)*100
print("percentage marks =",perc)