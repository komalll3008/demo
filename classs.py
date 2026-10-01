#demo of all basic commands
# print("lets start the fun")
# print("Welcome "," Just enjoy",sep="&")
# print("1","2","3","4","5",sep="@")

#sumof1st10evennos

# sum=0
# for i in range(1,21):
#     if(i%2==0):
#         sum=i+sum
# print(sum)


#accept s and n ,print sq of first n nos starting from s

# s=int(input("enter s: "))
# n=int(input("enter n: "))
# for i in range(s,n+1):
#     sq=i*i
#     print(sq)

#reverse the string

# a=input("enter the string: ")
# print("reverse",a[::-1])



#accept sentence and count vowels

# a=input("enter the sentence: ")
# def count_vowels(s):
#     count = 0
#     for i in s:
#         if i in "aeiouAEIOU":
#             count += 1
#     return count
# print("countes no of vowels: ",count_vowels(a))



#remove duplicates from list

# a = ['apple', 'banana', 'apple', 'papaya']
# b = []
# for i in a:
#     if i not in b:
#         b.append(i)

# print(b)



#reverse the list

# a=['a','b','c','d']
# print("reversed list: ",a[::-1])



#prit the pattern of*

# for i in range(1,6):
#     for j in range(1,i):
#         print("*", end=" ")
#     print()


#pyramid of*
# n=5
# for i in range(n):
#     for j in range(n-i):
#         print("",end=" ")
#     for k in range(i):
#         print("*", end=" ")
#     print()

