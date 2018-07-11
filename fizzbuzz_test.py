from fizzbuzz import FizzBuzz

class TestFizzBuzz(object):
    def test_returns_fizz_when_5(self):
        fizzbuzz = FizzBuzz()
        assert fizzbuzz.play(5) == 'fizz'
