//quicksort
#include<bits/stdc++.h>
using namespace std;
const int N=1e6+10;
mt19937 rd(chrono::steady_clock::now().time_since_epoch().count());
int n;
double A[N];
int get(int a,int b){
    if(a==b) return a;
    int t=rd();
    t=abs(t);
    return a+ t%(b-a+1);
}
void quick_sort(int l,int r){
    if(l>=r) return;
    int chot=get(l,r);
    swap(A[chot],A[r]);
    chot=r;
    int lefft=l;
    int right=r-1;
    while(lefft<=right){
        while(lefft<=right && A[lefft]<=A[chot]) lefft++;
        while(lefft<=right && A[right]>A[chot]) right--;
        if(lefft<=right){
            swap(A[lefft],A[right]);
            lefft++;
            right--;
        }
    }
    swap(A[chot],A[lefft]);
    quick_sort(l,lefft-1);
    quick_sort(lefft+1,r);
}
int main(){
    ios::sync_with_stdio(0);cin.tie(0);
    srand(time(NULL));
    cin>>n;
    for(int i=1; i<=n; i++) cin>>A[i];
    quick_sort(1,n);
    for(int i=1; i<=n; i++) cout<<A[i]<<' ';
    return 0;
}