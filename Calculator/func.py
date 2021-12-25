def plus(a, b):
    x = 0
    pw = 1
    carry = 0
    while a > 0 or b > 0:
        a0 = a % 10
        b0 = b % 10

        x += pw * ((a0 + b0 + carry) % 10)
        carry = (a0 + b0 + carry) // 10

        pw *= 10
        a //= 10
        b //= 10
    x += pw * carry
    return x


def minus(a, b):
    x = 0
    pw = 1
    flag = 0
    while a > 0:
        A = a % 10
        if flag == 1:
            A = A - 1
        if b > 0:
            B = b % 10
            if A >= B:
                flag = 0
            else:
                flag = 1
                A = A + 10
            C = A - B
        else:
            C = A
        x += pw * C
        pw *= 10
        a //= 10
        b //= 10
    return x
