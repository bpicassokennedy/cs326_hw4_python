def load(arr):
    file = open("inputFile.txt", "r")
    for line in file:
        arr.append(list(map(int, line.split())))
    file.close()

#def rotateArr():

def printArr(arr):
    for row in arr:
        print(row)

def main():
    original_array = []

    load(original_array) #loading and storing the values in the file to a 2d array

    print("Original Array: ")
    printArr(original_array) #printing the given 2d array 

    rotated_array = []
    #rotateArr(rotated_array) #rotating the original array 90 degrees clockwise

    print()
    print("Rotated Array: ")
    printArr(rotated_array)

if __name__ == "__main__":
    main()