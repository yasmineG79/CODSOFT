# This is task 2: calculator
class Calculator:
    @staticmethod
    def add(n1, n2):
        return n1 + n2

    @staticmethod
    def sub(n1, n2):
        return n1 - n2

    @staticmethod
    def multiply(n1, n2):
        return n1 * n2

    @staticmethod
    def divide(n1, n2):
        return n1 / n2

    @classmethod
    def calc(cls):
        run = input("on/off?")
        while run == "on":
            n1 = int(input("Enter first number \n"))
            n2 = int(input("Enter second number \n"))
            op = input("Enter operator: \n")
            if op == '+':
                ans = cls.add(n1, n2)
                print(n1, op, n2, "=", ans)
            elif op == '-':
                ans = cls.sub(n1, n2)
                print(n1, op, n2, "=", ans)
            elif op == '*':
                ans = cls.multiply(n1, n2)
                print(n1, op, n2, "=", ans)
            elif op == '/':
                ans = cls.divide(n1, n2)
                print(n1, op, n2, "=", ans)
            else:
                print("INVALID OPERATOR")

            run = input("on/off?")


Calculator.calc()
