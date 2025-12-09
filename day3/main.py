from csv import DictReader
from typing import List

class Solution:
    def max_joltage_part_1(self, battery_banks: List[str]) -> int:
        total_max_joltage = 0
        for bank in battery_banks:
            l_digit = -1
            r_digit = -1
            for i, digit in enumerate(bank):
                if i == len(bank) - 1:
                    break

                digit = int(digit)
                
                if digit > l_digit:
                    # This left digit is better than the current left digit, so we always will update left and right digit
                    l_digit = digit
                    r_digit = -1
                    # Find best right digit for this left digit
                    for j in range(i + 1, len(bank)):
                        if int(bank[j]) > r_digit:
                            r_digit = int(bank[j])
                elif digit == l_digit:
                    # This left digit is the same as the current left digit, so it is possible the available right digits are worse than our current number
                    cur_r_digit = -1
                    # Find best right digit for this left digit
                    for j in range(i + 1, len(bank)):
                        if int(bank[j]) > cur_r_digit:
                            cur_r_digit = int(bank[j])
                    if cur_r_digit > r_digit:
                        r_digit = cur_r_digit

            max_joltage = int(f"{l_digit}{r_digit}")
            print("Max Joltage: ", max_joltage)
            total_max_joltage += max_joltage

        return total_max_joltage

    # Greedily grab the largest digit. If we ever have a valid number from that, we know it is the best possible number.
    # If greedily grabbing the largest digit does not work, we can try the next largest digit.
    # This repeats until we first see a valid number.
    def greedy_largest_number(self, remaining_batteries: List[int], required_length: int) -> int:
        if remaining_batteries == []:
            return -1
        if len(remaining_batteries) < required_length:
            return -1
        if required_length == 1:
            return max(remaining_batteries)

        # Keep removing from the list the max digit until we have the required length
        digit_options = remaining_batteries.copy()
        tried_indexes = set()
        while True:
            max_digit = -1
            max_digit_index = -1
            for i, digit in enumerate(digit_options):
                if digit > max_digit and i not in tried_indexes:
                    max_digit = digit
                    max_digit_index = i

            new_list = remaining_batteries[max_digit_index + 1:]
            best_rest = self.greedy_largest_number(new_list, required_length - 1)
            if best_rest != -1:
                return int(f"{max_digit}{best_rest}")
            else:
                # Ignore this index as an option and try the next biggest digit
                tried_indexes.add(max_digit_index)


    def max_joltage_part_2(self, battery_banks: List[str]) -> int:
        max_joltage = 0
        for bank in battery_banks:
            int_battery_banks = [int(digit) for digit in bank]
            max_joltage += self.greedy_largest_number(int_battery_banks, 12)
        return max_joltage

    
if __name__ == "__main__":
    with open("input.csv") as file:
        reader = DictReader(file)
        battery_banks = [row["bank"] for row in reader]
        sol = Solution()
        print(sol.max_joltage_part_2(battery_banks))