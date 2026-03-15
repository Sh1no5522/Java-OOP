#include <iostream>
#include <string>
#include <algorithm>
#include <numeric>
#include <vector>

using namespace std;
int f(int x, int y) {return x*10+y;}
int main(){
  vector<int> c;
  vector<int> r;
  int sum = 0;
  int sit = 0;
  string v;
  int sor = 0;
  char b;
  string a;
  cin >> a;
  for(int i = 0 ; i < a.length() ; i++){
      b = a[i];
      if (b == ';') {
      int sum=0;
      sum=accumulate(c.begin(),c.end(),sum,f);
      r.push_back(sum);
      continue;
    } else {
      c.push_back(b);
    } 
  }
  for(int i = 0 ; i < r.size() ; i++){
      sit += r[i];
  }
  int u = sit/r.size();
  while (u > 0){
      sor += u / 10;
      u = u / 10;
  }
  if(sor % 5 == 0){
      v = "TRUE";
  } else {
      v = "FALSE";
  }
  cout << u << "," << sor << ";" << v;
}