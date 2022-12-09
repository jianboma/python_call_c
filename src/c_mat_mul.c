#include <stdio.h>
#include "c_mat_mul.h"

void mat_mul(
    const float * MatA, /* first matrix */
    const float * MatB, /* second matrix */
    float * ResMat,     /* resulting matrix */
    const int dim1,     /* first dimension of matrixA */
    const int dim2,     /* second dimension of matrixA */
    const int dim3      /* second dimension of matrixB */
    )
{
    // We should avoid allocate memory in the calling function
    // float **pp_resMat = malloc(sizeof(void *) * dim1);
    // // this is to record the real output
    // float *p_resMat = malloc(sizeof(float) * dim1 * dim3);

    // // allocate pp_resMat with pointers
    // for(int i=0; i<dim1; i++){
    //     pp_resMat[i] = &p_resMat[i*dim3]; // this allocates the address of the corresponding data to the pp_resMat pointer
    // }

    // now is the real computation
    for (int i=0; i<dim1; i++){
        for (int j=0; j<dim3; j++){
            ResMat[i*dim3+j] = 0; //initialize, may not be neccessary
            for (int n=0; n<dim2; n++){
                ResMat[i*dim3 + j] += MatA[i*dim1 + n] * MatB[n*dim3 + j]; // actually all of this can be parallely accelarated.
            }
        }
    }
    return ;
}