//heapsort
#include <iostream>
#include <vector>  
using namespace std;

const int N=1e6+10;

double A[N];
int n;
void go(int sz,int id){
    int l=id*2;
    int r=id*2+1;
    int F=id;
    if(l<=sz && A[l]>A[F]){
        F=l;
    }
    if(r<=sz && A[r]>A[F]){
        F=r;
    }
    if(F==id) return;
    swap(A[F],A[id]);
    go(sz,F);
}
void build(){
    for(int i=n/2; i>=1; i--){
        go(n,i);
    }
}
void heap_sort(){
    for(int i=n; i>=1; i--){
        swap(A[i],A[1]);
        go(i-1,1);
    }
}
int main(){
    ios::sync_with_stdio(0);cin.tie(0);
    cin>>n;
    for(int i=1; i<=n; i++) cin>>A[i];
    build();
    heap_sort();
    for(int i=1; i<=n; i++) cout<<A[i]<<' ';
    return 0;
}