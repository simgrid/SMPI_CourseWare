#!/usr/bin/env python3
import sys
import os
import subprocess
import math


###########################################
# Compile callibrating code
###########################################

callibrating_C_code = """
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <mpi.h>
#include <math.h>

#ifndef SIZE
#define SIZE 2000
#endif

static void matmult(double *A, double *B, double *C, int n) {
  int i,j,k;

  for (i=0; i < n; i++) {
    for (k=0; k < n; k++) {
      for (j=0; j < n; j++) {
        C[i*n+j] += A[i*n+k] * B[k*n+j];
      }
    }
  }
  return;
}


int main(int argc, char *argv[])
{
  MPI_Init(&argc, &argv);
 
  int my_rank;
  MPI_Comm_rank(MPI_COMM_WORLD,&my_rank);

  // Only process of rank 0 does something
  double sum;
  double start;
  double elapsed;

  if (my_rank == 0) {
    
    // Allocate matrices
    double *A = (double *)malloc(SIZE*SIZE*sizeof(double));
    double *B = (double *)malloc(SIZE*SIZE*sizeof(double));
    double *C = (double *)malloc(SIZE*SIZE*sizeof(double));
  
    // Fill in matrix values
    int i;
    for (i=0; i < SIZE*SIZE; i++) {
      A[i] = 2.0*i/(SIZE*SIZE);
      B[i] = -1.0*i/(SIZE*SIZE);
      C[i] = 0.0;
    }
  
    // Multiply matrices
    start = MPI_Wtime();
    matmult(A,B,C,SIZE);
  
    // Compute the sum (to avoid compiler optimization)
    sum=0;
    for (i=0; i < SIZE*SIZE; i++) {
      sum += C[i];
    }
    elapsed = MPI_Wtime() - start;

  }
  MPI_Barrier(MPI_COMM_WORLD);

  if (my_rank == 0) {
    // Print the wall-clock time and the sum
    printf("%.5lf\\t%0.2lf\\n", elapsed, sum);
  }

  // Clean-up
  MPI_Finalize();

  return 0;
}
"""

SIZE=2000

callibrating_code_filename = "/tmp/callibrating_code.c"
fh = open(callibrating_code_filename, 'w')
fh.write(callibrating_C_code)
fh.close()
error_code = os.system("smpicc -Ofast "+"-DSIZE="+str(SIZE)+" "+callibrating_code_filename+" -o /tmp/callibration_code")
if (error_code != 0):
	sys.stderr.write("Can't compile '"+callibrating_code_filename+"'... aborting\n")
	exit(1)
sys.stderr.write("Callibrating code compiled\n")


###########################################
# Create XML platform file (one host)
###########################################
platform_filename = "/tmp/platform_one_host.xml"
fh = open(platform_filename, 'w')
fh.write("<?xml version='1.0'?>\n<!DOCTYPE platform SYSTEM \"http://simgrid.gforge.inria.fr/simgrid/simgrid.dtd\">\n<platform version=\"4.1\">\n<AS id=\"AS0\" routing=\"Full\">\n")
fh.write("  <host id=\"host-0\" speed=\"200Gf\"/>\n")
fh.write("</AS>\n</platform>\n")
fh.close()
sys.stderr.write("One-host XML platform file generated\n")

###########################################
# Create host file (one host)
###########################################
hostfile_filename = "/tmp/hostfile_one_host"
fh = open(hostfile_filename, 'w')
fh.write("host-0\n")
fh.close()
sys.stderr.write("One-host hostfile generated\n")

###########################################
# Binary search to find the running power
###########################################

sys.stderr.write("Initiating binary search...\n")

# Coarse approximation of the traget simulated time
desired_simulated_gflops_rate=200.0
number_gflop = (3.0 * SIZE * SIZE * SIZE + SIZE * SIZE) / (1000000000.0)
target = number_gflop / desired_simulated_gflops_rate

# Initial bounds for the binary search
low = 0
high = 500000000000.0

while (True):

	attempt =  (low + high) / 2

	# Run the code
	FNULL = open(os.devnull, 'w')
	output = subprocess.check_output(["smpirun","--cfg=smpi/host-speed:"+str(attempt)+"f","-platform",platform_filename,"-hostfile",hostfile_filename,"-np","1","/tmp/callibration_code"],stderr = FNULL, encoding='UTF-8')
	FNULL.close()

	# Get the wall-clock time
	simulated_wallclock = float(output.split('\t')[0])

	print("candidate value: "+str(("%.3f" % attempt))+"\t-->  wallclock = "+str(("%.3f" % simulated_wallclock))+" (target ="+str(("%.3f" % target))+")")

	if (simulated_wallclock < target):
		low = attempt
	else:
		high = attempt
	

	if ((abs(simulated_wallclock - target) < 0.001) or (abs(high - low) < 100)):
		break

print("Run smpirun with --cfg=smpi/host-speed:"+str(("%.3f" % attempt))+"\n")
print("  (and run smpicc with -Ofast)\n")

