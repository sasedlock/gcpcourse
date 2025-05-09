def add(num1, num2):
    # Cast to integers
    num1int = int(num1)
    num2int = int(num2)

    # Sum them up
    if num1int is not None and num2int is not None:
        return num1int + num2int
    else:
        return 0
    
def add_array(numbers: list[int]) -> int:
    sum = 0
    for n in numbers:
        sum += n
    return sum
