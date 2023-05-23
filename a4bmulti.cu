#include<stdio.h>
#include<cuda.h>
#define row1 2 /* Number of rows of first matrix */
#define col1 3 /* Number of columns of first matrix */
#define row2 3 /* Number of rows of second matrix */
#define col2 2 /* Number of columns of second matrix */

__global__ void matproduct(int *l,int *m, int *n)
{
    int x=blockIdx.x;
    int y=blockIdx.y;
    int k;
  
n[col2*y+x]=0;
for(k=0;k<col1;k++)
   {
    n[col2*y+x]=n[col2*y+x]+l[col1*y+k]*m[col2*k+x];
   }
}

int main()
{
    int a[row1][col1];
    int b[row2][col2];
    int c[row1][col2];
    int *d,*e,*f;
    int i,j;

    printf("\n Enter elements of first matrix of size 2*3\n");
    for(i=0;i<row1;i++)
    {
        for(j=0;j<col1;j++)
            {
                scanf("%d",&a[i][j]);
            }
    }
    printf("\n Enter elements of second matrix of size 3*2\n");
        for(i=0;i<row2;i++)
        {
            for(j=0;j<col2;j++)
                {
                    scanf("%d",&b[i][j]);
                }
        }

    cudaMalloc((void **)&d,row1*col1*sizeof(int));
    cudaMalloc((void **)&e,row2*col2*sizeof(int));
    cudaMalloc((void **)&f,row1*col2*sizeof(int));

 cudaMemcpy(d,a,row1*col1*sizeof(int),cudaMemcpyHostToDevice);
 cudaMemcpy(e,b,row2*col2*sizeof(int),cudaMemcpyHostToDevice);

dim3 grid(col2,row1);
/* Here we are defining two dimensional Grid(collection of blocks) structure. Syntax is dim3 grid(no. of columns,no. of rows) */

    matproduct<<<grid,1>>>(d,e,f);

 cudaMemcpy(c,f,row1*col2*sizeof(int),cudaMemcpyDeviceToHost);
    printf("\nProduct of two matrices:\n ");
    for(i=0;i<row1;i++)
    {
        for(j=0;j<col2;j++)
        {
              printf("%d\t",c[i][j]);
        }
        printf("\n");
    }

    cudaFree(d);
    cudaFree(e);
    cudaFree(f);

    return 0;
}
// #include <cuda_runtime.h>
// #include <iostream>

// __global__ void matmul(int* A, int* B, int* C, int N) {
//     int Row = blockIdx.y*blockDim.y+threadIdx.y;
//     int Col = blockIdx.x*blockDim.x+threadIdx.x;
//     if (Row < N && Col < N) {
//         int Pvalue = 0;
//         for (int k = 0; k < N; k++) {
//             Pvalue += A[Row*N+k] * B[k*N+Col];
//         }
//         C[Row*N+Col] = Pvalue;
//     }
// }

// int main() {
//     int N = 512;
//     int size = N * N * sizeof(int);
//     int* A, * B, * C;
//     int* dev_A, * dev_B, * dev_C;
//     cudaMallocHost(&A, size);
//     cudaMallocHost(&B, size);
//     cudaMallocHost(&C, size);
//     cudaMalloc(&dev_A, size);
//     cudaMalloc(&dev_B, size);
//     cudaMalloc(&dev_C, size);

//     // Initialize matrices A and B
//     for (int i = 0; i < N; i++) {
//         for (int j = 0; j < N; j++) {
//             A[i*N+j] = i*N+j;
//             B[i*N+j] = j*N+i;
//         }
//     }

//     cudaMemcpy(dev_A, A, size, cudaMemcpyHostToDevice);
//     cudaMemcpy(dev_B, B, size, cudaMemcpyHostToDevice);

//     dim3 dimBlock(16, 16);
//     dim3 dimGrid(N/dimBlock.x, N/dimBlock.y);

//     matmul<<<dimGrid, dimBlock>>>(dev_A, dev_B, dev_C, N);

//     cudaMemcpy(C, dev_C, size, cudaMemcpyDeviceToHost);

//     // Print the result
//     for (int i = 0; i < 10; i++) {
//         for (int j = 0; j < 10; j++) {
//             std::cout << C[i*N+j] << " ";
//         }
//         std::cout << std::endl;
//     }

//     // Free memory
//     cudaFree(dev_A);
//     cudaFree(dev_B);
//     cudaFree(dev_C);
//     cudaFreeHost(A);
//     cudaFreeHost(B);
//     cudaFreeHost(C);

//     return 0;
// }
