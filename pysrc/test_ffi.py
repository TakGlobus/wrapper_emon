# _*_ coding : utf-8 _*_

#
# ++ Documentation
#       
# ++ History
#
#     ver.    date        author        comment 
#  ----------------------------------------------------------------------------
#     0.0  2018/11/20  T.Kurihana   init-code of Python wrapper for c-based 
#                                   energymon API
#                                   

from cffi import FFI
import ctypes

#=================================
# ++ CFFI
#=================================

# Python Decoreation
def deco_sharp(func):
  def _wrapper(*args, **kwargs):
    _deco = "  ###  "
    _write= " Load Module == "
    res = _deco
    res += _write
    res += func(args[0], **kwargs)
    res += _deco
    return res
  return _wrapper


ffi = FFI()
@deco_sharp
def func_print(str):
    return str
print(func_print('ffi'))


ffi.cdef("""
  typedef struct energymon energymon;

  struct energymon{
   int finit;
   uint64_t fread;
   int  ffinish;
   char* fsource;
   uint64_t finterval;
   uint64_t fprecision;
   int fexclusive;
   void* state;
  };

""")

# builds and returns a new cdata object of the given ctype
em = ffi.new("energymon *")


# checkio: em
print(em)
print(ffi.typeof(em)) # ctype
print(' ========================')

# cast convert object type
em_cast = ctypes.cast(int(ffi.cast("intptr_t", em)), ctypes.c_char_p)

# checkio: em_cast type
print(em_cast)
print(type(em_cast))
print(' ========================')

# change type from c_char_p to bytes
em_cast = bytes(em_cast)
print(type(em_cast))

# creates a mutable character buffer
em_cast = ctypes.create_string_buffer(em_cast, 32)

# get address of object(buffer)
ad_em = ctypes.addressof(em_cast)
print(ad_em)

# open shared library
sharedlib_path = '/usr/local/lib/libenergymon-osp.so'
energymon_osp = ctypes.cdll.LoadLibrary(sharedlib_path) 

#================================================
# ++ Example of Energymon API 
#================================================

# Getter & initialize energymon
energymon_osp.energymon_get_osp(ad_em)
energymon_osp.energymon_init_osp(ad_em)

# Start FLAG
t_start = energymon_osp.energymon_read_total_osp(ad_em)
print('API Start Energy ==', t_start)

a=0.00
for i in range(1000):
  a += float(i * (i+1))
  # Interval FLAG
  # ==> DO NOT comment out interval read_total_energy API
  #     insert read-energy API is imperative to get total energy in the end 
  t_int = energymon_osp.energymon_read_total_osp(ad_em)
  if i%50 == 0.00:
    print('  interval energy ==', t_int)


# END FLAG
t_end = energymon_osp.energymon_read_total_osp(ad_em)
print('API End   Energy ==', t_end)

# SHOW Consumed energy between start-end FLAG
print('API Total Energy (micro J) ==',  t_end - t_start)

# Finilize 
energymon_osp.energymon_finish_osp(ad_em)

# Print Normal End
print(func_print('NORMAL END'))
