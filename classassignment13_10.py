#wap to read a file and count vowels in that file

# count=0
# with open('abc.txt','r') as file:
#     content =file.read()
#     for ch in content:
#         if ch.lower() in "aeiou":
#             count+=1
# print('total no of vowels:',count)


#read all lines from a file into a list .print a total no of lines and display the 2nd and 4th line

# f = open("abc.txt", "r")
# lines = f.readlines()
# f.close()

# print("Total number of lines:", len(lines))
# print("2nd line:", lines[1], end="")
# print("4th line:", lines[3], end="")




#take a sentence from a user, split it into words and store them into list print the longest word

# s = input("Enter a sentence: ")
# words = s.split()
# longest = max(words, key=len)
# print("Longest word:", longest)



#read a file ,split its content into words and store them into list 
#i. print the total no of words
#ii. print all unique words

f = open("abc .txt", "r")
words = f.read().split()
f.close()
print("Total number of words:", len(words))
print("Unique words:", set(words))

