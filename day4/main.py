from typing import List
from copy import deepcopy

class Solution:
    def print_matrix(self, matrix: List[List[str]]):
        for row in matrix:
            for item in row:
                print(item, end=' ')
            print() # Move to the next line after each row

    def is_paper(self, matrix: List[List[str]], row: int, col: int) -> bool:
        if row < 0 or row >= len(matrix) or col < 0 or col >= len(matrix[0]):
            return False
        
        return matrix[row][col] == "@"

    def count_reachable_paper_part_1(self, matrix: List[List[str]]) -> int:
        num_reachable_paper = 0
        visual_matrix = deepcopy(matrix)

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if self.is_paper(matrix, row, col):
                    paper_neighbours = 0
                    directions = [(-1, 0), (-1, -1), (-1, 1), (1, 0), (1, -1), (1, 1), (0, -1), (0, 1)]
                    for direction in directions:
                        new_row = row + direction[0]
                        new_col = col + direction[1]
                        if self.is_paper(matrix, new_row, new_col):
                            paper_neighbours += 1
                    if paper_neighbours < 4:
                        num_reachable_paper += 1
                        visual_matrix[row][col] = "x"

        print("REACHABLE:")
        self.print_matrix(visual_matrix)

        return num_reachable_paper

    def count_reachable_paper_part_2(self, matrix: List[List[str]]) -> int:
        removed_paper = 0
        copy_matrix = deepcopy(matrix)

        while True:
            changed = False
            for row in range(len(copy_matrix)):
                for col in range(len(copy_matrix[0])):
                    if self.is_paper(copy_matrix, row, col):
                        paper_neighbours = 0
                        directions = [(-1, 0), (-1, -1), (-1, 1), (1, 0), (1, -1), (1, 1), (0, -1), (0, 1)]
                        for direction in directions:
                            new_row = row + direction[0]
                            new_col = col + direction[1]
                            if self.is_paper(copy_matrix, new_row, new_col):
                                paper_neighbours += 1
                        if paper_neighbours < 4:
                            removed_paper += 1
                            copy_matrix[row][col] = "x"
                            changed = True
            if not changed:
                break

        print("FINAL MATRIX:")
        self.print_matrix(copy_matrix)

        return removed_paper

    
if __name__ == "__main__":
    with open("input.txt") as file:
        matrix = [[char for char in line.rstrip()] for line in file]
        sol = Solution()
        sol.print_matrix(matrix)
        
        print(sol.count_reachable_paper_part_2(matrix))