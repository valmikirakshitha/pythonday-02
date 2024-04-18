#Convert a temperature from celsius to fahrenheit in python

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Example usage:
celsius_temperature = 30
fahrenheit_temperature = celsius_to_fahrenheit(celsius_temperature)
print(f"{celsius_temperature} degrees Celsius is equal to {fahrenheit_temperature} degrees Fahrenheit.")

#Find the second largest element in a list.

def second_largest(lst):
    sorted_list = sorted(lst, reverse=True)
    if len(sorted_list) < 2:
        return "List has fewer than 2 elements."
    else:
        return sorted_list[1]

# Example usage:
my_list = [10, 5, 20, 15, 30]
result = second_largest(my_list)
print("The second largest element in the list is:", result)

#Count the occurrences of each element in a list.

def count_occurrences(lst):
    occurrence_count = {}
    for element in lst:
        if element in occurrence_count:
            occurrence_count[element] += 1
        else:
            occurrence_count[element] = 1
    return occurrence_count

# Example usage:
my_list = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
occurrences = count_occurrences(my_list)
print("Occurrences of each element in the list:")
for element, count in occurrences.items():
    print(f"{element}: {count}")


#Find the sum of all even numbers in a list.

def sum_of_even_numbers(lst):
    total = 0
    for num in lst:
        if num % 2 == 0:
            total += num
    return total

# Example usage:
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = sum_of_even_numbers(my_list)
print("Sum of all even numbers in the list:", result)


#Find the sum of all even numbers in a list.

#def sum_of_even_numbers(lst):
    total = 0
    for num in lst:
        if num % 2 == 0:
            total += num
    return total

# Example usage:
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = sum_of_even_numbers(my_list)
print("Sum of all even numbers in the list:", result)

#Count the number of vowels in a string.

def count_vowels(string):
    vowels = "aeiouAEIOU"
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    return count

# Example usage:
my_string = "Hello, World!"
result = count_vowels(my_string)
print("Number of vowels in the string:", result)

#Reverse the words in a given sentence.

def reverse_words(sentence):
    words = sentence.split()
    reversed_sentence = ' '.join(reversed(words))
    return reversed_sentence

# Example usage:
my_sentence = "Hello world, how are you?"
reversed_sentence = reverse_words(my_sentence)
print("Reversed sentence:", reversed_sentence)


