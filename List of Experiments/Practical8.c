#include <stdio.h>

#define MAX 10

int graph[MAX][MAX];
int visited[MAX];
int queue[MAX];
int front = 0, rear = -1;

/*=========================================================
    Depth First Search (DFS)

    Time Complexity:
    Best Case    : O(V + E)
    Average Case : O(V + E)
    Worst Case   : O(V + E)

    Space Complexity:
    O(V)

    Where:
    V = Number of Vertices
    E = Number of Edges
=========================================================*/
void DFS(int v, int n)
{
    int i;

    visited[v] = 1;
    printf("%d ", v);

    for(i = 0; i < n; i++)
    {
        if(graph[v][i] == 1 && visited[i] == 0)
            DFS(i, n);
    }
}

/*=========================================================
    Breadth First Search (BFS)

    Time Complexity:
    Best Case    : O(V + E)
    Average Case : O(V + E)
    Worst Case   : O(V + E)

    Space Complexity:
    O(V)

    Where:
    V = Number of Vertices
    E = Number of Edges
=========================================================*/
void BFS(int start, int n)
{
    int i;

    visited[start] = 1;
    queue[++rear] = start;

    while(front <= rear)
    {
        int v = queue[front++];

        printf("%d ", v);

        for(i = 0; i < n; i++)
        {
            if(graph[v][i] == 1 && visited[i] == 0)
            {
                visited[i] = 1;
                queue[++rear] = i;
            }
        }
    }
}

/*======================= Main =======================*/
int main()
{
    int n, i, j, start, ch;

    printf("Enter number of vertices: ");
    scanf("%d", &n);

    printf("Enter Adjacency Matrix:\n");
    for(i = 0; i < n; i++)
    {
        for(j = 0; j < n; j++)
        {
            scanf("%d", &graph[i][j]);
        }
    }

    printf("Enter starting vertex: ");
    scanf("%d", &start);

    printf("\n1. DFS");
    printf("\n2. BFS");

    printf("\nEnter your choice: ");
    scanf("%d", &ch);

    for(i = 0; i < n; i++)
        visited[i] = 0;

    switch(ch)
    {
        case 1:
            printf("\nDFS Traversal: ");
            DFS(start, n);
            break;

        case 2:
            printf("\nBFS Traversal: ");
            BFS(start, n);
            break;

        default:
            printf("Invalid Choice");
    }

    return 0;
}