#include <stdio.h>

#define MAX 20

/*=========================================================
    Kruskal's Algorithm (Minimum Spanning Tree)

    Time Complexity:
    Best Case    : O(E log E)
    Average Case : O(E log E)
    Worst Case   : O(E log E)

    Space Complexity:
    O(V)

    Where:
    V = Number of Vertices
    E = Number of Edges

    Note:
    Finds the Minimum Spanning Tree (MST)
    using Greedy Approach.
=========================================================*/

struct Edge
{
    int u, v, w;
};

struct Edge edge[MAX];

int parent[MAX];

// Find Parent
int find(int x)
{
    while(parent[x] != x)
        x = parent[x];

    return x;
}

// Union of Sets
void Union(int a, int b)
{
    parent[a] = b;
}

// Sort Edges by Weight
void sortEdges(int e)
{
    int i, j;
    struct Edge temp;

    for(i = 0; i < e - 1; i++)
    {
        for(j = 0; j < e - i - 1; j++)
        {
            if(edge[j].w > edge[j + 1].w)
            {
                temp = edge[j];
                edge[j] = edge[j + 1];
                edge[j + 1] = temp;
            }
        }
    }
}

/*======================= Main =======================*/
int main()
{
    int v, e;
    int i;
    int u, w;
    int totalCost = 0;

    printf("Enter number of vertices: ");
    scanf("%d", &v);

    printf("Enter number of edges: ");
    scanf("%d", &e);

    printf("Enter Source Destination Weight:\n");

    for(i = 0; i < e; i++)
    {
        scanf("%d %d %d",
              &edge[i].u,
              &edge[i].v,
              &edge[i].w);
    }

    // Initialize Parent
    for(i = 0; i < v; i++)
        parent[i] = i;

    sortEdges(e);

    printf("\nEdges in Minimum Spanning Tree:\n");

    for(i = 0; i < e; i++)
    {
        int p1 = find(edge[i].u);
        int p2 = find(edge[i].v);

        if(p1 != p2)
        {
            Union(p1, p2);

            printf("%d --> %d  Cost = %d\n",
                   edge[i].u,
                   edge[i].v,
                   edge[i].w);

            totalCost += edge[i].w;
        }
    }

    printf("\nMinimum Cost = %d\n", totalCost);

    return 0;
}