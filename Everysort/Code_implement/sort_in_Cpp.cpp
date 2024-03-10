#include <iostream>
#include <algorithm> 
using namespace std;

const int N=1e6+10;
int n;
double A[N];
int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    cin>>n;
    for(int i=1; i<=n; i++){
        cin>>A[i];
    }
    sort(A+1,A+n+1);
    for(int i=1; i<=n; i++){
        cout<<A[i]<<' ';
    }
    return 0;
}