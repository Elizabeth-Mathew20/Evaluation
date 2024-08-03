# def num():
#     s=int(input("enter the number"))
#     n=1
#     a=num
#     if num==0:
#         return 
#     print(num,"is prime") 

#     print(num,"is not a prime")
#     print(num())6
 


# def prime(num):
#     number=int(input("enter the number"))
#     if num<= 1:
#         return False
#     for i in range(2, int(num**0.5) + 1):
#         if num% i== 0:
#             return False
#     return True

# # number=int(input("Enter a number:"))
# if prime(number):
#     print("is a prime number")
# else:
#     print("not a prime number")













def num():
    s=str(input("Enter the string"))
count = 0
for i in s:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
            count+=1
if count==0:
    print("No vowels found")
else:
    print("vowels are:" + str(count))