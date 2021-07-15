# To open file
file_variable = open('file.txt')
file_variable.close()
# Open file in write mood
file_variable_w = open('file.txt', 'w')

file_variable_w.close()
# Open file in read mood
file_variable_r = open('file.txt', 'r')
content = file_variable_r.read()
print(content)
file_variable_r.close()
# Open file in insert mood
file_variable_a = open('file.txt', 'a')
file_variable_a.close()

# Another best way
with open('file.txt') as f:
    print(f.read())
    f.close()
