#include <stdlib.h>
#include <vector>
#include <algorithm>
#include <chrono>
#include <iostream>
#include <cstdlib>

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
    size_t bytes = N*N*sizeof(float);
    float *B_T = (float *)aligned_alloc(32,bytes);

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

    size_t bytes = N*N*sizeof(float);
    float *B_T = (float *)aligned_alloc(32,bytes);

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

    size_t bytes = N*N*sizeof(float);
    float *B_T = (float *)aligned_alloc(32,bytes);

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


void avx2_ace_faster(float* A, float* B, float* C){

    size_t bytes = N*N*sizeof(float);
    float *B_T = (float *)aligned_alloc(32,bytes);

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
                __m256 a_vec = _mm256_load_ps(&A[i*N+k]);//_mm256_load_ps (load aligned) is faster than _mm256_loadu_ps because the CPU doesn't have to do safety checks.
                __m256 b_vec = _mm256_load_ps(&B_T[j*N+k]);//_mm256_load_ps (load aligned) is faster than _mm256_loadu_ps because the CPU doesn't have to do safety checks.

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

#include <memory>
void avx2_ace_unique_ptr(float* A, float* B, float* C){
    size_t bytes = N*N*sizeof(float);
    unique_ptr<float[],decltype(&free)> B_T(
        static_cast<float*>(aligned_alloc(32,bytes)),//the pointer
        &free//the clean up function
    );

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
                __m256 a_vec = _mm256_load_ps(&A[i*N+k]);//_mm256_load_ps (load aligned) is faster than _mm256_loadu_ps because the CPU doesn't have to do safety checks.
                __m256 b_vec = _mm256_load_ps(&B_T[j*N+k]);//_mm256_load_ps (load aligned) is faster than _mm256_loadu_ps because the CPU doesn't have to do safety checks.

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
}


int main(){
    // float *A = (float *)malloc(N*N*sizeof(float));
    // float *B = (float *)malloc(N*N*sizeof(float));   
    // float *C = (float *)malloc(N*N*sizeof(float));

    size_t bytes = N*N*sizeof(float);
    float *A = (float *)aligned_alloc(32,bytes);
    float *B = (float *)aligned_alloc(32,bytes);
    float *C = (float *)aligned_alloc(32,bytes);

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
    cout << "[AVX2] Waited "<<t4_elapsed.count()<<" ms\n";

    auto t5_start = chrono::high_resolution_clock::now();
    avx2_ace_faster(A,B,C);
    auto t5_end = chrono::high_resolution_clock::now();
    chrono::duration<double,milli> t5_elapsed = t5_end-t5_start;
    cout << "[AVX2 + _mm256_load_ps] Waited "<<t5_elapsed.count()<<" ms\n";

    auto t6_start = chrono::high_resolution_clock::now();
    avx2_ace_unique_ptr(A,B,C);
    auto t6_end = chrono::high_resolution_clock::now();
    chrono::duration<double,milli> t6_elapsed = t6_end-t6_start;
    cout << "[AVX2 + unique_ptr] Waited "<<t6_elapsed.count()<<" ms\n";


    free(A);free(B);free(C);

    return 0;

}

/*
[Standard triple loop] Waited 5120.62 ms
[GEMM] Waited 976.195 ms
[Tiling] Waited 641.961 ms
[AVX2] Waited 137.836 ms
[AVX2 + _mm256_load_ps] Waited 137.198 ms
[AVX2 + unique_ptr] Waited 133.831 ms
*/