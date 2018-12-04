#include <stdio.h>
#include <stdint.h>
//#include <energymon-default.h>
#include <energymon-osp.h>
//#include <energymon-osp-polling.h>

int main(void)
{
energymon em;
uint64_t start_uj, end_uj;
//double start_uj, end_uj;

// get the energymon instance and initialize
//energymon_get_default(&em);
//energymon_get_osp_polling(&em);
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
int n = 10;
int c[n][n];
int d[n][n];
int i;
int j;
for(i = 0; i<n;i++ ){
    for(j = 0; j<n;j++ ){
	c[i][j] += a ;
	d[i][j] = a*a ;
	d[i][j] = c[i][j] * d[i][j];
	//printf(" a = %d\n", a);
    }
}
//
//end_uj = em.fread(&em);
end_uj = energymon_read_total_osp(&em);
printf(" %"PRIu64"\n", end_uj  );
//printf(" %a\n", end_uj  );
printf("Total energy for do_work() in microjoules: %"PRIu64"\n", end_uj - start_uj);
//printf("Total energy for do_work() in microjoules: %a\n", end_uj - start_uj);

// destroy the instance
//em.ffinish(&em);
energymon_finish_osp(&em);

return 0;

}
