import time
import multiprocessing
import random


def processOne():
    #random wait between 0 and 1 seconds
    waitOne = random.uniform(0,1)
    #wait the alloted time
    time.sleep(waitOne)
    #print the process name and the wait time
    print(f"Process One: {waitOne}")
    
def processTwo():
    waitTwo = random.uniform(0,1)
    time.sleep(waitTwo)
    print(f"Process Two: {waitTwo}")
    
def processThree():
    waitThree = random.uniform(0,1)
    time.sleep(waitThree)
    print(f"Process Three: {waitThree}")


if __name__ == '__main__':
    #define the multi-processes
    process1 = multiprocessing.Process(target=processOne)
    process2 = multiprocessing.Process(target=processTwo)
    process3 = multiprocessing.Process(target=processThree)
    
    #run the processes    
    process1.start()
    process2.start()
    process3.start()