import numpy as np

binary_string = "010000000111111010111001"
#exponent = "10000000111"
#mantisa_portion ="111010111001"

# Extract the sign bit
sign = 1 if binary_string[0] == '1' else 0

# Extract the exponent bits
exponent_bits = binary_string[1:12]
exponent = int(exponent_bits, 2) - 1023
x =int(exponent_bits, 2)

# Calculate the decimal value
#decimal_value = ((-1)**sign) * (2**exponent)

# Calculating the mantisa
# Raised (1/2) to the indeces of the mantisa

# mantisa string
mantisa_string = binary_string[12:]
# made it into a list
mantisa_list = [i for i in mantisa_string]

# A formula to find the indices of each 1
def find_indices(list_to_check, item_to_find):
    array = np.array(list_to_check)
    indices = np.where(array == item_to_find)[0]
#   added 1 becasue indices start at 0
    return list(indices+1)

#   mantisa exponents
mantisa_exponents = find_indices(mantisa_list, '1')
#print(mantisa_exponents)

# this is 1*(1/2)^indices
onehalf_to_mantisa_exp = [1*(1/2)**x for x in mantisa_exponents]

#print(str(onehalf_rasied))

#   f
f = sum(onehalf_to_mantisa_exp)

#   solution
decimal_value = ((-1)**sign) * (1 + f) * (2**exponent)

decimal_format = format(decimal_value, '.5f')

solution_1 = decimal_format
#   prints solution with 5 decimal places
print(solution_1)
print()

# ===========
# Question 2
# ===========

#   find the index of the decimal point
decimal_index = solution_1.index(".")

#   string to float for computation
solution_1_type_float = float(solution_1)

#   output is 0.4915625
normalized_number = solution_1_type_float / (10**(decimal_index))

#   string for chopping
normalized_number = str(normalized_number)

#   location of decimal
normalized_index = normalized_number.index('.')
#print('normalized index:', normalized_index)
# k is 3 for k-digit floating point value
k = 3
#   index+1 becasue index starts at 0
chopping_normilized = normalized_number[0: (normalized_index + 1) + k]
#print('chopping normilized:', chopping_normilized)

#   I used float in this case becasue with other values it could have decimals
#   output is 461.0
chopping_value = float(chopping_normilized) * 10**decimal_index
#print('chopping value:', chopping_value)

#   converted it into an intiger since it's a whole number:
print(int(chopping_value))

# ===========
# Question 3
# ===========

#solution_1_type_float = float(solution_1)
#normalized_number = solution_1_type_float / (10**(decimal_index))
#   I was really tempted to just use round()


a = (normalized_index + 1) + k
b = a + 1
x = normalized_number
x_string = str(x)
place_holder = normalized_number[0: 6]


# here

rounding = float(place_holder) + 0.0005
print('rounded: ',rounding)
rounding_value = rounding * 10**decimal_index
print('rounding value: ', rounding_value)

# ===

normalized_indices = normalized_number[0:]
print('indeces: ', normalized_indices)



print('placeholder: ', place_holder)

print('normalized number: ', normalized_number)
print('a: ', a)


def custom_round_python(number, decimal_places):
    # Multiply the number by 10 raised to the power of the number of decimal places
    number *= 10**decimal_places
    # Check if the number needs to be rounded up or down
    if number - int(number) >= 0.5:
        number += 0.5
    else:
        number = int(number)
    # Divide the number by 10 raised to the power of the number of decimal places
    number /= 10**decimal_places
    return number

# Example usage
rounded_number = custom_round_python(0.4915625, 3)
print(rounded_number)

#===
#Question 6
#===



def check_for_alternating(function_we_got: str):
    term_check = check_for_negative_1_exponent_term(function_we_got)
    return term_check
def check_for_decreasing(function_we_got: str, x: int):
    decreasing_check = True
    k = 1
    starting_val = abs(eval(function_we_got))
    for k in range(2, 100):
        result = abs(eval(function_we_got))
        #print(result)
        if starting_val <= result:
            decreasing_check = False
    return decreasing_check
def check_for_negative_1_exponent_term(function: str) -> bool:
    if "-1**k" in function:
        return True
    return False

# this par for question 4
def absolute_error(precise:float, approximate: float):
    sub_operation = precise - approximate
    return abs(sub_operation)
def relative_error(precise:float, approximate: float):
    sub_operation = absolute_error(precise, approximate)
    div_operation = sub_operation / precise
    return div_operation
if __name__ == "__main__":
    # print(absolute_error())
    # print(relative_error())
    x: float = 4/9
    y: float = 1/3
    z: float = 7/3
    precise_val: float = (x - y) * z
    #print(absolute_error(precise_val, .259))
    #print(relative_error(precise_val, .259))
    
    # ====
    # Quesion 5 answer
    # ====
    
    ' section 1.3 '
    ' minimum of terms needed to computer f(1) with error 10^-6'
    ' pre reqs'
    function_a: str = "(-1**k) * (x**k) / (k**3)"
    x: int = 1
    check1: bool = check_for_alternating(function_a)
    check2: bool = check_for_decreasing(function_a, x)
    #print(check1 and check2)
    if check1 and check2:
        n = np.cbrt(10**4) - 1
        round_up_n = np.ceil(n)
        print('use function a and round up n =', round_up_n)
    #    use_minimum_term_function(function_a)