#include <stdio.h>
#include <stdlib.h>

// Matrix printing routine
void print_matrix(double *A,int n) {
  int i,j;

  for (i=0; i < n; i++) {
    printf("  ");
    for (j=0; j < n; j++) {
      printf("%2.0lf ",A[i*n+j]);
    }
    printf("\n");
  }
  printf("-------------------------------\n");
  return;
}

// Main routine
int main(int argc, char **argv) {
  int N;
  int i,j,k;

  // Parse command-line arguments
  if (argc != 2) {
    fprintf(stderr,"Usage: %s <N>\n",argv[0]);
    exit(1);
  }

  if (sscanf(argv[1],"%d",&N) != 1) {
    fprintf(stderr,"Invalid argument\n");
    exit(1);
  }

  // Allocate matrix
  double *A = (double *)malloc(N*N*sizeof(double));

  // Fill-in matrix elements with particular
  // values so that the Gaussian elimination can
  // be easily computed analytically
  for (i=0; i < N; i++) {
    for (j=0; j < N; j++) {
      A[i*N+j] = 0.0;
      int min_i_j = (i < j ? i : j);
      for (k=0; k < min_i_j+1; k++) {
        A[i*N+j] += (double)(k+1)*(k+1);
      }
    }
  }
  
  // Print the matrix
  if (N < 10) {
    printf("Initial Matrix:\n");
    print_matrix(A,N);
  }
  
  // Do the Gaussian elimination
  for (k=0; k <N-1; k++) {
    if (N < 10) {
      printf("Updating column %d with the factors:\n",k);
    }
    // Update the k-th column
    for (i=k+1; i < N; i++) {
      A[i*N+k] = A[i*N+k] / A[k*N+k];
    }
    if (N < 10) {
      print_matrix(A,N);
      printf("Updating the lower-right matrix:\n");
    }
    for (j=k+1; j < N; j++) {
      for (i = k+1; i < N; i++) {
        A[i*N+j] -= A[i*N+k] * A[k*N+j];
      }
    }
    if (N < 10) {
      print_matrix(A,N);
    }
  }
 
  // Validate the results
  for (i=0; i < N; i++) {
    for (j=0; j < N; j++) {
      if ((i > j) && (A[i*N+j] != 1.0)) {
        fprintf(stderr,"** MISMATCH  ** A(%d,%d) = %.2lf but should be %.2lf\n", i,j, A[i*N+j],1.0);
      }
      if ((i <= j) && (A[i*N+j] != (double)(i+1)*(i+1))) {
        fprintf(stderr,"** MISMATCH  ** A(%d,%d) = %.2lf but should be %.2lf\n",i,j, A[i*N+j],(double)(i+1)*(i+1));
      }
    }
  }



  return 0;
}

