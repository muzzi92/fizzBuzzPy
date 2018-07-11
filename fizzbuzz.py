class FizzBuzz():
    def play(self, num):
        if num % 15 == 0:
            return 'fizzbuzz'
        elif num % 5 == 0:
            return 'fizz'
        else:
            return 'buzz'
