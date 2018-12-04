#include <stdio.h>
#include <stdint.h>
#include </usr/local/include/energymon/energymon.h>
#include </usr/local/include/energymon/energymon-osp.h>


// return strcut energumon
//struct em{
//  energymon em;
//};

// set global struct
energymon em;

//energymon get_em(void)
//{
//  energymon em;
//  return em;
//}


// getter function
//void getter(struct em)
//void getter(energymon &em)
//int getter(energymon em)
int getter(void)
//void getter(energymon em)
{
    energymon_get_osp(&em); 
}

// init function
//void finit(struct em)
//void finit(struct &em)
//void finit(energymon* em)
//int emfinit(energymon em)
int emfinit(void)
//void em_finit(energymon em)
{
    energymon_init_osp(&em); 
}


// init function
//void finish(struct em)
//void finish(struct &em)
//void em_finish(energymon em)
//int emfinish(energymon em)
int emfinish(void)
{
    energymon_finish_osp(&em);
}

// read function
//uint64_t em_read_flag(struct em){
//uint64_t em_read_flag(struct &em){
//uint64_t em_read_flag(energymon em){
uint64_t em_read_flag(void){
  uint64_t uj;
  uj = energymon_read_total_osp(&em);
  return uj;
}


int main(void)
{
  printf("  hello em");
}

