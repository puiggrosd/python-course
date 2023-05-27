import argparse
import logging
logging.basicConfig(format='%(asctime)s %(levelname)-5.5s %(message)s  (%(filename)s:%(lineno)s) [%(name)-15.15s] [%(threadName)s]', level=logging.DEBUG)

from abc import ABC, abstractmethod

class Operator(ABC):
    @abstractmethod
    def operate(self, a, b):
        pass


class Add(Operator):
    def operate(self, a, b):
        return a + b

class Subtract(Operator):
    def operate(self, a, b):
        return a - b

class Multiply(Operator):
    def operate(self, a, b):
        return a * b

class Divide(Operator):
    def operate(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
    
operations = {"+": Add(), "-":Subtract(), "*":Multiply(), "/":Divide()}

def token_evaluate(tokens):
    if len(tokens)==0: raise ValueError("Cannot get enough operands")
    token, *rest = tokens
    if token in "+-*/":
        op1, rest = token_evaluate(rest)
        op2, rest = token_evaluate(rest)
        return operations[token].operate(op1,op2),rest
    return float(token), rest

def evaluate(expression):
    tokens = expression.split()
    value, rest = token_evaluate(tokens)
    if len(rest):
        raise ValueError("Mismatch with expression operands")
    return value


if __name__ == "__main__":
    logging.info(f'Program start')
    parser = argparse.ArgumentParser(
        description="This program takes an expression as argument"
        )
    parser.add_argument('expression', type=str, help='number to convert')
    args = parser.parse_args()
    logging.debug(vars(args))
    expression = args.expression
    logging.info(f'Evaluating expression:"{expression}"')

    print(f'Evaluating expression:{expression} result: {evaluate(expression)}')
    logging.info(f'Program end')
