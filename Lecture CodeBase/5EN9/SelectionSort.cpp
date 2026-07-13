#include"bits/stdc++.h"
using namespace std;
int main(){
    int n, min = 0;
    cout<<"Please enter the size of Array: ";
    cin>>n;
    int arr[n];
    cout<<"Please enter the Elements: ";
    for(int i=0; i<n; i++){
        cin>>arr[i];
    }
/**
 *     for(int i=0; i<n; i++){
        min = i;
        for(int j=i+1; j<n; j++){
            if(arr[j] < arr[min]){
                min = j;
            }
            int temp = arr[i];
            arr[i] = arr[min];
            arr[min] = temp;
        }
    }
 */

    for(int i=0; i<n-1; i++){
        for(int j=i+1; j<n; j++){
            if(arr[i] > arr[j]){
                int temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }
    }
    cout<<"Sorted Array: "<<endl;
    for(int i=0; i<n; i++){
        cout<<arr[i]<<" ";
    }
    return 0;
}

/**
 * TC : O(n)^2
 * SC : O(1)
 */