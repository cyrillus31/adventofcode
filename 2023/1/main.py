def get_two_digits(line: str) -> int:
    d = {'first': "0", 'last': "0"}
    first_found = False
    for char in line:
        if char.isdigit():
            d['last'] = char
            if not first_found:
                d['first'] = char
                first_found = True
    result = int(d.get('first', '0') + d.get('last', '0'))
    return result

with open('input.txt', 'r') as file:
    total = 0
    for line in file:
        result = get_two_digits(line)
        total += result

print(total)
        


