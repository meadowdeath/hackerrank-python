def swap_case(s):
    letters = list(s)
    swaped_letters = [letter.upper() if letter.islower() else letter.lower() for letter in letters]
    return "".join(swaped_letters)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)