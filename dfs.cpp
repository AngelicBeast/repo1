#include <iostream>
#include<vector>
#include<map>
using namespace std;

int main(){
    map<int, vector<int>> d;
    vector <int> v;
    v.push_back(30);
    v.push_back(40);
    d[1]=v;
    std::map<std::string, int>::iterator it = d.begin();
    cout<<d[1];
}
