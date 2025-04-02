def anagramcheck(str1, str2):
    if(sorted(str1)==sorted(str2)):
        return True
    else:
        return False

str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

if(anagramcheck(str1, str2)):
    print("The strings are anagrams")
else:
    print("The strings are not anagrams")