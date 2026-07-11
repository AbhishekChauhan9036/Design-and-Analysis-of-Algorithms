#include <iostream>
using namespace std;

#define MAX 10
#define INF 9999

/*=========================================================
    Prim's Algorithm (Minimum Spanning Tree)

    Time Complexity:
    Best Case    : O(V^2)
    Average Case : O(V^2)
    Worst Case   : O(V^2)

    Space Complexity:
    O(V)

    Where:
    V = Number of Vertices

    Note:
    Finds the Minimum Spanning Tree (MST) of a
    connected weighted graph.
=========================================================*/

int main()
{
    int graph[MAX][MAX];
    int selected[MAX];
    int n, i, j;
    int edge = 0;
    int x, y;
    int min, cost = 0;

    cout << "Enter number of vertices: ";
    cin >> n;

    cout << "Enter Cost Adjacency Matrix:\n";

    for(i = 0; i < n; i++)
    {
        for(j = 0; j < n; j++)
        {
            cin >> graph[i][j];

            if(graph[i][j] == 0)
                graph[i][j] = INF;
        }
    }

    // Initially select first vertex
    for(i = 0; i < n; i++)
        selected[i] = 0;

    selected[0] = 1;

    cout << "\nEdges in Minimum Spanning Tree:\n";

    while(edge < n - 1)
    {
        min = INF;

        for(i = 0; i < n; i++)
        {
            if(selected[i])
            {
                for(j = 0; j < n; j++)
                {
                    if(!selected[j] && graph[i][j] < min)
                    {
                        min = graph[i][j];
                        x = i;
                        y = j;
                    }
                }
            }
        }

        cout << x << " --> " << y << "  Cost = " << graph[x][y] << endl;

        cost += graph[x][y];
        selected[y] = 1;
        edge++;
    }

    cout << "\nMinimum Cost = " << cost << endl;

    return 0;
}