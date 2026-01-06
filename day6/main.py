import math
from typing import List

class Solution:
    def print_matrix(self, matrix: List[List[str]]):
        for row in matrix:
            for item in row:
                print(item, end='')
        print()

    def calculate_part_1(self, problems: List[List[str]]) -> int:
        total = 0

        for problem in problems:
            print(problem)
            operator = problem[-1]
            problem_total = 0
            if operator == "+":
                for num in problem[:-1]:
                    problem_total += int(num)
            elif operator == "*":
                problem_total = 1
                for num in problem[:-1]:
                    problem_total *= int(num)
            print(problem_total)
            total += problem_total

        return total

    def calculate_part_2(self, problem_matrix: List[List[str]]) -> int:
        total = 0

        for row in problem_matrix:
            print(row)
        num_cols = len(problem_matrix[0])
        num_rows = len(problem_matrix)
        cur_nums = []
        for col in range(num_cols - 1, -1, -1):
            cur_num = ""
            for row in range(num_rows):
                if problem_matrix[row][col] != " " and problem_matrix[row][col] != "+" and problem_matrix[row][col] != "*":
                    cur_num += problem_matrix[row][col]
                elif problem_matrix[row][col] == "+":
                    cur_nums.append(cur_num)
                    total += sum([int(num) for num in cur_nums])
                    cur_nums = []
                    cur_num = ""
                elif problem_matrix[row][col] == "*":
                    cur_nums.append(cur_num)
                    total += 1 * math.prod([int(num) for num in cur_nums])
                    cur_nums = []
                    cur_num = ""

            if cur_num != "":
                cur_nums.append(cur_num)
            
        return total
    
if __name__ == "__main__":
    with open("input.txt") as file:
        raw_matrix = []
        columns = []
        first = True
        for line in file:
            if first:
                columns = [[] for _ in range(len(line.split()))]
                first = False
            for num_index, num in enumerate(line.split()):
                columns[num_index].append(num)
            raw_matrix.append([char for char in line if char != "\n"])
        sol = Solution()
        #print(sol.calculate_part_1(columns))
        #sol.print_matrix(raw_matrix)
        print(sol.calculate_part_2(raw_matrix))