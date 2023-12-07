digits = {
        "one": ("one", "1"),
        "two": ("two", "2"),
        "thr": ('three', "3"),
        "fou": ('four', "4"),
        "fiv": ('five', "5"),
        "six": ('six', "6"),
        "sev": ('seven', "7"),
        "eig": ('eight', "8"),
        "nin": ('nine', "9"),
        }




def get_two_digits(line: str) -> int:
    d = {'first': "0", 'last': "0"}
    first_found = False
    start = 0
    full = "00000"
    for index, char in enumerate(line):
        if char.isdigit():
            d['last'] = char
            if not first_found:
                d['first'] = char
                first_found = True
        end = index
        string = line[start:(end+1)]
        if len(string) == 3:
            if string in digits:
                full = digits[string][0]
                l = len(full)
                if line[start: start+l] == full:
                    d['last'] = digits[string][1]
                    if not first_found:
                        d['first'] = digits[string][1]
                        first_found = True
            start += 1
    result = int(d.get('first', '0') + d.get('last', '0'))
    return result
        

with open('input.txt', 'r') as file:
    total = 0
    for line in file:
        line = line.strip()
        result = get_two_digits(line)
        total += result
        print("this is line: ", line, "result: ", result)

print(total)
