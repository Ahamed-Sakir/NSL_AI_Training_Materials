# String concatenation
str1 = 'Sakir'
str2 = 'Ahamed'
print(str1 + " " + str2)

# String Repetition
repetition = "Bangladesh "
print(repetition * 3)

# Some important function
# Join
elements = ['first', 'second', 'third']
join_elements = ','.join(elements)
print(join_elements)
print('Find out different between these two prints')
print(elements)

# Replace
str3 = 'Sakir Ahamed'
new_str3 = str3.replace('Sakir Ahamed', 'Ahamed Sakir')
print(f'You name is changed {str3} to {new_str3}')

# Upper case
print('This is bangladesh'.upper())

# Lower case
print('THis is Lowercase'.lower())

# Split
together_string = "My name is sakir Ahamaled. I love to do code. I live in Bangladesh"
individual_words = together_string.split(" ")
print(individual_words)


print("This is a sentence.".startswith("This"))
print("This is a sentence.".endswith("."))


