from fizzbuzz import FizzBuzz

class TestFizzBuzz(object):
    def test_returns_fizz_when_5(self):
        fizzbuzz = FizzBuzz()
        assert fizzbuzz.play(5) == 'fizz'

    def test_returns_fizz_when_10(self):
        fizzbuzz = FizzBuzz()
        assert fizzbuzz.play(10) == 'fizz'

    def test_returns_buzz_when_3(self):
        fizzbuzz = FizzBuzz()
        assert fizzbuzz.play(3) == 'buzz'

    def test_returns_fizzbuzz_when_15(self):
        fizzbuzz = FizzBuzz()
        assert fizzbuzz.play(15) == 'fizzbuzz'
