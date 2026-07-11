# =========================================================
# Travelling Salesman Problem (TSP)
#
# Time Complexity:
# Best Case    : O(n!)
# Average Case : O(n!)
# Worst Case   : O(n!)
#
# Space Complexity:
# O(n)
#
# Where:
# n = Number of Cities
#
# Note:
# Uses Backtracking to find the minimum cost
# Hamiltonian Cycle.
# =========================================================

INF = float('inf')


# Recursive Function
def tsp(graph, visited, city, count, cost, n):
    global min_cost

    # All cities visited
    if count == n and graph[city][0] != 0:
        cost += graph[city][0]
        min_cost = min(min_cost, cost)
        return

    for i in range(n):
        if not visited[i] and graph[city][i] != 0:
            visited[i] = True

            tsp(graph, visited, i, count + 1, cost + graph[city][i], n)

            visited[i] = False


# ======================= Main =======================
def main():
    global min_cost

    n = int(input("Enter number of cities: "))

    print("Enter Cost Matrix:")

    graph = []
    for _ in range(n):
        row = list(map(int, input().split()))
        graph.append(row)

    visited = [False] * n
    visited[0] = True

    min_cost = INF

    tsp(graph, visited, 0, 1, 0, n)

    print(f"\nMinimum Tour Cost = {min_cost}")


if __name__ == "__main__":
    main()