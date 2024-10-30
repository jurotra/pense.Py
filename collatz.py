
print("Let's use the Collatz Conjecture!\n")

n = int(input("Enter a number to use in Collatz: \n"))

result=[n]

def collatz_number(n):

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


print("This is the collatz values for ther number", n, ":\n", collatz_number(n))

time = list(range(len(result))) 

print("\nAnd this how many steps the collatz take to find the number 1:\n", time)






