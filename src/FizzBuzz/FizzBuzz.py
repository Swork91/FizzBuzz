'''
Created on May 10, 2018
FizzBuzz
@author: Sam

Challenge: Write a program that counts 1 to 100. Every time it is a multiple of 3 you say 'Fizz' and every time its a multiple of 5 say 'Buzz'. When it is both write 'FizzBuzz'
'''

# Constant time O(1) unmaintainable without wanting to kill whoever wrote it. 
def constantFizzBuzz():
    print("1")
    print("2")
    print("Fizz")
    print("4")
    print("Buzz")
    print("Fizz")
    print("7")
    print("8")
    print("Fizz")
    print("Buzz")
    print("11")
    print("Fizz")
    print("13")
    print("14")
    print("FizzBuzz")
    print("you get the idea")
    
# linear time O(n), but also maybe hard to edit/maintain. Written in like 5 minutes from hearing the problem. 
def quickLinearFizzBuzz():
    for i in range(1,101):
        if((i%3==0) & (i%5==0)):
            print('FizzBuzz')
        elif(i%3==0):
            print('Fizz')
        elif(i%5==0):
            print('Buzz')
        else:
            print(i)

# linear time O(n) and written after thinking a little about legacy and readability. Also comments. 
'''
Outputs the numbers between the range 'startingNumber' and 'numberToCountTo'.
Replaces the numbers at the multiple of each variable with the desired word. 
More number multiples can be added by creating their variable and adding an if statement similar to the ones used. 
'''
def plannedLinearFizzBuzz():
    startingNumber = 1
    numberToCountTo = 100
    multipleOfX = 3
    multipleOfY = 5
    multipleOfZ = 4
    
    for i in range(startingNumber,numberToCountTo+1):
        outputFizzBuzz = ""
        
        if(i%multipleOfX==0):
            outputFizzBuzz += ('Fizz')
            
        if(i%multipleOfY==0):
            outputFizzBuzz += ('Buzz')
            
        if(i%multipleOfZ==0):
            outputFizzBuzz += ('Jazz')
            
        if (outputFizzBuzz == ""):
            outputFizzBuzz = i
            
        print(outputFizzBuzz)
        
# constantFizzBuzz()      
# quickLinearFizzBuzz()       
plannedLinearFizzBuzz()