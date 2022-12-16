#include <stdio.h>
#include <stdlib.h>
#pragma warning (disable: 4996)
//Insertion Sort with Priority Queue
//2018312824 Chaeeun Ryu

int main() {
    int size;
    int count = 0, tmp = 0;
    scanf("%d", &size);
    int* arr = (int*)malloc(sizeof(int) * size);

    for (int i = 0;i < size;i++) {
        scanf("%d", &arr[i]);
    }

    for (int pass = 1; pass < size; pass++) {
        int save = arr[pass];
        int j = pass - 1;
        while (j >= 0 && arr[j] > save){
            arr[j + 1] = arr[j];
            j--;
        }//while
        arr[j + 1] = save;
        /*
        printf("\n %d iteration====\n", pass);
        for (int i = 0; i < size; i++) {
            printf(" %d", arr[i]);
        }
        printf("(inserted: %d)", save);*/
    }
    //printf("\n\n");
    for (int i = 0; i < size; i++) {
        printf(" %d", arr[i]);
    }
    
	return 0;
}