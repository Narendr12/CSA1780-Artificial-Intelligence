from heapq import heappop, heappush
def solve_puzzle(start):
    goal = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    def heuristic(board):
        return sum(
            abs((val - 1) % 3 - i % 3) + abs((val - 1) // 3 - i // 3)
            for i, val in enumerate(board) if val != 0
        )
    visited = set()
    pq = [(heuristic(start), 0, start)]
    while pq:
        _, steps, board = heappop(pq)
        if board == goal:
            return steps
        visited.add(tuple(board))
        zero_index = board.index(0)
        for direction in (-1, 1, -3, 3):
            new_zero_index = zero_index + direction
            if (
                0 <= new_zero_index < 9
                and not (zero_index % 3 == 2 and direction == 1)  
                and not (zero_index % 3 == 0 and direction == -1) 
            ):
                new_board = board[:]
                new_board[zero_index], new_board[new_zero_index] = new_board[new_zero_index], new_board[zero_index]
                if tuple(new_board) not in visited:
                    heappush(pq, (steps + 1 + heuristic(new_board), steps + 1, new_board))
    return -1 
print("Enter the puzzle board as 9 space-separated integers (0 for blank):")
start_state = list(map(int, input().strip().split()))

if len(start_state) == 9:
    result = solve_puzzle(start_state)
    print(f"Minimum moves to solve: {result}")
else:
    print("Invalid input! Please enter exactly 9 integers.")
