import unittest

# method to check if number is prime or not
def isprime(number):
    if number > 1:
        for i in range ( 2 , (number // 2) + 1 ):
            if (number % i) == 0:
                return False
        else:
            return True
    else:
        return False


# tests for method
class IsNumberPrimeTests ( unittest.TestCase ):

    def testTwo(self):
        self.failUnless ( isprime ( 7 ) )
        # fail unless :- assertTrue


    def testOne(self):
        self.failIf ( isprime ( 8 ) )
        # fail if :- assertfalse


def main():
    unittest.main ( )


if __name__ == '__main__':
    main ( )
