for i in range(1, 11, 1):
    num1: int = i
    for e in range(1, 11, 1):
        num2: int = e
        answer: int = num1 * num2
        print('', str(num1), "*", str(num2), '=', str(answer), end='')
        if num2 == 10:
            print("")
