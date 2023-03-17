def get_matrix():
    rows = int(input("Enter the number of rows: "))
    matrix = []
    for i in range(rows):
        row = input(f"Enter space-separated values for row {i+1}: ")
        row_values = [int(x) for x in row.split()]
        matrix.append(row_values)
    return matrix

def sort_rows(matrix):
    row_sums = {}
    for i in range(len(matrix)):
        row_sum = sum(matrix[i])
        row_sums[i] = row_sum
    
    sorted_indices = sorted(row_sums, key=row_sums.get)
    sorted_matrix = [matrix[i] for i in sorted_indices]
    
    return sorted_matrix

def print_matrix(matrix):
    for row in matrix:
        row_str = ' '.join([str(x) for x in row])
        print(row_str)

matrix = get_matrix()
sorted_matrix = sort_rows(matrix)
print_matrix(sorted_matrix)
