#include"bits/stdc++.h"
using namespace std;
int main(){
    int n;
    cout<<"Please enter the size of Array: ";
    cin>>n;
    int arr[n];
    cout<<"Please enter the Elements: ";
    for(int i=0;i<n;i++){
        cin>>arr[i];
    }
    for(int i=0;i<n;i++){
        for(int j=0;j<n-i-1;j++){
            if(arr[j]>arr[j+1]){
                int temp = arr[j];
                arr[j] = arr[j+1]; 
                arr[j+1] = temp;
            }
        }
    }
    cout<<"Sorted Array: "<<endl;
    for(int i=0;i<n;i++){
        cout<<arr[i]<<" ";
    }
    return 0;
}

/**
 * TC : O(n)^2
 * SC : O(1)
 */