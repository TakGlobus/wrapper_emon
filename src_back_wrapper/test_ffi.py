# _*_ coding : utf-8 _*_
from cffi import FFI
import ctypes
#import numpy as np
#=================================
# ++ CFFI Equivalent
#=================================

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

#ffi.cdef("""
#  typedef struct {
#  unsigned char r, g, b;
#  } pixel_t;
#""")
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
#  extern "Python" energymon get_energymon();

#ffi.cdef("""
#  typedef struct {
#   int finit;
#   uint64_t fread;
#   int  ffinish;
#   char* fsource;
#   uint64_t finterval;
#   uint64_t fprecision;
#   int fexclusive;
#   void* state;
#  } energymon;
#""")

em = ffi.new("energymon *")
#em = ffi.new("struct energymon *")
#em = ffi.cast('int', em )

#print(em)
#what_type = ffi.typeof(em)
#print(what_type) # ctype

#em_cast = ffi.cast("int",em )
#em_cast = int(ffi.cast("intptr_t",em ))
#print()
#print('type===', type('Hello'))
#buf = ctypes.create_string_buffer(32)
#print('Try buf==', buf)
#em_cast = str(em_cast)
#em_cast = ctypes.c_char_p(em_cast)

print(em)
print(ffi.typeof(em)) # ctype
print('1 ========================')


#em_cast = ctypes.cast(int(ffi.cast("intptr_t", em)), ctypes.c_void_p)
em_cast = ctypes.cast(int(ffi.cast("intptr_t", em)), ctypes.c_char_p)
print(em_cast)
print(type(em_cast))

#
#char="{em_cast}"
#em_cast = em_cast.encode('utf-8')
em_cast = bytes(em_cast)
print(type(em_cast))
#print('char is ', char)

#em = str(em)
#em = ctypes.c_char_p(em.encode('utf-8'))
em_cast = ctypes.create_string_buffer(em_cast, 32)
#bufr = ctypes.create_string_buffer(em, 32)
#print('2 ========================')
#print()
#print(bufr) # ctype
#stop
#print(ffi.typeof(bufr)) # ctype

#ad_em = prototype(em)
#ad_em = ffi.addressof(em)
ad_em = ctypes.addressof(em_cast)
print(ad_em)
#ad_em = ctypes.addressof(em.contents)

#ffi.set_source("_my_example", r"""
#  #include <stdio.h>
#  #include </usr/local/include/energymon/energymon.h>
#
#  energymon  em;
#""")




# open shared library
sharedlib_path = '/usr/local/lib/libenergymon-osp.so'
#energymon_osp = ffi.dlopen(sharedlib_path) 
energymon_osp = ctypes.cdll.LoadLibrary(sharedlib_path) 


energymon_osp.energymon_get_osp(ad_em)
energymon_osp.energymon_init_osp(ad_em)
#energymon_osp.energymon_get_osp(em)


t_start = energymon_osp.energymon_read_total_osp(ad_em)
print('API Start Energy ==', t_start)

a=0.00
for i in range(1000):
  a += float(i * (i+1))
  t_int = energymon_osp.energymon_read_total_osp(ad_em)
  if i%50 == 0.00:
    print('  interval energy ==', t_int)


t_end = energymon_osp.energymon_read_total_osp(ad_em)
print('API End   Energy ==', t_end)

print('API Total Energy (micro J) ==',  t_end - t_start)

energymon_osp.energymon_finish_osp(ad_em)

#ffi.new(" ")
#em = energymon_osp.finit()
#
#energymon_osp.energymon_get_osp(em)

# pointer address
#p_address = ffi.addressof()
#print(p_address)

#ffi.new("energymon_osp.energymon_get_osp(&energymon)")
#energymon_osp.energymon_get_osp(&energymon)
