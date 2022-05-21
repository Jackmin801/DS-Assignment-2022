from itertools import chain
import random
import os

CASE_DIR = os.path.join(os.path.dirname(__file__), "cases")

test_cases = next(os.walk(CASE_DIR))[2]
print(len(test_cases))
for case in sorted(test_cases):
    with open(os.path.join(CASE_DIR, case), 'r') as f:
        num_rails = int(f.readline())
        print(num_rails)

        rails = [f.readline().strip() for _ in range(num_rails)]
        random.shuffle(rails)
        print(*rails, sep="\n")
        rails = [i.split(" => ") for i in rails]
        
        districts = list(set(chain(*rails)))
        adj = {d:set() for d in districts}
        for p, q in rails:
            adj[p].add(q)
            adj[q].add(p)

        f.readline()
        num_queries = int(f.readline())
        print(num_queries)
        for _ in range(num_queries):
            line = f.readline()
            print(line, end="")
            src, dst = line.strip().split(" -> ")

            try:
                user_path = list(map(str.strip, input().split("->")))
            except EOFError:
                raise Exception('Program stopped without completing all the tasks!')
            if user_path[0] != src:
                raise ValueError("This path doesnt start at the starting station!")
            if user_path[-1] != dst:
                raise ValueError("This path doesnt end at the destination!")
            for i, j in zip(user_path, user_path[1:]):
                if j not in adj[i]:
                    raise ValueError(f"There is no train from {i} to {j}")

print("EXIT", flush=True)
