#include <iostream>
using namespace std;

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
    cout << v << " ";

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

        cout << v << " ";

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

    cout << "Enter number of vertices: ";
    cin >> n;

    cout << "Enter Adjacency Matrix:\n";
    for(i = 0; i < n; i++)
    {
        for(j = 0; j < n; j++)
        {
            cin >> graph[i][j];
        }
    }

    cout << "Enter starting vertex: ";
    cin >> start;

    cout << "\n1. DFS";
    cout << "\n2. BFS";

    cout << "\nEnter your choice: ";
    cin >> ch;

    for(i = 0; i < n; i++)
        visited[i] = 0;

    switch(ch)
    {
        case 1:
            cout << "\nDFS Traversal: ";
            DFS(start, n);
            break;

        case 2:
            cout << "\nBFS Traversal: ";
            BFS(start, n);
            break;

        default:
            cout << "Invalid Choice";
    }

    return 0;
}