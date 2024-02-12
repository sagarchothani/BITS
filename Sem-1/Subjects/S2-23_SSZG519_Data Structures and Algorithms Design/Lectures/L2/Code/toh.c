#include<stdio.h>
void TOH(int n,int A,int B,int C){
    if(n>0){
        TOH(n-1,A,C,B);
        printf("Move %dth disc from %d to %d\n",n,A,C);
        TOH(n-1,B,A,C);
    }
}
void main(){
    int n=3;
    int A=1,B=2,C=3;
    TOH(n,A,B,C);
}
