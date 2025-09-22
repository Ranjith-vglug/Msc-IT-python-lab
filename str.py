s=input("Enter the string :")
word=s.split()
Alphabets=0
Digits=0
Special_characters=0
for a in s:
    if a.isalpha():
        Alphabets+=1
    elif a.isdigit():
        Digits+=1
    elif not(a.isalnum() or a.isspace()):
        Special_characters+=1
Lower_case=s.lower()
Upper_case=s.upper()
swap=s.swapcase()
print("The No of words in a String is :",len(word))
print("The No of Alphabets in a String is :",Alphabets)
print("The No of Digits in a String is :",Digits)
print("The No of Special characters is :",Special_characters)
print("The converted string is :",swap)
print("The upper to lower is :",Lower_case)
print("The lower to upper is :",Upper_case)