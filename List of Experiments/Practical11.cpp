#include <iostream>
#include <iomanip>
using namespace std;

#define MAX 10
#define INF 9999

/*=========================================================
    Floyd-Warshall Algorithm

    Time Complexity:
    Best Case    : O(V^3)
    Average Case : O(V^3)
    Worst Case   : O(V^3)

    Space Complexity:
    O(V^2)

    Where:
    V = Number of Vertices

    Note:
    Finds the shortest paths between all pairs
    of vertices in a weighted graph.
=========================================================*/

int main()
{
    int graph[MAX][MAX];
    int n;
    int i, j, k;

    cout << "Enter number of vertices: ";
    cin >> n;

    cout << "Enter Cost Matrix (Enter 9999 for Infinity):\n";

    for(i = 0; i < n; i++)
    {
        for(j = 0; j < n; j++)
        {
            cin >> graph[i][j];
        }
    }

    // Floyd-Warshall Algorithm
    for(k = 0; k < n; k++)
    {
        for(i = 0; i < n; i++)
        {
            for(j = 0; j < n; j++)
            {
                if(graph[i][k] + graph[k][j] < graph[i][j])
                {
                    graph[i][j] = graph[i][k] + graph[k][j];
                }
            }
        }
    }

    cout << "\nShortest Distance Matrix:\n";

    for(i = 0; i < n; i++)
    {
        for(j = 0; j < n; j++)
        {
            if(graph[i][j] == INF)
                cout << "INF ";
            else
                cout << setw(4) << graph[i][j] << " ";
        }
        cout << endl;
    }

    return 0;
}