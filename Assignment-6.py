#Python program which checks whether the given input is palindrome or not
str = input("Enter a string:::")
j = -1
flag = 0
for i in str:
	if i != str[j]:
		flag = 1
		break
	j = j - 1
try:
   if flag == 1:
       print(str," is not a palindrome")
   else:
	    print(str," is a palindrome")
except TypeError:
   print("TypeError:Invalid input\n\tPlease re-check")