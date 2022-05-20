import os

CASE_DIR = os.path.join(os.path.dirname(__file__), "cases")

test_cases = next(os.walk(CASE_DIR))[2]
#print(len(test_cases))
for case in sorted(test_cases):
    with open(os.path.join(CASE_DIR, case), 'r') as f:
        while True:
            line = f.readline()
            if line == "END\n":
                print("REBOOT")
                break
            if line != "CLEAR\n":
                print(line, end="")
            else:
                ans = set(f.readline().strip().split())
                user_ans = set(input().strip().split())

                if ans != user_ans:
                    if len(user_ans) != len(ans):
                        raise ValueError(f"Wrong answer. Too many entries. Expected {len(ans)} entries but got {len(user_ans)}")
                    raise ValueError(f"Wrong Answer. Entries missing from answer: {ans - user_ans}. Entries not in answer: {user_ans - ans}")

print("EXIT", flush=True)
