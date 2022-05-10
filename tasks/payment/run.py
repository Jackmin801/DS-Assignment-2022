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
                    print(len(ans))
                    print(len(user_ans))
                    raise ValueError("Wrong answer")

print("EXIT", flush=True)
