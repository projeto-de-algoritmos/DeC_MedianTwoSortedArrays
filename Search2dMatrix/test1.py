# Caso de Teste 1
# Input: matrix = [
#     [1,4,7,11,15],
#     [2,5,8,12,19],
#     [3,6,9,16,22],
#     [10,13,14,17,24],
#     [18,21,23,26,30]
# ], 
# target = 5
# Output: true

import search2dMatrix as sd

matrix = [
    [1,4,7,11,15],
    [2,5,8,12,19],
    [3,6,9,16,22],
    [10,13,14,17,24],
    [18,21,23,26,30]
]
target = 5

solution = sd.Solution()
print(f"Target: {target}")
print(f"Matrix:")
for i in range(0, len(matrix)):
    print(matrix[i])
result = solution.searchMatrix(matrix, target)
print(f"Solution: {result}")






