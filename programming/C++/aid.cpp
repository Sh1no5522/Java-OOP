#include<iostream>
#include<vector>

using namespace std;

int main(){
    int n , l = 0;
    vector<int> vec;
    cin >> n;
    int j = 0;
    int arr[n], i;
    for(i=0; i<n; i++){
        cin>>arr[i];
    }
    for (int i = 0; i < n; i++) {
        if(vec[i] == l){
            continue;
        } else {
            vec.push_back(arr[i]);
        }
    }
    for (int i = 0; i < n; i++) {
        cout << vec[i] << " ";
    }
    
    return 0;
}