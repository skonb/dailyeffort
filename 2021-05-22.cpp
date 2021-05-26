#include "stdio.h"
const int MAX_N = 500;
int g_memo[MAX_N]={0};
//階乗関数
int fact(int n){
    if (n==1){
        return 0;
    }
    return n*fact(n-1);
}

int fib(int n){
    if (n<=1){
        return 1;
    }
    return fib(n - 1) + fib(n - 2);
}

int memo_fib(int n)
{
    if (n<=1){
        return 1;
    }
    if (g_memo[n]!=1){
        return g_memo[n];
    }
    return memo_fib(n - 1) + memo_fib(n - 2);
}
int main (void){
    int arg=0;
    scanf("%d", &arg);
    printf("fact(%d)=%d\n", arg, fact(arg));
    printf("fib(%d)=%d\n",arg, memo_fib(arg));
    printf("fib(%d)=%d\n",arg, fib(arg));
}