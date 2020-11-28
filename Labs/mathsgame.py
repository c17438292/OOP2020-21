class game:
    def __init__(self):
        print("""
                Press 1 if you would like to play the Fibonacci game.    
                Press 2 if you woukd like to play our ...        
                Press 3 if you would like to play our ...        """)
        Ans = int(input("\t        Enter your number now\n"))

        if Ans == 1:
            self.fib()
    
    def fib(self):
        print("You have chosen to play our game based around fibonacci. Fibonacci is a sequence of numbers in which " + 
        "the next number of the list is calculated by adding the n-1th term and the n-2th term together" +
        "For example, the first 2 numbers are 0 and 1. So the 3rd number is 0 + 1 which is 1.")
        print("How many values of the fibonacci sequence would you like to see?")
        self.n = int(input())

        self.fibonacci = [0,1]
        if self.n<=0:
            print("Input has to be greater than 0!!!")
        elif self.n == 1:
            return self.fibonacci[0]
        elif self.n == 2:
            return self.fibonacci
        else:
            for i in range(2,self.n):
                tempfib = (self.fibonacci[-1] + self.fibonacci[-2])
                self.fibonacci.append(tempfib)

        print(self.fibonacci)
        self.nextNum = self.fibonacci[-1] + self.fibonacci[-2]

        print("Now its your turn! what is the next number in the fibonacci sequence?")
        self.score = 0
        self.ans = int(input())

        if self.ans == self.nextNum:
            print("Correct, you are getting the hang of this!")
            self.fibonacci.append(self.ans)
            self.score += 1
            print("Your score is: " + str(self.score))
        else:
            print("Wrong, the correct number is {}".format(self.nextNum))

g = game()


