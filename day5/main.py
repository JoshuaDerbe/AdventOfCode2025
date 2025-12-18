from typing import List

class FreshRange:
    def __init__(self, start: int, end: int):
        self.start = start
        self.end = end

    def __repr__(self):
        return f"FreshRange(start={self.start}, end={self.end})"

class Solution:
    def count_fresh_ingredients(self, fresh_ranges: List[FreshRange], ingredient_ids: List[int]) -> int:
        fresh_ingredients = 0

        fresh_ranges.sort(key=lambda x: x.start)
        for ingredient_id in ingredient_ids:
            for fresh_range in fresh_ranges:
                if ingredient_id >= fresh_range.start and ingredient_id <= fresh_range.end:
                    fresh_ingredients += 1
                    break

        return fresh_ingredients

    def total_fresh_ingredients(self, fresh_ranges: List[FreshRange]) -> int:
        total_fresh_ingredients = 0

        fresh_ranges.sort(key=lambda x: x.start)
        non_overlapping_fresh_ranges = []
        for fresh_range in fresh_ranges:
            if not non_overlapping_fresh_ranges or non_overlapping_fresh_ranges[-1].end < fresh_range.start:
                non_overlapping_fresh_ranges.append(fresh_range)
            else:
                non_overlapping_fresh_ranges[-1].end = max(non_overlapping_fresh_ranges[-1].end, fresh_range.end)
        print(non_overlapping_fresh_ranges)

        for fresh_range in non_overlapping_fresh_ranges:
            total_fresh_ingredients += fresh_range.end - fresh_range.start + 1

        return total_fresh_ingredients
        
if __name__ == "__main__":
    with open("input.txt") as file:
        fresh_ranges = []
        ingredient_ids = []
        on_ingredient_ids = False
        for line in file:
            if line == "\n":
                on_ingredient_ids = True
                continue
        
            if on_ingredient_ids:
                ingredient_ids.append(int(line.strip()))
            else:
                fresh_ranges.append(FreshRange(start=int(line.split("-")[0]), end=int(line.split("-")[1])))

        print(fresh_ranges)
        print(ingredient_ids)
        sol = Solution()
        print(sol.count_fresh_ingredients(fresh_ranges, ingredient_ids))
        print(sol.total_fresh_ingredients(fresh_ranges))