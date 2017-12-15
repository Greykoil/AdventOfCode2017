# For full puzzle description please see http://adventofcode.com/2017/day/15

#=============================================================================
def run_day_15():
#
#-----------------------------------------------------------------------------
    a_value = 679
    b_value = 771
    a_multiplier = 16807
    b_multiplier = 48271
    dividor = 2147483647
    matches = 0
    checks = 0
    a_values = []
    b_values = []
    last = 1
    while (len(a_values) < 5000000 or len(b_values) < 5000000):
        a_value = (a_value * a_multiplier) % dividor
        b_value = (b_value * b_multiplier) % dividor
        if (a_value % 4 == 0):
            a_values.append(a_value)
            current_a = a_value
        if (b_value % 8 == 0):
            b_values.append(b_value)
        if (min(len(a_values), len(b_values)) > last * 2):
            print(last)
            last *= 2

    for i in range(0, 5000000):
        if (last_16_binary_bits(a_values[i]) == last_16_binary_bits(b_values[i])):
            matches += 1
    return matches

#=============================================================================
def last_16_binary_bits(number):
#
#-----------------------------------------------------------------------------
    result = bin(number)[-16:]

    while (len(result) < 16):
        result = "0" + result
    return result
