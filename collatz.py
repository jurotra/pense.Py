
print("Let's use the Collatz Conjecture!\n")

def collatz_number(n):

    result = [n]

    while True:  # condition for stopping the function
        if n % 2==0: #even
            n = n // 2
            result.append(n)
        elif n % 2!=0 or n!=1: #odd
            n = n*3+1
            result.append(n)
        else: 
            break
     
    print(result)
    


n = int(input("Enter a number to use in Collatz: "))
collatz_number(n)


