/*
다차원 배열

*/

#include <iostream>

using namespace std;

void printMatrix(int mat[][3]){
    for (int i = 0;i<3;i++){
        for (int j = 0;j<3;j++){
            cout << mat[i][j]<<"\t";
        }
        cout << endl;
    }
}

void plusMatrix(int A[][3],int B[][3]){
    cout << "--- A+B ---"<<endl;
    for (int i = 0;i<3;i++){
        for (int j = 0;j<3;j++){
            cout << A[i][j]+B[i][j]<<"\t";
        }
        cout << endl;
    }
    cout << endl;
}

void minusMatrix(int A[][3],int B[][3]){
    cout << "--- A-B ---"<<endl;
    for (int i = 0;i<3;i++){
        for (int j = 0;j<3;j++){
            cout << A[i][j]-B[i][j] << "\t";
        }
        cout << endl;
    }
    cout << endl;
}



int main(){
    int matA[][3] = {{1,2,3,},{4,5,6},{7,8,9}};
    int matB[][3] = {{11,12,13},{14,15,16},{17,18,19}};

    plusMatrix(matA,matB);
    minusMatrix(matA,matB);
    printMatrix(matA);

    return 0;
}