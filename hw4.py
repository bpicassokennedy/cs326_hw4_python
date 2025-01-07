# Programmer: Bella Picasso-Kennedy 
# Date: 01/06/2025
# Purpose: CS326 HW4 (write a modular program in Python - my first ever python program! - for rotating a 2d array) 


INPUT_FILE = "inputFile.txt"

def load(rows, cols, arr):
    try:
        file = open(INPUT_FILE, "r") # source: https://www.w3schools.com/python/python_file_open.asp
        for line in file:
            current_row = [int(char) for char in line.strip()] # source: https://www.geeksforgeeks.org/convert-string-to-integer-in-python/ 
            arr.append(current_row) # source: https://www.geeksforgeeks.org/appending-to-2d-list-in-python/ 
            rows += 1               # source: https://www.w3schools.com/python/ref_string_strip.asp 
            if cols < len(current_row):
                cols = len(current_row)
        for row in arr:
            while len(row) < cols:
                row.append(0)
    except FileNotFoundError:
        print("Error opening file!")
    return rows, cols
    
def rotate_arr(rows, cols, arr, rotated):
    for i in range(cols): # source: https://stackoverflow.com/questions/6667201/how-to-define-a-two-dimensional-array 
        rotated.append([0] * rows) 
    for i in range(rows):
        for j in range(cols):
            rotated[j][rows - i - 1] = arr[i][j]
    temp = rows 
    rows = cols
    cols = temp
    return rows, cols

def print_arr(rows, cols, arr):
    for i in range(rows):
        for j in range(cols):
            print(arr[i][j], end= " ") # source: https://stackoverflow.com/questions/17870612/printing-a-two-dimensional-array-in-python 
        print()

def main():
    rows = 0
    cols = 0
    original_array = [] # source: https://stackoverflow.com/questions/2397141/how-to-initialize-a-two-dimensional-array-list-of-lists-if-not-using-numpy-in 
    rotated_array = []

    rows, cols = load(rows, cols, original_array) #loading and storing the values in the file to a 2d array
    print("Original: ")
    print_arr(rows, cols, original_array) #printing the given 2d array 

    rows, cols = rotate_arr(rows, cols, original_array, rotated_array) #rotating the original array 90 degrees clockwise
    print("\nRotated: ")
    print_arr(rows, cols, rotated_array)

if __name__ == "__main__":
    main()