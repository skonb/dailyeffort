#include<iostream>
#include<string>
#include <list>
using namespace std;

int main() {
    int N;
    cin >> N;
    string S;
    cin >> S;

    string Srev = S;
    reverse(Srev.begin(), Srev.end());
    int l = 0;
    int r = 0;
    list<char> T;

    for (int i = 0; i < N; i++)
    {
        string S_sub = S.substr(l, N - i);
        string Srev_sub = Srev.substr(r, N - i);
        if (S_sub < Srev_sub){
            T.push_back(S_sub[0]);
            l++;
        }else{
            T.push_back(Srev_sub[0]);
            r++;
        }
            
    }
    for (string t:T){
        cout << t ; 
    }
    cout << endl;
}
