def matchwords(words):
    ctr=0
    lst=[]
    for word in words:
        if len(word)>1 and word[0]==word[-1]:
            ctr+=1
            lst.append(word)
    print("List of words with first and last character same:",lst)
    return ctr
count=matchwords(['abc','cfc','xyz','aba','1221'])    
print("Number of words having first and last character same:",count)
  
