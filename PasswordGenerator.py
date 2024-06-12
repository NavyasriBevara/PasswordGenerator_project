#WEEK-4 PROJECT
import random
print("RANDOM PASSWORD GENERATOR")
lower="abcdefghijklmnopqrstuvwxyz"
upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers="0123456789"
special_char="!@#$%^&*()_+{}[]?"
all=lower+upper+numbers+special_char
length=8
n=int(input("Number of times you want to generate password:"))
for i in range(n):
    password="".join(random.sample(all,length))
    print(password)
