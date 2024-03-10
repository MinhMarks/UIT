//merge_sort
#include <iostream>
#include <vector>  
using namespace std;
const int N=1e6+10;

int n;
double x;
vector<double> D[N*4];

void my_merge(vector<double> &c,vector<double> &b,vector<double> &a){
    double d=0;
    for(double v: b){
        while(d<a.size() && a[d]<=v){
            c.push_back(a[d]);
            d++;
        }
        c.push_back(v);
    }
    while(d<a.size()){
        c.push_back(a[d]);
        d++;
    }
}
void merge_sort(int id,int l,int r){
    if(l==r){
        cin>>x;
        D[id].push_back(x);
        return;
    }
    int mid=(l+r)>>1;
    merge_sort(id*2,l,mid);
    merge_sort(id*2+1,mid+1,r);
    my_merge(D[id],D[id*2],D[id*2+1]);
}
signed main(){
    ios::sync_with_stdio(0);cin.tie(0);
    cin>>n;
    merge_sort(1,1,n);
    for(double i=1; i<=n; i++){
        cout<<D[1][i-1]<<' ';
    }
    return 0;
}