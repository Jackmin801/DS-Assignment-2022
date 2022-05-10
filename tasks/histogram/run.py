from typing import List
import os

CASE_DIR = os.path.join(os.path.dirname(__file__), "cases")

test_cases = next(os.walk(CASE_DIR))[2]
print(len(test_cases))
for case in sorted(test_cases):
    with open(os.path.join(CASE_DIR, case), 'r') as f:
        print(f.readline(), end='')
        print(f.readline(), end='', flush=True)
        f.readline()
        cutoffs: List[int] = list(map(int, f.readline().split()))
        counts: List[int] = list(map(int, f.readline().split()))
        
        user_cutoffs: List[int] = list(map(int, input().split()))
        user_counts: List[int] = list(map(int, input().split()))
        
        if cutoffs != user_cutoffs:
            raise ValueError("Wrong cutoffs")
        if counts != user_counts:
            raise ValueError("Wrong counts")

print("EXIT", flush=True)
