/* 3.	Develop a code to implement a feature that highlights matching pairs of parentheses, brackets, and braces. A stack can be employed to track the opening and closing symbols and ensure proper nesting.
Sample input 1: {[()]}
Sample output 1: Parentheses are balanced.
Sample input 2: {[(}]}
Sample output 2: Parentheses are not balanced.
Sample input 3: {[()]
Sample output 3: Parentheses are not balanced.
*/

#include <stdio.h>
#define MAXSIZE 5
char stack[MAXSIZE];//stack is an integer array for implementing Stack...
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
/* Function to delete from the stack */
char pop(){
    if(isempty()){
        printf("Stack is EMPTY\n");
        return '0';
    }
    else{
    	//Write your code here...
        char ele = stack[tos];
        stack[tos] = 0;
        tos = tos - 1;
        return ele;
    }
}
/* Function to insert into the stack */
void push(char data){
    if(tos == MAXSIZE - 1){
        printf("Stack is FULL\n");
        return;
    }
    //Write your code here...
    else{
        tos = tos + 1;
        stack[tos] = data;
    }
}
// Check if an expression has balanced parentheses
int areParenthesesBalanced(const char *expression) {
    char popped;
    for (int i = 0; expression[i] != '\0'; i++) {
        //Write your code here...
        if (expression[i] == '{' || expression[i] == '[' || expression[i] == '(') {
            push(expression[i]);
        } else if (expression[i] == '}' || expression[i] == ']' || expression[i] == ')') {
            if (isempty()) {
                return FALSE;
            }
            popped = pop();
            if ((expression[i] == '}' && popped != '{') || 
                (expression[i] == ']' && popped != '[') || 
                (expression[i] == ')' && popped != '(')) {
                return FALSE;
            }
        }
    }
    if (isempty()) {
        return TRUE;
    } else {
        return FALSE;
    }
}

void main() {
    //const char *expression = "{[()]}";
    const char *expression = "{[(}]}";
    // const char *expression = "{[()]";
    if (areParenthesesBalanced(expression)) {
        printf("Parentheses are balanced.\n");
    } else {
        printf("Parentheses are not balanced.\n");
    }
}
