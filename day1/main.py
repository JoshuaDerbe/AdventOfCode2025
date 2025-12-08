from csv import DictReader
from typing import List

class Solution:
    def rotate_dial_part_1(self, dial_rotations: List[str]) -> int:
        num_zeroes = 0

        cur_pos = 50
        for rotation in dial_rotations:
            direction = rotation[0]
            amount = int(rotation[1:])
            if direction == "L":
                cur_pos = (cur_pos - amount) % 100
            elif direction == "R":
                cur_pos = (cur_pos + amount) % 100
            else:
                raise ValueError(f"Invalid direction: {direction}")
            
            if cur_pos == 0:
                num_zeroes += 1
                
        return num_zeroes

    def rotate_dial_part_2(self, dial_rotations: List[str]) -> int:
        num_zeroes_crossed = 0

        cur_pos = 50
        for rotation in dial_rotations:
            direction = rotation[0]
            amount = int(rotation[1:])

            # Extract away multiple spinnings
            num_spinnings = amount // 100
            amount = amount % 100
            num_zeroes_crossed += num_spinnings

            if direction == "L":
                if (cur_pos - amount) <= 0 and cur_pos != 0:
                    num_zeroes_crossed += 1
                
                # Do rotation
                cur_pos = (cur_pos - amount) % 100
            elif direction == "R":
                if (cur_pos + amount) >= 100 and cur_pos != 0:
                    num_zeroes_crossed += 1

                # Do rotation
                cur_pos = (cur_pos + amount) % 100
            else:
                raise ValueError(f"Invalid direction: {direction}")

        
        return num_zeroes_crossed

    
if __name__ == "__main__":
    with open("input.csv") as file:
        reader = DictReader(file)
        rotations = [row["rotation"] for row in reader]
        sol = Solution()
        print(sol.rotate_dial_part_2(rotations))