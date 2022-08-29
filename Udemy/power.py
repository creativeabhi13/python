base = int(input("enter the base"))
exp = int(input("enter the exponent"))


def pow(base, exp):
    assert base >= 0 and int(base) == base, 'this is for positive'
    if exp == 0:
        return 1
    if exp == 1:
        return base
    return base*pow(base, exp-1)


print(pow(base, exp))
