"""
Q3. Take a matrix as input and print the upper triangle of the matrix
Example
Input
1 2 3
4 5 6
7 8 9
Output:
1 2 3
4 5
7
"""

matrix = [[1,2,3],[4,5,6],[7,8,9]]

row = len(matrix)  #This is length of row
column = len(matrix[0])  #This is the length of column

for i in range(row):
    for j in range(column-i):   #This is decrease one element every time from column
        print(matrix[i][j], end=" ")
    print()                 #This will add a new Line