from collections import Counter
result=[]
while(1):
    a=input()
    leftstack=[]
    rightstack=[]
    if a=='.':
       break
    arr=[text for text in a if text=='[' or text==']' or text==')' or text=='(']

    counts= Counter(arr)

    if counts['(']!=counts[')'] or counts['[']!=counts[']']:
        result.append('no')
    else:
        # left=list(filter(lambda x:arr[x] =='(', range(len(arr))))
        # right=list(filter(lambda x:arr[x] ==')',range(len(arr))))
        # left_=list(filter(lambda x:arr[x] =='[', range(len(arr))))
        # right_=list(filter(lambda x:arr[x] ==']', range(len(arr))))

        # if 
        #     result.append('no')
        # else:    
        #     result.append('yes')
        isbool=True
        for kkomi in arr:
            if kkomi == '(' or kkomi=='[':
                leftstack.append(kkomi)
            else:       #) ]
                if len(leftstack)==0:
                    result.append('no')
                    isbool=False
                    break
                pops=leftstack.pop()
                if (pops!='(' and kkomi==')') or (pops!='[' and kkomi==']'):
                    result.append('no')
                    isbool=False
                    break
        if len(leftstack)==0 and isbool==True:
            result.append('yes')

for a in result:
    print(a)
