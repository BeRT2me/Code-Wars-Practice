def last_digit(n1, n2):
    if n2 % 4 != 0 or n2 == 0:
        return int(str(n1**(n2 % 4))[-1])
    else:
        return int(str(n1**4)[-1])
