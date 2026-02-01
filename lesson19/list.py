def match_words(words):
    cont = 0
    lst = []
    for words in words:
        if len(words)>1 and words[0]  == words[-1]:
            cont = cont + 1
            lst.append(words)
    print("List of 1st and last character same thing",lst)
    return cont
w = match_words(["aba","cbc","xyz","abc","1221"])
print("Number of 1st and last character same thing",w)