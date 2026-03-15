#include <iostream>

using namespace std;

class Aidcar {
    private:
      string Brand;
      
    public:
      void ereke1 (string s){
          Brand = s;
      }
      string ereke2 (){
          return Brand;
      }
};

int main(){
    Aidcar aidobj1;
    aidobj1.ereke1("NISSAN SKYLINE GTR R35");
    cout << aidobj1.ereke2();
    return 0;
}