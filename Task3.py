# This is Task 3: Password generator
import random
import string


class Password:
    @staticmethod
    def high(n):
        let = random.choices(string.ascii_letters, k=(n - (n // 3)))
        dig = random.choices(string.digits, k=(n // 3))
        return random.sample(let + dig, n)

    @staticmethod
    def mid(n):
        let = random.choices(string.ascii_letters, k=(n - (n // 2)))
        dig = random.choices(string.digits, k=(n // 2))
        return random.sample(let + dig, n)

    @staticmethod
    def low(n):
        let = random.choices(string.ascii_letters, k=(n // 4))
        dig = random.choices(string.digits, k=(n - (n // 4)))
        return random.sample(let + dig, n)

    @classmethod
    def gen(cls):
        n = int(input("Enter length of password: \n"))
        cmplx = input("Complexity: low, mid, high? \n")
        if cmplx == 'high':
            print("".join(cls.high(n)))
        elif cmplx == 'mid':
            print("".join(cls.mid(n)))
        elif cmplx == 'low':
            print("".join(cls.low(n)))
        else:
            return "INVALID"


Password.gen()
