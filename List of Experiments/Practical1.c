#include <stdio.h>

#define MAX 100

/*=========================================================
    Bubble Sort
    Time Complexity:
    Best Case    : O(n)
    Average Case : O(n^2)
    Worst Case   : O(n^2)

    Space Complexity:
    O(1)
=========================================================*/
void bubbleSort(int a[], int n)
{
    int i, j, t;

    for(i=0;i<n-1;i++)
    {
        for(j=0;j<n-1-i;j++)
        {
            if(a[j]>a[j+1])
            {
                t=a[j];
                a[j]=a[j+1];
                a[j+1]=t;
            }
        }
    }
}

/*=========================================================
    Selection Sort
    Time Complexity:
    Best Case    : O(n^2)
    Average Case : O(n^2)
    Worst Case   : O(n^2)

    Space Complexity:
    O(1)
=========================================================*/
void selectionSort(int a[], int n)
{
    int i,j,min,t;

    for(i=0;i<n-1;i++)
    {
        min=i;

        for(j=i+1;j<n;j++)
        {
            if(a[j]<a[min])
                min=j;
        }

        t=a[i];
        a[i]=a[min];
        a[min]=t;
    }
}

/*=========================================================
    Insertion Sort
    Time Complexity:
    Best Case    : O(n)
    Average Case : O(n^2)
    Worst Case   : O(n^2)

    Space Complexity:
    O(1)
=========================================================*/
void insertionSort(int a[], int n)
{
    int i,j,key;

    for(i=1;i<n;i++)
    {
        key=a[i];
        j=i-1;

        while(j>=0 && a[j]>key)
        {
            a[j+1]=a[j];
            j--;
        }

        a[j+1]=key;
    }
}

/*=========================================================
    Merge Sort
    Time Complexity:
    Best Case    : O(n log n)
    Average Case : O(n log n)
    Worst Case   : O(n log n)

    Space Complexity:
    O(n)
=========================================================*/
void merge(int a[], int l, int m, int r)
{
    int b[MAX];
    int i=l,j=m+1,k=0;

    while(i<=m && j<=r)
    {
        if(a[i]<a[j])
            b[k++]=a[i++];
        else
            b[k++]=a[j++];
    }

    while(i<=m)
        b[k++]=a[i++];

    while(j<=r)
        b[k++]=a[j++];

    for(i=l,k=0;i<=r;i++,k++)
        a[i]=b[k];
}

void mergeSort(int a[], int l, int r)
{
    if(l<r)
    {
        int m=(l+r)/2;

        mergeSort(a,l,m);
        mergeSort(a,m+1,r);
        merge(a,l,m,r);
    }
}

/*=========================================================
    Quick Sort
    Time Complexity:
    Best Case    : O(n log n)
    Average Case : O(n log n)
    Worst Case   : O(n^2)

    Space Complexity:
    O(log n) (Recursion Stack)
=========================================================*/
int partition(int a[], int low, int high)
{
    int pivot=a[high];
    int i=low-1,j,t;

    for(j=low;j<high;j++)
    {
        if(a[j]<pivot)
        {
            i++;

            t=a[i];
            a[i]=a[j];
            a[j]=t;
        }
    }

    t=a[i+1];
    a[i+1]=a[high];
    a[high]=t;

    return i+1;
}

void quickSort(int a[], int low, int high)
{
    if(low<high)
    {
        int p=partition(a,low,high);

        quickSort(a,low,p-1);
        quickSort(a,p+1,high);
    }
}

/*================== Display Function ==================*/
void printArray(int a[], int n)
{
    int i;

    printf("\nSorted Array:\n");

    for(i=0;i<n;i++)
        printf("%d ",a[i]);

    printf("\n");
}

/*======================= Main =======================*/
int main()
{
    int a[MAX], n, i, ch;

    printf("Enter number of elements: ");
    scanf("%d",&n);

    printf("Enter elements:\n");
    for(i=0;i<n;i++)
        scanf("%d",&a[i]);

    printf("\nSorting Algorithms");
    printf("\n1. Bubble Sort");
    printf("\n2. Selection Sort");
    printf("\n3. Insertion Sort");
    printf("\n4. Merge Sort");
    printf("\n5. Quick Sort");

    printf("\n\nEnter your choice: ");
    scanf("%d",&ch);

    switch(ch)
    {
        case 1:
            bubbleSort(a,n);
            break;

        case 2:
            selectionSort(a,n);
            break;

        case 3:
            insertionSort(a,n);
            break;

        case 4:
            mergeSort(a,0,n-1);
            break;

        case 5:
            quickSort(a,0,n-1);
            break;

        default:
            printf("Invalid Choice");
            return 0;
    }

    printArray(a,n);

    return 0;
}