

def solve(term, first,two: list):
    multiplier = two[1]-two[0]
    print(multiplier)
    return round(first+(term-1)*multiplier,4)


print(solve(term=36, first=10, two=[17,24]))