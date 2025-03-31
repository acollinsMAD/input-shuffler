#Starts with getting user input for either numbers or words
user_input = input("Please enter either numbers or words: ")

#repeats this step to create a second array
user_input2 = input("Please enter either numbers or words: ")

#if the user enters numbers, converts it to an array of integers
if user_input.isdigit():
    user_input = list(map(int, user_input))
    
#If the user enters words, converts it to an array
elif user_input.isalpha():
    user_input = list(user_input)
    
#If the user enters neither, prints an error message
else:
    print("Invalid input")
    
#repeats the process for the second array
if user_input2.isdigit():
    user_input2 = list(map(int, user_input2))
    
elif user_input2.isalpha():
    user_input2 = list(user_input2)

    
#If the user enters neither, prints an error message
else:
    print("Invalid input")
    
#combines the two arrays, with the first value in the first array first, then the first value in the second array, and so on. If they're different lengths, it adds the excess to the end of the combined array
combined = []
for i in range(max(len(user_input), len(user_input2))):
    if i < len(user_input):
        combined.append(user_input[i])
    if i < len(user_input2):
        combined.append(user_input2[i])
        
print(combined)