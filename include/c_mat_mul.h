#include <stdio.h>

// it's always good to initialize the memory in upper function, and manipulate it in the calling function
void mat_mul(const float * MatA, const float * MatB, float * ResMat, const int dim1, const int dim2, const int dim3);
