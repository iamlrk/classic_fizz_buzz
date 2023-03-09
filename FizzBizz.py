# Ramkiran Lepakshi - 22204920
# GitHub - @iamlrk

def is_divisible(divisor, dividend):
    return divisor%dividend == 0

def replace_values_in_dict(dict_keys,dict_values):
    return dict(zip(list(dict_keys.keys()), dict_values))

def key_from_value_dict(dictonary,value):
    return list(dictonary.keys())[list(dictonary.values()).index(value)]

def calculate_fizzbuzz(starting_number,ending_number,**numberx_word):
    numbers=list(range(starting_number,ending_number))
    numbers_dict = dict.fromkeys(numbers, 1)
    temp_numbers_values = ['']*len(numbers)
    
    for i in range(len(numbers)):
        for divisor in numberx_word.values():
            if is_divisible(numbers[i],(divisor)) == True:
                temp_numbers_values[i] = str(temp_numbers_values[i]) + key_from_value_dict(numberx_word, divisor)
    
    # replacing the empty strings temp_numbers_values with the correponding numbers  
    for i in range(len(temp_numbers_values)):
        if temp_numbers_values[i] == '':
            temp_numbers_values[i] = numbers[i]
        
    numbers_dict = replace_values_in_dict(numbers_dict, temp_numbers_values)    
    return numbers_dict

if __name__ == '__main__':
    fizzbuzz_dict = calculate_fizzbuzz(10,46,Fizz=3,Buzz=5)#, Fang = 7, Bang = 11)

    for key,value in fizzbuzz_dict.items():
        print(f'{key}: {value}')