def hex_converter():
    # only support the hex-convertion from 2 to 10
    num = int(input("input the number: "))
    from_hex = int(input("input the original hex: "))
    to_hex = int(input("input the hex you want to convert to: "))
    if num < 0:
        num *= -1
    sum = 0
    power = 1
    while num >= 1:
        remainder = num%to_hex
        num //= to_hex
        sum += remainder*power
        power *= from_hex

    return sum

result = hex_converter()
print(result)

def ten_to_hex():
    #only supprt from 10 to 16
    num = int(input("input the number here: "))
    bases = [str(_) for _ in range(0,11)] + [chr(i) for i in range(65,75)]
    result = ''
    while num:
        remainder = num%16
        num //= 16
        result  = bases[remainder] + result
    return result

print(ten_to_hex())




