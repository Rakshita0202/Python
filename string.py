#initialise
s = 'Rakshita'
print(type(s))

#How to access the characters from the string
#sequence of characters
s = 'vansh'
print(s[0])
print(s[1])
print(s[2])
print(s[3])
print(s[4])

#for printing last character or accessing single element
s = 'pineapple'
print(s[len(s)-1]) #1st method
print(s[-1]) #2nd method

#If we have to access multiple characters
#string to substring , it is known as slicing
s = 'pineapple'
print(s[0:4])
#String slicing : It is the process of extracting the 
#substring from the string in which we decide the
#starting index of the particular substring
#and ending index of the substring
#syntax s = 'Rakshita'
#s[start_idx : end_idx : step] -> start_idx -> inclusive
#end_idx -> exclusive

s = 'APPLE'
print(s[0:3]) #APP
print(s[0:]) #it will print full
print(s[ :3]) #By default it will print fom start (APP)
print(s[:]) #it will print full

#for steps
s = 'pineapple'
print(s[0::2]) #pnape
print(s[-8:])
print(s[-7:-9:-1])

#right se left -> -ve step(-1)
#left se right -> +ve step(+1)


text = "DataScienceWithPython"
# Character positions for reference:
#  D  a  t  a  S  c  i  e  n  c  e  W  i  t  h  P  y  t  h  o  n
#  0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20
#-21-20-19-18-17-16-15-14-13-12-11-10 -9 -8 -7 -6 -5 -4 -3 -2 -1

text = "DataScienceWithPython"

# Positive Indexing
print(text[0:4])  # Output: Data Q1
print(text[4:11])  # Output: Science Q2
print(text[11:15])  # Output: With Q3
print(text[15:21])  # Output: Python Q4
print(text[4:15])  # Output: ScienceWith Q5
print(text[:10])  # Output: DataScienc Q6
print(text[5:16])  # Output: cienceWithP Q7
print(text[4:])  # Output: ScienceWithPython Q8
print(text[:15])  # Output: DataScienceWith Q9
print(text[:])  # Output: DataScienceWithPython Q10


text = "DataScienceWithPython"
# Character positions for reference:
#  D  a  t  a  S  c  i  e  n  c  e  W  i  t  h  P  y  t  h  o  n
#  0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20
#-21-20-19-18-17-16-15-14-13-12-11-10 -9 -8 -7 -6 -5 -4 -3 -2 -1

# Negative Indexing
print(text[-6:])  # Output: Python Q11
print(text[-10:-6])  # Output: With Q12
print(text[-17:-10])  # Output: Science Q13
print(text[-5:])  # Output: ython Q14
print(text[-10:])  # Output: WithPython Q15
print(text[:-7])  # Output: DataScienceWithP Q16
print(text[-11:])  # Output: nceWithPython Q17
print(text[-1])  # Output: n Q18
print(text[-2])  # Output: o Q19
print(text[-21:])  # Output: DataScienceWithPython Q20

# Step Slicing
print(text[0::2]) #print every 2nd character Q21
print(text[0::3]) #print every 3rd character Q22
print(text[1::2]) #print every alternate character from index 1 Q23
print(text[0::4]) #print every 4th character Q24
print(text[::-1]) #reverse the complete string Q25
print(text[:-7:-1]) #Reverse only "Python" Q26
print(text[-11:-18:-1]) #Reverse only "Science" Q27
print(text[::-2]) #print every 2nd character in reverse order Q28
print(text[::-3]) #print every 3rd character in reverse order Q29
print(text[::-2]) #print the string from the end t the beginning by skipping one character each time Q30

#Mixed positive and negative indexing
print(text[4:-10]) #Extract "Science" using one positive index and one negative index. Q31
print(text[-10:21]) #Extract "WithPython" using positive indexing for the start and negative indexing for the stop. Q32
print(text[-17:15]) #Extract "ScienceWith" using negative indexing for the start and positive indexing for the stop. Q33
print(text[12:-5]) #Extract "ithP" using mixed indexing. Q34
print(text[4:-1]) #Extract everything from "S" to the second-last character using mixed indexing. Q35
print(text[1:-1]) #Extract all characters except the first and last character using mixed indexing. Q36
print(text[5:-6]) #Extract the middle 10 characters using mixed slicing. Q37
print(text[5:-3]) #Extract "cienceWithPyt" using mixed indexing. Q38
print(text[14:10:-1]) #Extract only "With" in reverse order. Q39
#Q40 Without using any string methods or loops, write slicing expressions to produce the following outputs:
# 1. Data
# 2. Science
# 3. Python
# 4. nohtyP
# 5. DataScience
# 6. WithPython
# 7. DataWith
# 8. Every alternate character
# 9. Every alternate character in reverse
# 10. The complete string except the first and last two characters
print(text[:4]) #1
print(text[4:11]) #2
print(text[15:]) #3
print(text[:-7:-1]) #4
print(text[:11]) #5
print(text[11:]) #6
print(text[:4]+text[11:15]) #7
print(text[::2]) #8
print(text[::-2]) #9
print(text[2:-2]) #10


#String formatting
name = 'Rakshita'
age = 21
sent = f"My name is {name}. My age is {age}."
print(sent)

#Dot format
sent = "My name is {}. My age is {}.".format(name,age)
print(sent)

#index based format
sent = "My name is {1}. My age is {0}.".format(age, name)
print(sent)

#+,*
#String operators
first_name = 'Rakshita'
last_name = 'Rathi'
full_name = first_name +' '+ last_name
print(full_name)

print('Rakshita' * 100)

#Membership operator
text = 'This is a sentence.'
print('@' in text)
print('t' in text)

#How to iterate over the strings
#in c
# for (int i = 0;i<=5;i++){
#     execution
# }

#in python
# range(start,end,step)
# start -> inclusive
# end -> exclusive
for i in range(0,6):
    print(i)

s = 'This is a sentence.'
for i in range (0,len(s)):
    print(s[i])

#2nd method to iterate by using membership operator
for ch in s:
    print(ch)
