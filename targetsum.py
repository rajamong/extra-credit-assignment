# creates a function to take an array of integers and a target sum, and 
# return an array containing the two integers that add up to the target sum
def findtargetvalues(numberarray, arraysize, targetvalue):
    # creates a variable to store front index location of the array
    frontindex = 0
    # creates a variable to store next index location of the array
    nextindex = arraysize

    # runs as long as the next index is greater than the front index
    while nextindex > frontindex:
        # if the two numbers at the indexes of the array add up to the target value
        if (numberarray[frontindex] + numberarray[nextindex] == targetvalue):
            # prints out the array containing to two numbers
            print ("[" + str(numberarray[frontindex]) + ", " + str(numberarray[nextindex]) + "]")
            # breaks out of the loop
            break;
        # if the two numbers at the indexes of the array add up to greater than target value
        elif (numberarray[frontindex] + numberarray[nextindex] > targetvalue):
            # decremement the next index variable
            nextindex = nextindex - 1
        # if the two numbers at the indexes of the array add up to less than target value
        else:
            # increment the front index variable
            frontindex = frontindex + 1


if __name__ == "__main__":
    # variable with the example array of integers
    numberarray = [2, 7, 11, 15]
    # variable with the size of the example array
    arraysize = len(numberarray)
    arraysize = arraysize - 1
    # variable with the example target value
    targetvalue = 9
    # calls the function to find the target values
    findtargetvalues(numberarray, arraysize, targetvalue)
