#+--------------------------+
#| lab9_1.py - Isaiah Grace |
#+--------------------------+

# Task 1 - summate nums between N and 1, recursive

def recsum(N: int) -> int:
    return 0 if N==0 else N + recsum(N - 1)
