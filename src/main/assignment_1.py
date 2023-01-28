import numpy as np
from decimal import Decimal

# ===========
# Question 1
# ===========

binary_string = "010000000111111010111001"
# exponent = "10000000111"
# mantisa_portion ="111010111001"

# The sign portion
sign = 1 if binary_string[0] == '1' else 0

# The exponent portion
exponent_bits = binary_string[1:12]
exponent = int(exponent_bits, 2) - 1023
x =int(exponent_bits, 2)

# mantisa string
mantisa_string = binary_string[12:]
# made it into a list
mantisa_list = [i for i in mantisa_string]

# A formula to find the indices of each 1
def find_indices(checking_mantisa_list, finding_1s):
    array = np.array(checking_mantisa_list)
    indices = np.where(array == finding_1s)[0]
#   added 1 becasue indices start at 0
    return list(indices+1)

# mantisa exponents
mantisa_exponents = find_indices(mantisa_list, '1')
#print(mantisa_exponents)

# this is 1*(1/2)^indices
onehalf_to_mantisa_exp = [1*(1/2)**x for x in mantisa_exponents]

#print(str(onehalf_rasied))

# f
f = sum(onehalf_to_mantisa_exp)

# solution
decimal_value = ((-1)**sign) * (1 + f) * (2**exponent)

decimal_format = format(decimal_value)

# Soltution 1
solution_1 = decimal_format
#print(solution_1)

# ===========
# Question 2
# ===========

# find the index of the decimal point
decimal_index = solution_1.index(".")

# string to float for computation
solution_1_type_float = float(solution_1)

# output is 0.4915625
normalized_number = solution_1_type_float / (10**(decimal_index))

# string for chopping
normalized_number = str(normalized_number)

# location of decimal
normalized_index = normalized_number.index('.')
#print('normalized index:', normalized_index)

# k is 3 for k-digit floating point value
k = 3
# index+1 becasue index starts at 0
chopping_normilized = normalized_number[0: (normalized_index + 1) + k]
#print('chopping normilized:', chopping_normilized)

# I used float in this case becasue with other values it could have decimals
chopping_value = float(chopping_normilized) * 10**decimal_index
#print('chopping value:', chopping_value)

# print('Chopping normilized: ', chopping_normilized)
#print(chopping_value)

# ===========
# Question 3
# ===========

#   I was really tempted to use round()

# custom rounding method 
a = (normalized_index + 1) + k
b = a + 1
x = normalized_number
x_string = str(x)
place_holder = normalized_number[0: 6]

# add's 5 to the number after the 3rd term
rounding = float(place_holder) + 0.0005

rounding_value = rounding * 10**decimal_index
#print(rounding_value)


# ===========
# Question 4
# ===========

# Preliminary before calculations
rounding_value_decimal = Decimal(rounding_value)
solution_1_decimal = Decimal(solution_1_type_float)

# Absolute Error:
abs_error = abs(rounding_value_decimal - solution_1_decimal)
#print(abs_error)

# Relative Error:
relative_err = abs(rounding_value_decimal - solution_1_decimal) / abs(solution_1_decimal)
#print(str(f'{relative_err:.31f}'))


# ===========
# Question 5
# ===========

# Check for alternating
def check_for_alternating(function_we_got: str):
    term_check = check_for_negative_1_exponent_term(function_we_got)
    return term_check
# Check for decreasing
def check_for_decreasing(function_we_got: str, x: int):
    decreasing_check = True
    k = 1
    starting_val = abs(eval(function_we_got))
    for k in range(2, 100):
        result = abs(eval(function_we_got))
        if starting_val <= result:
            decreasing_check = False
    return decreasing_check
def check_for_negative_1_exponent_term(function: str) -> bool:
    if "-1**k" in function:
        return True
    return False


# ===========
# Question 6
# ===========

# part a
def bisection_method(left: float, right: float, given_function: str):
# checking if right and left function changes signs
    x = left
    intial_left = eval(given_function)
    x = right
    intial_right = eval(given_function)
    if intial_left * intial_right >= 0:
        print("Invalid inputs. Not on opposite sides of the function")
        return
    tolerance: float = 0.0001
    diff: float = right - left


    bisection_iteration_counter = 0
    while (diff >= tolerance and bisection_iteration_counter <= 20):
        bisection_iteration_counter += 1
        # find function(midpoint)
        mid_point = (left + right) / 2
        x = mid_point
        evaluated_midpoint = eval(given_function)
        if evaluated_midpoint == 0.0:
            break
        
        # find function(left)
        x = left
        evaluated_left_point = eval(given_function)
        
        # checks is orgin point has been crossed
        first_conditional: bool = evaluated_left_point < 0 and evaluated_midpoint > 0
        second_conditional: bool = evaluated_left_point > 0 and evaluated_midpoint < 0
        if first_conditional or second_conditional:
            right = mid_point
        else:
            left = mid_point
        
        diff = abs(right - left)
        # prints each iteration
        #print(mid_point)
    # prints the number of iterations
    print(bisection_iteration_counter, end='\n\n')

# part b newton raphson method

# manual derivative
def custom_derivative(value):
    return (3 * value* value) + (8 * value)
def newton_raphson(initial_approximation: float, tolerance: float, sequence: str):
    iteration_counter = 0
    # finds f
    x = initial_approximation
    f = eval(sequence)
    # finds f' 
    f_prime = custom_derivative(initial_approximation)
    
    approximation: float = f / f_prime
    while(abs(approximation) >= tolerance):
        # finds f
        x = initial_approximation
        f = eval(sequence)
        # finds f' 
        f_prime = custom_derivative(initial_approximation)
        # division operation
        approximation = f / f_prime
        # subtraction property
        initial_approximation -= approximation
        iteration_counter += 1
    return iteration_counter

if __name__ == "__main__":
    # Answers to Assignment 1:
    
    # Answer 1
    print(solution_1_type_float, end='\n\n')

    # Answer 2
    print(chopping_value, end='\n\n')

    # Answer 3
    print(rounding_value, end='\n\n')

    # Answer 4
    # Absolute Error:
    print(abs_error, sep='\n\n')
    # Relative Error:
    print(str(f'{relative_err:.31f}'), end='\n\n')

    # Answer 5
    function_a: str = "(-1**k) * (x**k) / (k**3)"
    x: int = 1
    check1: bool = check_for_alternating(function_a)
    check2: bool = check_for_decreasing(function_a, x)
    # print(check1 and check2)
    # Check 1 and Check 2 passed therefore we can check iterations
    if check1 and check2:
        n = np.cbrt(10**4) - 1
        # rounds up n
        round_up_n = np.ceil(n)
        # use function a and round up n = num
        print(int(round_up_n), end='\n\n')

    # Answer 6 (a) Bisection Method
    left = -4
    right = 7
    function_string = "x**3 + (4*(x**2)) - 10"
    bisection_method(left, right, function_string)

    # Answer 6 (b) newton raphson method
    initial_approximation: float = (7-(-4))/2
    tolerance: float = .0001
    sequence: str = "x**3 + (4*(x**2)) - 10"
    iteration_counter = newton_raphson(initial_approximation, tolerance, sequence)
    print(iteration_counter, end='\n\n')
    
