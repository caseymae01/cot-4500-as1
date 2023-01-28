import numpy as np

def zeros_to_append(number_string):
    zeros_to_add = 64 - len(number_string)
    new_number = number_string + ("0" * zeros_to_add)
    return new_number


def double_precision(new_number, decimals):
    num = int(new_number[0])

    exponent = 0
    for index in range(1, 12):
        exponent = exponent + (int(new_number[index]) * 2 ** (11 - index))

    fraction = 0
    for index in range(12, 64):
        fraction = fraction + (int(new_number[index]) * (1 / 2) ** (index - 11))

    final = np.float64(((-1) ** num) * (2 ** (exponent - 1023)) * (1 + fraction))

    format_specs = "." + str(decimals) + "f"
    end_result = format(final, format_specs)

    return end_result


def chopping(chopped_number, digit):
    format_specs = "." + str(digit) + "f"
    end_result = format(chopped_number, format_specs)

    return end_result


def rounding(rounded_number, digit):
    new_num = rounded_number + (10 ** (-1 * (digit + 1))) * 5
    format_specs = "." + str(digit) + "f"
    end_result = format(new_num, format_specs)
    return end_result


def abs_error(exact_number, rounded):
    absolute = np.absolute(exact_number - rounded)
    return absolute


def rel_error(exact_number, rounded):
    relative = np.absolute((exact_number - rounded) / exact_number)
    return relative


def check_for_negative_1_exponent_term(function) -> bool:
    if "-1**k" in function:
        return True
    return False


def check_for_alternating(function):
    term_check = check_for_negative_1_exponent_term(function)
    return term_check


def check_for_decreasing(function, x):
    decreasing_check = True
    k = 1

    starting_val = abs(eval(function))
    for k in range(1, 75):
        result = abs(eval(function))

        if starting_val < result:
            decreasing_check = False
    return decreasing_check


def minimum_term(error):
    counter = 0
    while (1 / (counter + 1) ** 3) > error:
        counter = counter + 1

    print(counter)


def bisection_method(left, right, given_function, tolerance):

    def f(x):
        f = eval(given_function)
        return f

    error = abs(right - left)
    iteration_counter = 0

    while error > tolerance:
        mid_point = (right + left) / 2

        if f(left) * f(right) >= 0:
            print("Cannot use bisection method in this case.")
            break

        elif f(mid_point) * f(left) < 0:
            right = mid_point
            error = abs(right - left)
            iteration_counter += 1

        elif f(mid_point) * f(right) < 0:
            left = mid_point
            error = abs(right - left)
            iteration_counter += 1

    print(iteration_counter)


def function(value):
    return (value ** 3) + (4 * (value ** 2)) - 10


def custom_derivative(value):
    return (3 * value ** 2) + (8 * value)


def newton_raphson(initial_approximation, tolerance, sequence):
    iteration_counter = 0
    x = initial_approximation
    f = eval(sequence)
    f_prime = custom_derivative(initial_approximation)

    approximation: float = f / f_prime
    while abs(approximation) >= tolerance:
        x = initial_approximation
        f = eval(sequence)
        f_prime = custom_derivative(initial_approximation)
        approximation = f / f_prime
        initial_approximation -= approximation
        iteration_counter += 1

    print(iteration_counter)


def main():
    # Question 1
    number_string = "010000000111111010111001"
    new_number = zeros_to_append(number_string)
    decimals = 5
    end_result = double_precision(new_number, decimals)
    print(end_result)
    print("")

    end_result = np.double(end_result)

    # Question 2
    new_chopped_number = chopping(end_result, 0)
    print(new_chopped_number)
    print("")

    # Question 3
    new_rounded_number = rounding(end_result, 0)
    print(new_rounded_number)
    print("")

    new_rounded_number = np.double(new_rounded_number)

    # Question 4
    print(abs_error(end_result, new_rounded_number))

    print(rel_error(end_result, new_rounded_number))
    print("")

    # Question 5
    function = "(-1**k) * (x**k) / (k**3)"
    x = 1
    check1: bool = check_for_alternating(function)
    check2: bool = check_for_decreasing(function, x)

    error = 10 ** -4
    if check1 and check2:
        minimum_term(error)

    print("")

    # Question 6
    # PART A BISECTION
    left = -4
    right = 7
    tolerance = .0001
    function_string = "x**3 + (4*(x**2)) - 10"
    bisection_method(left, right, function_string, tolerance)
    print("")

    # PART B NEWTON
    initial_approximation = -4
    tolerance = .0001
    sequence = "x**3 + (4*(x**2)) - 10"
    newton_raphson(initial_approximation, tolerance, sequence)


if __name__ == "__main__":
    main()
