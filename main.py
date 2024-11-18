vowels = input("Enter Your Favourite Vowel: ").lower() 
valid_vowels = {"a", "e", "i", "o", "u"}  

if vowels in valid_vowels:
    print(f"{vowels} is a vowel.")
else:
    print(f"{vowels} is not a vowel.")