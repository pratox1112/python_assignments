def mutate_string(str_input,index,char):
    return str_input[:index] + char + str_input[index+1:]
str_input = str(input("Enter the string: "))
index = int(input("Enter the index: "))
char = input("Enter the character to insert: ")
print(mutate_string(str_input,index,char))
