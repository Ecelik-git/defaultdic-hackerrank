from collections import defaultdict

n, m = map(int, (input().split()))
#putting m words in first list
word_list1 = [input() for i in range(n)]
#putting n wwords in second list
word_list2 = [input() for i in range(m)]
#creating default dic
d= defaultdict(list)
index=0
#adding first list elements to dic
for i in word_list1:
    d[i].append( word_list1.index(i, index) + 1)
    index+=1
#if second list lements in dic, print the number
for i in word_list2:
    if i not in word_list1:
        print(-1)
    else:
        print(" ".join(map(str, d[i])))
