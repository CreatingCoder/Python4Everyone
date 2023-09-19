class Try:

    def obtainInput(self):
        userInput1 = input('Please input a number:')
        userInput2 = input('Please enter another number:')
        return userInput1, userInput2

    def addNumbers(self):
        userInput1, userInput2 = self.obtainInput()


        try:
            return print(int(userInput1)+ int(userInput2))

        except:
            return print('Error: user input contains a symbol other than a number.')

t = Try()
t.addNumbers()
