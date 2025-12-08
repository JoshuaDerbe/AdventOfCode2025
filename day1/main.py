from csv import DictReader

class Solution:
    def foo(self, input: str) -> int:
        return 0

    
if __name__ == "__main__":
    with open("input.csv") as file:
        reader = DictReader(file)
        for row in reader:
            print(row)