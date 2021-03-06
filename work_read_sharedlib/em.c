#include <stdio.h>
#include <stdint.h>
#include </usr/local/include/energymon/energymon.h>
#include </usr/local/include/energymon/energymon-osp.h>
//#include <ctime>

int main(void)
{
energymon em;
uint64_t start_uj, end_uj;
uint64_t interval_uj;
uint64_t inside;
char* em_src;
char buffer[100];
int size = sizeof(buffer);
int exc;

// get the energymon instance and initialize
energymon_get_osp(&em);
//em.finit(&em);
energymon_init_osp(&em);

// profile application function
//start_uj = em.fread(&em);
start_uj = energymon_read_total_osp(&em);
printf(" %"PRIu64"\n", start_uj  );
//printf(" %a\n", start_uj  );


//do_work();
int a = 1;
int n = 100;
int c[n][n];
int d[n][n];
int i;
int j;
for(i = 0; i<n;i++ ){
    for(j = 0; j<n;j++ ){
	printf("this is n: %d\n",n);
	c[i][j] += a ;
	d[i][j] = a*a ;
	d[i][j] = c[i][j] * d[i][j];
        inside = energymon_read_total_osp(&em);
        printf("Run %d, Energy:  %"PRIu64"\n", i,inside  );
	//printf(" a = %d\n", a);
    }
}

// interrval
interval_uj = energymon_get_interval_osp(&em);
printf("Get the refresh interval for sensor  in microseconds: %"PRIu64"\n", interval_uj);


//
//end_uj = em.fread(&em);
end_uj = energymon_read_total_osp(&em);
printf(" %"PRIu64"\n", end_uj  );
//printf(" %a\n", end_uj  );

// src
em_src = energymon_get_source_osp(buffer, size);
printf("Energymon get source osp %s \n",  em_src);

// exclusive
exc = energymon_is_exclusive_osp();
printf("Energymon exlusive osp  %d \n", exc);

// Check Energy 
printf("Total energy for do_work() in microjoules: %"PRIu64"\n", end_uj - start_uj);
//printf("Total energy for do_work() in microjoules: %a\n", end_uj - start_uj);

// destroy the instance
//em.ffinish(&em);
energymon_finish_osp(&em);

return 0;

}
