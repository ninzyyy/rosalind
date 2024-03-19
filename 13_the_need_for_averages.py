
def expected_num_of_offspring(couples:list) -> int:

    total = (1*couples[0]) + (1*couples[1]) + (1*couples[2]) + (0.75*couples[3]) + (0.5*couples[4]) + (0*couples[5])
    total *= 2
    return total

arr = [19988, 18845, 18306, 18219, 19146, 17774]

print(expected_num_of_offspring(arr))
