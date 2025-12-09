
from typing import List

def split_into_fixed_length_chunks(text: str, chunk_length: int) -> List[str]:
    """Splits a string into chunks of a specified fixed length."""
    return [text[i:i + chunk_length] for i in range(0, len(text), chunk_length)]

class Solution:
    def invalid_ids_part_1(self, id_ranges: List[str]) -> int:
        print(id_ranges)
        invalid_id_sum = 0

        for id_range in id_ranges:
            start, end = id_range.split("-")
            start = int(start)
            end = int(end)
            
            for num in range(start, end + 1):
                str_num = str(num)
                
                if str_num[0:len(str_num)//2] == str_num[len(str_num)//2:]:
                    invalid_id_sum += num

        return invalid_id_sum

    def invalid_ids_part_2(self, id_ranges: List[str]) -> int:
        print(id_ranges)
        invalid_id_sum = 0

        for id_range in id_ranges:
            start, end = id_range.split("-")
            start = int(start)
            end = int(end)

            for num in range(start, end + 1):
                str_num = str(num)
                for chunk_size in range(1, (len(str_num)//2) + 1):
                    chunks = split_into_fixed_length_chunks(str_num, chunk_size)
                    if len(set(chunks)) == 1:
                        # All chunks are the same
                        invalid_id_sum += num
                        break

        return invalid_id_sum
    
if __name__ == "__main__":
    with open("input.txt") as file:
        input = file.read()
        id_ranges = input.split(",")
        sol = Solution()
        print(sol.invalid_ids_part_1(id_ranges))
        print(sol.invalid_ids_part_2(id_ranges))