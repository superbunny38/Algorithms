#include <stdlib.h>
#include <vector>
#include <algorithm>
#include <chrono>
#include <iostream>

using namespace std;

#define N 1024

void standard_triple_loop(float *A,float *B, float* C){
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

void gemm_transposed(float* A, float* B, float* C){
    float *B_T = (float *)malloc(N*N*sizeof(float));

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

//memory optimization
void tiling(float* A, float* B, float* C){

    float *B_T = (float *)malloc(N*N*sizeof(float));

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
    free(B_T);
}

#include <immintrin.h>
//math optimization
void avx2_ace(float* A, float* B, float* C){

    float *B_T = (float *)malloc(N*N*sizeof(float));

    if (B_T == NULL) return;

    for (int i= 0;i<N;++i){
        for (int j = 0; j < N; ++j) {
            B_T[j * N + i] = B[i * N + j];
        }
    }

    for (int i = 0;i<N;++i){
        for (int j = 0;j<N;++j){
            __m256 sum_vec = _mm256_setzero_ps();

            for (int k = 0;k<N;k+=8){
                __m256 a_vec = _mm256_loadu_ps(&A[i*N+k]);
                __m256 b_vec = _mm256_loadu_ps(&B_T[j*N+k]);

                sum_vec = _mm256_fmadd_ps(a_vec,b_vec,sum_vec);
            }
            
            float total = 0.0f;

            __m128 low = _mm256_extractf128_ps(sum_vec,0);
            __m128 high = _mm256_extractf128_ps(sum_vec,1);

            __m128 temp_total = _mm_hadd_ps(low,high);
            temp_total = _mm_hadd_ps(temp_total, temp_total);
            total = _mm_cvtss_f32(temp_total);


            C[i*N+j] = total;
        }
    }
    free(B_T);
}

int main(){
    float *A = (float *)malloc(N*N*sizeof(float));
    float *B = (float *)malloc(N*N*sizeof(float));   
    float *C = (float *)malloc(N*N*sizeof(float));

    if (A == NULL || B == NULL || C == NULL) return 1;

    //init with numbers
    for (int i = 0;i<N*N;i++){
        A[i] = i%10;
        B[i] = i%5;
        C[i] = 0;
    }

    auto t1_start = chrono::high_resolution_clock::now();
    standard_triple_loop(A,B,C);
    auto t1_end = chrono::high_resolution_clock::now();
    chrono::duration<double,milli> t1_elapsed = t1_end-t1_start;
    cout << "[Standard triple loop] Waited " << t1_elapsed.count() << " ms\n";

    auto t2_start = chrono::high_resolution_clock::now();
    gemm_transposed(A,B,C);
    auto t2_end = chrono::high_resolution_clock::now();
    chrono::duration<double,milli> t2_elapsed = t2_end-t2_start;
    cout << "[GEMM] Waited "<<t2_elapsed.count()<<" ms\n";

    auto t3_start = chrono::high_resolution_clock::now();
    tiling(A,B,C);
    auto t3_end = chrono::high_resolution_clock::now();
    chrono::duration<double,milli> t3_elapsed = t3_end-t3_start;
    cout << "[Tiling] Waited "<<t3_elapsed.count()<<" ms\n";

    auto t4_start = chrono::high_resolution_clock::now();
    avx2_ace(A,B,C);
    auto t4_end = chrono::high_resolution_clock::now();
    chrono::duration<double,milli> t4_elapsed = t4_end-t4_start;
    cout << "[AVX2] Waitd "<<t4_elapsed.count()<<" ms\n";

    free(A);free(B);free(C);

    return 0;

}

/*
[Standard triple loop] Waited 3324.77 ms
[GEMM] Waited 1229.84 ms
[Tiling] Waited 763.056 ms
[AVX2] Waitd 156.314 ms
*/