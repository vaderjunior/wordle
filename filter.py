import json
 
f = open('words_dictionary.json')
 
data = json.load(f)
print("success")

size = input('Enter size of word ')

reduced=[ k for k,v in data.items() if len(k)==5 ]
i=1
present=[]
p_len=0
abscent=[]
a_len=0
while i==1:

    present_add=[x for x in input('Enter letters present').split(', ') ]
    present.extend(present_add)
    abscent_add=[x for x in input('Enter letters abscent').split(', ') ]
    abscent.extend(abscent_add)

    for words in reduced:
        if(all((i in words) for i in present)):
            if(all((h not in words) for h in abscent)):
                print(words)
        #for i in range(len(present)):
    ans=input("Continue? y/n \ ")
    if(ans!="y"):
        i=2


#for data in reduced:
