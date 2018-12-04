# _*_ coding : utf-8 _*_

from mod_cffi_emon import _emon

# gen instance & initialize module
em = _emon()

# args of _init_ is 
#   True  :print intermediate chape/value/etc
#   False :minimum print on terminal
em._init_(True)

# get address 
ad_em = em.get_address()
print(type(ad_em)) # DONOT comment out 

# getter and initialize
em.energymon_getinit_osp(ad_em)

# init Flag
t_start = em.energymon_read_total_osp(ad_em)
print('API Start Energy ==', t_start)

a=0.00
for i in range(1000):
  a += float(i * (i+1))
  # Interval FLAG
  # ==> DO NOT comment out interval read_total_energy API
  #     insert read-energy API is imperative to get total energy in the end 
  t_int = em.energymon_read_total_osp(ad_em)
  if i%50 == 0.00:
    print('  interval energy ==', t_int)

# END FLAG
t_end = em.energymon_read_total_osp(ad_em)
print('API End   Energy ==', t_end)

# terminate
em.energymon_osp.energymon_finish_osp(ad_em)

# SHOW Consumed energy between start-end FLAG
print('API Total Energy (micro J) ==',  t_end - t_start)

