#include <stdio.h>
#include <stdint.h>
#include </usr/local/include/energymon/energymon-osp.h>


// return strcut energumon
//struct em{
//  energymon em;
//};
energymon em;


// getter function
//void getter(struct em)
//void getter(energymon &em)
int getter(energymon em)
{
    energymon_get_osp(&em); 
}

// init function
//void finit(struct em)
//void finit(struct &em)
//void finit(energymon* em)
int finit(energymon em)
{
    energymon_init_osp(&em); 
}


// init function
//void finish(struct em)
//void finish(struct &em)
int finish(energymon em)
{
    energymon_finish_osp(&em);
}

// read function
//uint64_t em_read_flag(struct em){
//uint64_t em_read_flag(struct &em){
uint64_t em_read_flag(energymon em){
  energymon_read_total_osp(&em);
}


