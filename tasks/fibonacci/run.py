import os

CASE_DIR = os.path.join(os.path.dirname(__file__), "cases")

for case in sorted(next(os.walk(CASE_DIR))[2]):
    with open(os.path.join(CASE_DIR, case), 'r') as f:
        lines = f.readlines()
        for line in lines:
            n, ans = line.split()
            print(n, flush=True)
            user_ans = input()
            if user_ans != ans:
                raise ValueError(f"{n}th fibonacci number is {ans}. {user_ans} was given.")
print("EXIT", flush=True)
