templist = ['3', '5', '7' ,'9','11','13','15','17','19']
templist2 = ['4', '6', '8' ,'10','12','14','16','18','20']
wordlist=[]

# wordlist.append(templist)
for i in range(len(templist)):
    wordlist.append(templist[i])
templist2.reverse()
for i in range(len(templist2)):
    wordlist.append(templist2[i])
print('\n'.join(wordlist))
# for i in range(3,20,2):
#     print(i)
# wordlist.append(templist)
# wordlist.append(templist2)
# print(wordlist)