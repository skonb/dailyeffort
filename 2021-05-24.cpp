#include <stack>
#include <queue>
#include <cstdio>

using namespace std;

/*
int main(){
    stack<int> a;
    a.push(1);
    a.push(2);
    a.push(3);
    printf("%d\n",a.top());
    a.pop();
    printf("%d\n", a.top());
    a.pop();
    printf("%d\n",a.top());
    a.pop();
}
*/
/*
int main(){
    queue<int> a;
    a.push(1);
    a.push(2);
    a.push(3);
    printf("%d\n",a.front());
    a.pop();
    printf("%d\n", a.front());
    a.pop();
    printf("%d\n",a.front());
    a.pop();
}
*/
//目標 : 深さ優先探索で部分和問題を解く　
//ヒント : 探索手法は再帰で再現する
bool dfs(int*array, int pos,int n,int k,int cnt)
{
    if (pos==n+1){
        return false;
    }
    if (cnt==k){
        return true;
    }
    if (cnt>k){
        return false;
    }
    //pos番目の要素をつかう
    if (dfs(array,pos+1,n,k,cnt+array[pos])){
        return true;
    }
    //つかわない
    if (dfs(array,pos+1,n,k,cnt)){
        return true;
    }
    return false;
}

int main(){
    int n = 4;
    int a[4] = {1,2,4,7};
    int k = 13;

    //　全部の和<Kならfalse
    int sum = 0;
    for (int i = 0; i < n; i++)
    {
        sum += a[i];
    }
    if (sum<k){
        printf("No");
        return 0;
    }

    //探索を行う
    if(dfs(a,0,n,k,0)){
        printf("Yes");
    }else{
        printf("No");
    }
}