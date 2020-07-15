#Demonstrate the usage of lambda function

ftemps=[32,65,100,212]
ctemps=[0,12,34,100]

# Convert Fahrenheit to Celsius and 

print(list(map(lambda t:(t-32)*5/9,ftemps)))
print(list(map(lambda t:(t*9/5)+32,ctemps)))