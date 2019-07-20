templist = ['3', '5', '7' ,'9','11','13','15','17','19']
templist2 = ['3', '5', '7' ,'9','11','13','15','17','19']
wordlist=[]


for i in range(len(templist)):
    wordlist.append(templist[i])
templist2.reverse()
for i in range(1,len(templist2)):
    wordlist.append(templist2[i])
print(wordlist)
# for i in range(3,20,2):
#     print(i)
# wordlist.append(templist)
# wordlist.append(templist2)
# print(wordlist)