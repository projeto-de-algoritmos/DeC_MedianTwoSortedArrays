class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        return search_matrix_helper(matrix, target, 0, 0, rows - 1, cols - 1)


def search_matrix_helper(matrix, target, start_row, start_col, end_row, end_col):
    if start_row > end_row or start_col > end_col:
        return False

    mid_row = (start_row + end_row) // 2
    mid_col = (start_col + end_col) // 2
    mid_element = matrix[mid_row][mid_col]

    if mid_element == target:
        return True
    elif mid_element < target:
        # Search the bottom-right submatrix
        return (
            search_matrix_helper(matrix, target, mid_row + 1, start_col, end_row, end_col)
            or search_matrix_helper(matrix, target, start_row, mid_col + 1, mid_row, end_col)
            or search_matrix_helper(matrix, target, mid_row + 1, mid_col + 1, end_row, end_col)
        )
    else:
        # Search the top-left submatrix
        return (
            search_matrix_helper(matrix, target, start_row, start_col, mid_row - 1, end_col)
            or search_matrix_helper(matrix, target, start_row, start_col, end_row, mid_col - 1)
            or search_matrix_helper(matrix, target, start_row, mid_col, mid_row - 1, end_col)
        )