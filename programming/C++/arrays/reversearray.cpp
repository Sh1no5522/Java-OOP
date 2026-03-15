#include<iostream>
#include<vector>

using namespace std;

int main(){
    int n , d = 0;
    vector<int> vec;
    cin >> n;
    int j = n;
    int arr[n], i;
    for(i=0; i<n; i++){
        cin>>arr[i];
    }
    for (j; j > -1; j--){
        if (arr[j] == n){
            continue;
        } else {
            vec.push_back(arr[j]);
        }
    }
    for (int i = 1; i < vec.size(); i++) {
        cout << vec[i] << " ";
    }
    return 0;
    
}