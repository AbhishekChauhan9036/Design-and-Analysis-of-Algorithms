#include<bits/stdc++.h>
using namespace std;
int main(){
    int n;
    cin>>n;
    int arr[n];
    for(int i=0; i<n; i++){
        cin>>arr[i];
    }

    cout<<"Sorted Elements are:"<<endl;
    for(int gap=n/2; gap>0; gap/=2){
        for(int i = gap; i<n; i++){
            int temp = arr[i];
            int j = i;
            while(j>= gap && arr[j-gap]>temp){
                arr[j] = arr[j - gap];
                j-=gap;
            }
            arr[j] = temp;
        }
    }
    
    for(int i=0;i<n;i++){
        cout<<arr[i]<<" ";
    }
    return 0;
}

/**
 * TC -
 *      Best Case - O(n log n)
 *      Average Case - O(n)^1.5
 *      Worst Case - O(n)^2
 * 
 * SC - O(1)
 */