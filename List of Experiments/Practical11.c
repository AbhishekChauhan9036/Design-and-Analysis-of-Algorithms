#include <stdio.h>

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

    printf("Enter number of vertices: ");
    scanf("%d", &n);

    printf("Enter Cost Matrix (Enter 9999 for Infinity):\n");

    for(i = 0; i < n; i++)
    {
        for(j = 0; j < n; j++)
        {
            scanf("%d", &graph[i][j]);
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

    printf("\nShortest Distance Matrix:\n");

    for(i = 0; i < n; i++)
    {
        for(j = 0; j < n; j++)
        {
            if(graph[i][j] == INF)
                printf("INF ");
            else
                printf("%4d ", graph[i][j]);
        }
        printf("\n");
    }

    return 0;
}