def fizzbuzz(int):
    if int%5==0:
        if int%3==0:
            return "FizzBuzz"
        else:
            return "Buzz"
    elif int%3==0:
        return "Fizz"
    else:
        return int

arr=[]
for i in range(3):
    a=input()
    if a.isdecimal()==True:
        if i==0:
            result=fizzbuzz(int(a)+3)
        elif i==1:
            result=fizzbuzz(int(a)+2)
        else:
            result=fizzbuzz(int(a)+1)
        
    else:
        pass
print(result)