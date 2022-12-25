from utils import read_input

DAY = 25
TEST = False
input_str = read_input(day=DAY, test=TEST)

digits = {
    '2': 2,
    '1': 1,
    '0': 0,
    '-': -1,
    '=': -2,
}


def snafu_to_decimal(s):
    n = 0
    for i, item in enumerate(s):
        place = len(s) - i - 1
        n += digits[item] * (5 ** place)
    return n


def decimal_to_snafu(n):
    snafu = ''
    while n:
        n, r = divmod(n, 5)
        match r:
            case 0 | 1 | 2: snafu = str(r) + snafu
            case 3:
                n += 1
                snafu = '=' + snafu
            case 4:
                n += 1
                snafu = '-' + snafu
    return snafu


sum = 0
for snafu in input_str.splitlines():
    sum += snafu_to_decimal(snafu)
print(sum)
print(decimal_to_snafu(sum))
