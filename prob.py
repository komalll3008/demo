# n=int(input("enter the number: "))
# count =0
# while n>0:
#     n=n//10
#     count+=1
#     print("digits in given number: ",count)

# n=int(input("enter the num: "))
# while n!=0:
#     di=n%10
#     print(di,end="")
#     n=n//10
class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        temp=x
        rev=0
        while x>0:
            digit=x%10
            rev=rev*10+digit
            x=x//10
            return temp==rev