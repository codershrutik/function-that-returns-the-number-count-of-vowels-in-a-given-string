str = input("Enter a string value: ")

def count_vowels(str):
    vowels = "aeiouAEIOU"
    count = 0
    for c in str:
        if c in vowels:
            count += 1
    return count;

print(count_vowels(str))