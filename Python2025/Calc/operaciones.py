def resta(*nums:float)->float:
    res = nums[0]
    for num in nums:
        res -= num

    return res


def suma(*nums:float)->float:
    sum = 0
    for num in nums:
        sum += num

    return sum


def multiplicacion(*nums:float)->float:
    mul = 1
    for num in nums:
        mul *= num

    return mul


def division(n1:float, n2:float)-> float:
    res = n1 / n2
    sobra = n1 % n2

    return res,sobra


def exponente(n1:float, n2:float)-> float:
    exp  = n1**n2
    
    return exp
