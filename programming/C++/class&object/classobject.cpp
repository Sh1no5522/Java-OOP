#include <iostream>

using namespace std;

class Aidcar {
    public:
      int Year;
      string Model;
      string Brand;
};

int main(){
    Aidcar aidobj1;
    aidobj1.Brand = "NISSAN SKYLINE";
    aidobj1.Model = "GTR R35";
    aidobj1.Year = 2013;
    cout << aidobj1.Brand << " " << aidobj1.Model << " " << aidobj1.Year << "+";
    return 0;
}