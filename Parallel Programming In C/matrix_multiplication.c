#include <stdio.h>
#include <time.h>
#include <stdlib.h>


clock_t base, total;
#define START_TIMER  base = clock();
#define PAUSE_TIMER  total += (clock() - base);


int main()
{
	srand(time(NULL));  

  int m, n, p, q, c, d, k,i, sum = 0;
  int *first[15000];
    for (i=0; i<15000; i++)
         first[i] = (int *)malloc(15000 * sizeof(int));
  int *second[15000];
    for (i=0; i<15000; i++)
         second[i] = (int *)malloc(15000 * sizeof(int));
     int *multiply[15000];
    for (i=0; i<15000; i++)
         multiply[i] = (int *)malloc(15000 * sizeof(int));


  printf("Enter the number of rows and columns of first matrix\n");
  scanf("%d%d", &m, &n);
  printf("Generating elements of first matrix\n");
 
  for (c = 0; c < m; c++)
    for (d = 0; d < n; d++)
      first[c][d]= rand() % 1000;
 
  printf("Enter the number of rows and columns of second matrix\n");
  scanf("%d%d", &p, &q);
 
  if (n != p)
    printf("Matrices with entered orders can't be multiplied with each other.\n");
  else
  {
    printf("Generating elements of second matrix\n");
    for (c = 0; c < p; c++)
      for (d = 0; d < q; d++)
      	second[c][d]= rand() % 1000;
     printf("Calculating\n");
 START_TIMER
    for (c = 0; c < m; c++) {
      for (d = 0; d < q; d++) {
        for (k = 0; k < p; k++) {
          sum = sum + first[c][k]*second[k][d];
        }
 
        multiply[c][d] = sum;
        sum = 0;
      }
    }
 
    printf("Product of entered matrices:-\n");
 
    for (c = 0; c < m; c++) {
      for (d = 0; d < q; d++)
        printf("%d\t", multiply[c][d]);
 	
      printf("\n");
    }
printf("\n");
    for (c = 0; c < m; c++) {
      for (d = 0; d < q; d++)
        printf("%d\t", second[c][d]);
 	
      printf("\n");
    }

printf("\n");
    for (c = 0; c < m; c++) {
      for (d = 0; d < q; d++)
        printf("%d\t", first[c][d]);
 	
      printf("\n");
    }



   PAUSE_TIMER

  printf(" Serial execution Time: %ld\n", total);
  }
 
  return 0;
}