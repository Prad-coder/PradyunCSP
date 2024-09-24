string = "Brawl Stars is a fun game!"
string2 = "Tacocat"
print("String 1: Brawl Stars is a fun game!")
length = len(string)
print("Length:", length)
def count_vowels(input_string):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in input_string:
        if char in vowels:
            count += 1
    return count
print("Vowel Count:", count_vowels(string))
def average_word_length(input_string):
    words = input_string.split()
    if not words:
        return 0
    total_length = sum(len(word) for word in words)
    average_length = total_length / len(words)
    return average_length
print("Average Word Count:", average_word_length(string))
def palindrome(input_string):
    string = input_string.replace(" ","").lower()
    return string == string[::-1]
print("Palindrome or Not?", palindrome(string))
print("String 2: Tacocat")
length2 = len(string2)
print("Length:", length2)
print("Vowel Count:", count_vowels(string2))
print("Average Word Count:", average_word_length(string2))
print("Palindrome or Not?", palindrome(string2))