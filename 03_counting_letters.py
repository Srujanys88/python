sentence = input("Enter the sentence : ")
words = sentence.split(" ")
num_words = 0
num_digits = 0
num_uc = 0
num_lc = 0
for word in words:
    num_words+=1
    for char in word:
        if char.isdigit():
            num_digits+=1
        elif char.isupper():
            num_uc +=1
        elif char.islower():
            num_lc +=1
print("words = ",num_words, ", digits= ",num_digits,", uc = ",num_uc, ", lc = ",num_lc)

