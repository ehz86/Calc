from func import plus, minus

def calc(a, b, z):
    if z == '+':

        ml = max(len(str(a)), len(str(b)))
        if b > a:
            u = b
            b = a
            a = u
        print(' ' * (1 + ml - len(str(a))), end='')
        print(a)
        print('+', end='')
        print(' ' * (ml - len(str(b))), end='')
        print(b)
        print(' ' + '_' * ml)
        p = 10
        if a == 0 or b == 0:

            print(' ' * (ml - len(str(a)) + 1), end='')
            print(a)


        else:

            for i in range(ml):
                print(" " * (ml - i), end='')
                d = plus(a, b) % p
                print(d // (p // 10))
                p *= 10

            s = plus(a, b)
            print(" " * (1 + ml - len(str(s))), end='')
            print(s)
    else:
        if z == '-':
            p = 10
            if int(a) >= 0 or int(b) >= 0:
                ml = max(len(str(a)), len(str(b)))
                flag2 = 0
                if a > b:

                    print(' ' * (1 + ml - len(str(a))), end='')
                    print(a)
                    print('-', end='')
                    print(' ' * (ml - len(str(b))), end='')
                    print(b)
                    print(' ' + '_' * ml)

                else:

                    print(' ' * (1 + ml - len(str(b))), end='')
                    print(b)
                    print('-', end='')
                    print(' ' * (ml - len(str(a))), end='')
                    print(a)
                    print(' ' + '_' * ml)
                if a == b:

                    print(' ' * (len(str(a)) - 1), end=' ')
                    print(0)
                else:
                    if a == 0:

                        print(' ' * (ml - len(str(b))), end='')
                        print(-b)

                    else:

                        if b == 0:
                            print(' ' * (ml - len(str(a))), end=' ')
                            print(a)
                        else:
                            if a < b:
                                a, b = b, a
                                flag2 = 1
                            for i in range(ml):
                                print(' ' * (ml - i), end='')
                                d = minus(int(a), int(b)) % p
                                print(d // (p // 10))
                                p *= 10
                            s = minus(int(a), int(b))
                            if flag2 == 1:
                                print(' ' * (ml - len(str(s))), end='')
                                print(-s)

                            else:

                                print(' ' * (ml - len(str(s))), end=' ')
                                print(s)
        else:
            print('Не верный знак')
