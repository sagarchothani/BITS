// 2.	Complete the following code to develop Queue using Array. Do not forget to print a relevant message when the Queue is full and the Queue is empty.

#include <stdio.h>

#define MAXSIZE  5

int queue[MAXSIZE];
int front = -1;
int rear = -1;

#define TRUE    (1)
#define FALSE   (0)

/* Check if the queue is empty */
int isEmpty(){
    //Write your code here...
    if (front == -1) 
        return TRUE;
    else 
        return FALSE;
}
/* Function to return the front element in the queue */
int front_ele(){
    //Write your code here...
    if (front == -1) 
        return -1;
    else 
        return queue[front];
}
/* Function to insert into the queue */
void enqueue(int data){
    //Write your code here...
    if (rear == MAXSIZE - 1)
        printf("QUEUE is Full... ERROR occured\n");
    else{
        rear += 1;
        queue[rear] = data;
    }

    if (front == -1){
        front = 0; 
    }
}
/* Function to delete from the queue */
int dequeue(){
    //Write your code here...
    int ele;
    if (isEmpty()){
        printf("QUEUE is Empty... ERROR occured\n");
        return -1;
    }
    else{
        ele = queue[front];
        queue[front] = 0;
        
        if (front == rear){
        front = -1;
        rear = -1;
        }
        else
            front += 1;

        return ele;
    }
}

void main(){
    enqueue(10);
    int data = dequeue();
    printf("Deleted element %d\n",data);
    data = dequeue();
        if (!isEmpty())
            printf("Deleted element %d\n",data);
    enqueue(21);
    enqueue(32);
    data = dequeue();
    printf("Deleted element %d\n",data);
    enqueue(43);
    enqueue(54);
    enqueue(65);
    enqueue(76);

    printf("Element at front of the queue: %d\n", front_ele());
    printf("Dequeued ele...\n");

    while(!isEmpty()) {
        data = dequeue();
        printf("%d\n",data);
    }
}
