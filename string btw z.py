
input_str = "3Haaris"

n = int(input_str[0])  
name = input_str[1:]  

output_str = name[0] 


for i in range(1, len(name)):
    if i % n == 0:  # if i is a multiple of n, replace the character with "z"
        output_str += "z"
    else:  
        output_str += name[i]

print(output_str)
