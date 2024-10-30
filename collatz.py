
print("Let's use the Collatz Conjecture!\n")

def collatz_number(n):

    result = [n]

    while True:  # condition for stopping the function
        if n % 2==0: #even
            n = n // 2
            result.append(n)
        elif n<=1:
            break
        else:
            n = n*3+1
            result.append(n)
         
    return result


n = int(input("Enter a number to use in Collatz: "))
print(collatz_number(n))





