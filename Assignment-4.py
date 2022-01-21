#program to print prime numbers till the given number
n=int(input("Enter the number for which till you want to print primes:"))#Takes input from the user to know the maximum value
primes=[]#empty list which is going to be filled with primes
for i in range(2,n+1):#this for loop iterates in range (2->n+1)
    for j in range(2,i):#this for loop iterates in range (2->i)
        if(i%j==0):#this statement checks for the prime condition
            break
    else:#this executes if the number is prime
        primes.append(i)#the prime number will be added to the pre-defined list primes
print("\nThe prime numbers till the given number are:",primes)