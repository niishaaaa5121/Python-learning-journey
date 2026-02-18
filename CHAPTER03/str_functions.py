name = "innisha kumari"

print(len(name))   #this will give the length of the string 
print(name.upper())   #this will convert the string to uppercase
print(name.lower())   #this will convert the string to lowercase  
print(name.capitalize())   #this will capitalize the first letter of the string
print(name.title())   #this will capitalize the first letter of each word in the string
print(name.count("i"))   #this will count the number of times the letter "i" appears in the string
print(name.find("i"))   #this will return the index of the first occurrence of the letter "i" in the string
print(name.find("a"))   #this will return -1 because the letter "z" is not in the string
print(name.replace("i", "a"))   #this will replace all occurrences of the letter "i" with the letter "a" in the string
print(name.replace("n", "m", 1))   #this will replace the first occurrence of the letter "n" with the letter "m" in the string      
print(name.replace("n", "m", 2))   #this will replace the first two occurrences of the letter "n" with the letter "m" in the string but since there is only one occurrence of the letter "n" it will replace that one occurrence and ignore the second occurrence which does not exist in the string  
print(name.endswith("ari"))   #this will return True because the string ends with "ari"
print(name.endswith("kumari"))   #this will return True because the string ends with "kumari"
print(name.startswith("Inn"))   #this will return True because the string starts with "innisha"
print(name.startswith("inn"))   #this will return True because the string starts with "innisha" 

# index means the position of that letter

#  we can use chatgpt to get ore string functions, thes e are some basic ones so no nedd to learn it all by heart just know that there are many string functions available and you can use them to manipulate strings in different ways.
