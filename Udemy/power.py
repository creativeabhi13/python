def pow(base,exp):
    assert exp>=0 and int(exp) ==exp, 'The exponenetial must be as postive integer only!'
    if exp==0:
        return 1
    if exp==1:
        return base
    return base*pow(base,exp-1)
print(pow(2,3))