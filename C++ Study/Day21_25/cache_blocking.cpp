#include <stdlib.h>
#include <vector>
#include <algorithm>

using namespace std;

#define N 1024

void standard_triple_loop(int *A,int *B, int* C){
    //C = A*B
    
    for (int i = 0;i<N; ++i){
        for (int j = 0;j<N;++j){
            float sum= 0.0f;
            for (int k = 0;k<N;++k){
                sum += A[i*N+k]*B[k*N+j];
            }
            C[i*N+j] = sum;
        }
    }
}

void gemm_transposed(int* A, int* B, int* C){
    int *B_T = (int *)malloc(N*N*sizeof(int));

    if (B_T == NULL) return;

    for (int i= 0;i<N;++i){
        for (int j = 0; j < N; ++j) {
            B_T[j * N + i] = B[i * N + j];
        }
    }

    for (int i = 0;i<N; ++i){
        for (int j = 0;j<N;++j){
            float sum= 0.0f;
            for (int k = 0;k<N;++k){
                sum += A[i*N+k]*B_T[j*N+k];
            }
            C[i*N+j] = sum;
        }
    }
    
    free(B_T);
    
}

#define BLOCK_SIZE 64

void tiling(int* A, int* B, int* C){

    int *B_T = (int *)malloc(N*N*sizeof(int));

    if (B_T == NULL) return;

    for (int i= 0;i<N;++i){
        for (int j = 0; j < N; ++j) {
            B_T[j * N + i] = B[i * N + j];
        }
    }

    for (int bi = 0; bi < N; bi += BLOCK_SIZE) {
        for (int bj = 0; bj < N; bj += BLOCK_SIZE) {
            for (int bk = 0; bk < N; bk += BLOCK_SIZE) {
                
                
                for (int i = bi; i < min(bi + BLOCK_SIZE, N); ++i) {
                    for (int j = bj; j < min(bj + BLOCK_SIZE, N); ++j) {
                        float sum = 0; 
                        for (int k = bk; k < min(bk + BLOCK_SIZE, N); ++k) {
                            sum += A[i * N + k] * B_T[j * N + k];
                        }
                        C[i * N + j] += sum;
                    }
                }

                
            }
        }
    }
}

int main(){
    int *A = (int *)malloc(N*N*sizeof(int));
    int *B = (int *)malloc(N*N*sizeof(int));   
    int *C = (int *)malloc(N*N*sizeof(int));

    if (A == NULL || B == NULL || C == NULL) return 1;

    //init with numbers
    for (int i = 0;i<N*N;i++){
        A[i] = i%10;
        B[i] = i%5;
        C[i] = 0;
    }

    standard_triple_loop(A,B,C);

    gemm_transposed(A,B,C);

    tiling(A,B,C);

    free(A);free(B);free(C);

    return 0;

}