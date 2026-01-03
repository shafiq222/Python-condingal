Word = input("pls enter a word k")
char = input("pls enter a word")

i=0
count=0

while i<len(Word):
    if Word[i] == char:
        count=count+1
    i=i+1
print("ur letter has bee printed this times ",count)