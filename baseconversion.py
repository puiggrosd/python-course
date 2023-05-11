import argparse
import logging
logging.basicConfig(format='%(asctime)s %(levelname)-5.5s %(message)s  (%(filename)s:%(lineno)s) [%(name)-15.15s] [%(threadName)s]', level=logging.DEBUG)


class BaseConversor:
    """
    A class for converting numbers to a given base.

    Attributes:
    -----------
    base_output : int
        The base to convert the numbers to.

    Methods:
    --------
    to_char(digit: int) -> str:
        Converts a single digit to its corresponding character in the given base.

    convert(number: int) -> str:
        Converts a number to the given base and returns it as a string.

    __repr__() -> str:
        Returns a string representation of the instance.

    """
        
    def __init__(self, base_output):
        """
        Initializes the BaseConversor instance.

        Parameters:
        -----------
        base_output : int
            The base to convert the numbers to.
        """
        self.base_output = base_output
    
    def to_char(self, digit):
        """
        Converts a single digit to its corresponding character in the given base.

        Parameters:
        -----------
        digit : int
            The digit to be converted.

        Returns:
        --------
        str
            The corresponding character in the given base.
        """
        if 0<=digit <=9:
            return str(digit)
        else:
            return chr(ord('A')+(digit-10))
    
    def convert(self, number):
        """
        Converts a number to the given base and returns it as a string.

        Parameters:
        -----------
        number : int
            The number to be converted.

        Returns:
        --------
        str
            The number converted to the given base.
        """
        # Raise an error if the input number is negative
        if number < 0: 
            raise TypeError("Cannot convert negative numbers to a base.")

        # Initialize an empty string to store the result
        result = ""

        # Repeatedly divide the input number by the base and append the remainder to the result string
        while number >= self.base_output:
            # Compute the quotient and remainder of the division
            number, modulo = number // self.base_output, number % self.base_output

            # Convert the remainder to its corresponding character in the given base and append it to the result
            result = self.to_char(modulo) + result

        # Convert the final quotient (which may be less than the base) to its corresponding character in the given base and append it to the result
        result = self.to_char(number) + result
        return result

    
    def __repr__(self):
        return f"Conversor to base: {self.base_output} (class: {type(self).__name__})"

class B2Conversor(BaseConversor):
    """
    A subclass of BaseConversor for converting numbers to binary (base 2).

    Methods:
    --------
    convert(number: int) -> str:
        Converts a number to binary and returns it as a string.

    """
    def __init__(self):
        super().__init__(2)

    def convert(self, number):
        if number < 0: 
            raise TypeError("Cannot convert negative numbers.")
        return bin(number)[2:]

if __name__ == "__main__":
    logging.info(f'Program start')
    parser = argparse.ArgumentParser(
        description="This program takes 2 arguments"
        )
    parser.add_argument('-o', type=int, required=True, help='output base')
    parser.add_argument('number', type=int, help='number to convert')
    args = parser.parse_args()
    logging.debug(vars(args))
    base_output = args.o
    number = args.number
    logging.info(f'Converting number:{number} to base:{base_output}')
    
    
    if base_output==2:
        conversor = B2Conversor()
    else:
        conversor = BaseConversor(base_output)
    print(f'Converting number:{number} to base:{base_output} result: {conversor.convert(number)}')
    logging.info(f'Program end')


