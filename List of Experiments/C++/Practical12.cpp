#include <iostream>
using namespace std;

#define MAX 10
#define INF 999999

/*=========================================================
    Travelling Salesman Problem (TSP)

    Time Complexity:
    Best Case    : O(n!)
    Average Case : O(n!)
    Worst Case   : O(n!)

    Space Complexity:
    O(n)

    Where:
    n = Number of Cities

    Note:
    Uses Backtracking to find the minimum cost
    Hamiltonian Cycle.
=========================================================*/

int graph[MAX][MAX];
int visited[MAX];
int n;
int minCost = INF;

// Recursive Function
void tsp(int city, int count, int cost)
{
    int i;

    // All cities visited
    if(count == n && graph[city][0] != 0)
    {
        cost += graph[city][0];

        if(cost < minCost)
            minCost = cost;

        return;
    }

    for(i = 0; i < n; i++)
    {
        if(!visited[i] && graph[city][i] != 0)
        {
            visited[i] = 1;

            tsp(i, count + 1, cost + graph[city][i]);

            visited[i] = 0;
        }
    }
}

/*======================= Main =======================*/
int main()
{
    int i, j;

    cout << "Enter number of cities: ";
    cin >> n;

    cout << "Enter Cost Matrix:\n";

    for(i = 0; i < n; i++)
    {
        for(j = 0; j < n; j++)
        {
            cin >> graph[i][j];
        }
    }

    visited[0] = 1;

    tsp(0, 1, 0);

    cout << "\nMinimum Tour Cost = " << minCost << endl;

    return 0;
}