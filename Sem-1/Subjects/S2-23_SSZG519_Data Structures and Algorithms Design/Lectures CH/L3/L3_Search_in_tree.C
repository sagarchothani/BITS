#include <stdio.h>
int a[16]={0,11,0,12,0,0,0,13,0,0,0,0,0,0,0,14};
int size = 16;
int search(int root, int key){
    printf("\n--search(%d,%d)--\n",root,key);
    int i = root;
    if(a[i]==key)
        return i;
    else{
        if(2*i <= size)
            search(2*i,key);
        if(((2*i)+1) <= size)
            search(((2*i)+1),key);
        else
            return 0;
    }
}
void main(){
    printf("Found at %d",search(1,13));
}

////////////////////////////////////////////////////////////////////////
// #include <stdio.h>

// int a[16] = {0, 11, 0, 12, 0, 0, 0, 13, 0, 0, 0, 0, 0, 0, 0, 14};
// int size = 16;

// int search(int root, int key) {
//     printf("\n--search(%d,%d)--\n", root, key);
//     int i = root;
//     if (a[i] == key)
//         return i;
//     else {
//         int result = 0;  // Variable to store the result of the search
//         if (2 * i <= size)
//             result = search(2 * i, key);  // Check the result of the left subtree search
//         if (result == 0 && ((2 * i) + 1) <= size)
//             result = search(((2 * i) + 1), key);  // Check the result of the right subtree search
//         return result;  // Return the result (0 if not found)
//     }
// }

// int main() {
//     int key = 13;
//     int result = search(1, key);
//     if (result != 0)
//         printf("Found at %d", result);
//     else
//         printf("Not found");
//     return 0;
// }
