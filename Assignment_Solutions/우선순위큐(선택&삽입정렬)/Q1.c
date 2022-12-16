#include <stdio.h>
#include <stdlib.h>
#pragma warning (disable: 4996)
//2018312824 Chaeeun Ryu
//Inplace Insertion Sort with Priority Queue
int main() {
	int size;
    int count = 0, tmp = 0;
    scanf("%d",&size);
    int* arr = (int*)malloc(sizeof(int) * size);
   
    for (int i = 0;i < size;i++) {
        scanf("%d", &arr[i]);
    }
    for (int i = size-1; i > 0;i--) {
        int maxLoc = i;
        for (int j = 0;j < i;j++) {
            if (arr[j] > arr[maxLoc]) {
                maxLoc = j;
            }
        }//j
        tmp = arr[i];
        arr[i] = arr[maxLoc];
        arr[maxLoc] = tmp;
        /*
        printf("\n %d iteration====\n", size - (i));
        for (int i = 0; i < size; i++) {
            printf(" %d", arr[i]);
        }
        printf(" (swapped: %d %d)", arr[maxLoc], arr[i]);*/
        
    }
    //printf("\n========printing results=========\n");
    for (int i = 0; i < size; i++) {
        printf(" %d",arr[i]);
    }
	return 0; 
}

/*

int* arr = (int*)malloc(sizeof(int) * size);
    do {

        // Take input at position count
        // and increment count
        scanf_s("%d", arr[count++]);

        // If '\n' (newline) has occurred
        // or the whole array is filled,
        // then exit the loop

        // Otherwise, continue
    } while (getchar() != '\n' && count < size);

    for (int i = 0; i < size; i++) {
        printf("arr[%d] : %d\n", i, arr[i]);
    }
    */