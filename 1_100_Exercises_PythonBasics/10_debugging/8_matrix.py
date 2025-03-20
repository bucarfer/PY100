'''Matrix
We wanted to create a matrix 3x3 so we could use it to build a Tic-Tac-Toe game. However, we encountered an issue, as whenever we change a value in one nested list, all nested lists are affected. Can you fix the code?

Copy Code
sub_list = ["-", "-", "-"]
matrix = []

for _ in range(3):
    matrix.append(sub_list)

matrix[0][0] = "X"
print(matrix) # [['X', '-', '-'], ['X', '-', '-'], ['X', '-', '-']]'''

sub_list = ["-", "-", "-"]
matrix = []

for _ in range(3):
    matrix.append(sub_list.copy())

matrix[0][0] = "X"
print(matrix) # [['X', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]

# the original append have all the sub_list referencing the same object, we can create copies of the original list with list.copy, what creates a shallow copy of the list object. As a result, modifications in one sub-list won't affect others.
# sub_list.copy()