f = open("coding_qual_input.txt", "r")
dict = {}
for line in f:
    listy = line.split()
    dict.update({int(listy[0]):listy[1]})

maxKey = max(dict.keys())
phrase  = ""
j = 1
i = 1

while (i<=maxKey):
    for i in range (i,i+j):
        print(i, end =" ")
        if(i==(j*(j+1))/2):
            phrase += dict[i]+ ' ' 
        i+=1
    print()
    j+=1    


print()
print(phrase)




