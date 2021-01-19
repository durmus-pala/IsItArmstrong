number = input("Please Enter a positive integer number: ")
number_list = []  
if number.isdigit() == True:
    for i in range(len(number)):
        number_list.append(int(number[i]) ** len(number))
    if sum(number_list) == int(number):
        print(number, "is an Armstrong number")
    else:
        print(number, "is not an Armstrong number")
else:
    print("It is an invalid entry. Don't use non-numric, float or negative values!")
    
    
    


