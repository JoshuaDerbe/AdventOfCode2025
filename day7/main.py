from collections import deque
from copy import deepcopy
from typing import List

class Solution:
    def print_matrix(self, matrix: List[List[str]]):
        for row in matrix:
            for item in row:
                print(item, end='')
            print()

    def count_beam_splits(self, input: List[List[str]]) -> int:
        total_splits = 0

        matrix = deepcopy(input)

        starting_row = -1
        starting_col = -1
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == "S":
                    starting_row = row
                    starting_col = col
                    break

        bfs_queue = deque([(starting_row + 1, starting_col)])
        visited = set()
        visited.add((starting_row + 1, starting_col))

        while bfs_queue:
            current_row, current_col = bfs_queue.popleft()

            if current_row < 0 or current_row >= len(matrix) or current_col < 0 or current_col >= len(matrix[0]):
                continue

            if matrix[current_row][current_col] == ".":
                matrix[current_row][current_col] = "|"
                bfs_queue.append((current_row + 1, current_col))
            elif matrix[current_row][current_col] == "^":
                total_splits += 1
                if matrix[current_row][current_col - 1] == ".":
                    bfs_queue.append((current_row, current_col - 1))
                if matrix[current_row][current_col + 1] == ".":
                    bfs_queue.append((current_row, current_col + 1))

        self.print_matrix(matrix)

        return total_splits

    def count_timelines(self, input: List[List[str]]) -> int:
        matrix = deepcopy(input)

        starting_row = -1
        starting_col = -1
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] == "S":
                    starting_row = row
                    starting_col = col
                    break

        memo = {}

        def dfs(row: int, col: int) -> int:
            if row >= len(matrix):
                return 1
            
            if (row, col) in memo:
                return memo[(row, col)]

            result = 0

            if matrix[row][col] == ".":
                result += dfs(row + 1, col)
            elif matrix[row][col] == "^":
                if matrix[row][col - 1] == ".":
                    result += dfs(row, col - 1)
                if matrix[row][col + 1] == ".":
                    result += dfs(row, col + 1)

            memo[(row, col)] = result
            return result

        self.print_matrix(matrix)

        return dfs(starting_row + 1, starting_col)
    
if __name__ == "__main__":
    with open("input.txt") as file:
        matrix = []
        for line in file:
            matrix.append([char for char in line if char != "\n"])
        sol = Solution()
        sol.print_matrix(matrix)
        print(sol.count_beam_splits(matrix))
        print(sol.count_timelines(matrix))