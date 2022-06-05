# Copyright (c) 2022 kamyu. All rights reserved.
#
# Google Code Jam 2022 Round 3 - Problem A. Revenge of GoroSort
# https://codingcompetitions.withgoogle.com/codejam/round/00000000008779b4/0000000000b45189
#
# Time:  O(K * N)
# Space: O(N)
#
# python interactive_runner.py python3 testing_tool.py3 2 -- python3 revenge_of_gorosort.py3
#

def colors(C):
    print(" ".join(map(str, C)), flush=True)
    return int(input())

def revenge_of_gorosort():
    a = list(map(lambda x: int(x)-1, input().split()))
    while True:
        C = [0]*N
        color = 1
        for i in range(N):
            cycle = []
            j = i
            while a[i] >= 0:
                j = a[i]
                a[i], a[j] = a[j], ~a[i]
                cycle.append(j)
            while cycle:
                for _ in range(3 if len(cycle) >= 6 else len(cycle)):
                    C[cycle.pop()] = color
                color += 1
        if colors(C):
            break
        a = list(map(lambda x: int(x)-1, input().split()))

T, N, K = map(int, input().split())
for case in range(T):
    revenge_of_gorosort()
