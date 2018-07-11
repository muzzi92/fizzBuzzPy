class FizzBuzz():
    def play(self, num):
        if num % 15 == 0:
            return 'fizzbuzz'
        elif num % 5 == 0:
            return 'fizz'
        elif num % 3 == 0:
            return 'buzz'
        else:
            return num
