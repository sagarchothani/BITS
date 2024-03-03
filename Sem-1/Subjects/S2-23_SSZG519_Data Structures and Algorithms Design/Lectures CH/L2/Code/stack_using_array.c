// 1.   Complete the following code to develop Stack using Array. Do not forget to print a relevant message when the stack is full and the stack is empty.

#include <stdio.h>
#define MAXSIZE 5
int stack[MAXSIZE];//stack is an integer array for implementing Stack...
int tos = -1;//tos is index to top of the stack...

#define TRUE    (1)
#define FALSE   (0)

/* Check if the stack is empty */
int isempty(){
    //Write your code here...
    if (tos == -1)
        return TRUE;
    else
        return FALSE;
}

/* Function to return the topmost element in the stack */
int top(){
    //Write your code here...
    if (tos == -1)
        return 0;
    else    
        return stack[tos];
}

/* Function to delete from the stack */
int pop(){
    //Write your code here...
    int ele;
    if (isempty())
        printf("Stack is Empty... ERROR occured\n");
    else{
        ele = stack[tos];
        stack[tos] = 0;
        tos = tos - 1;
        return ele;
    }
}

/* Function to insert into the stack */
void push(int data){
    //Write your code here...
    if (tos == MAXSIZE - 1)
        printf("Stack is Full... ERROR occured\n");
    else{
        tos = tos + 1;
        stack[tos] = data;
    }

}
/* Main function */
void main(){
   int data;
   push(10);
   data = pop();
   printf("Deleted element %d\n",data);
   data = pop();
   push(21);
   push(32);
   data = pop();
   printf("Deleted element %d\n",data);
   push(43);
   push(54);
   printf("Element at top of the stack: %d\n" ,top());
   printf("Deleting Elements: \n");

   while(!isempty()) {
      data = pop();
      printf("%d\n",data);
   }
}
