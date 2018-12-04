# _*_   coding : utf-8 _*_
"""
 This code leads unknown import error in FFI module
 Author T. Kurihana 2018/11/20
"""
import cffi
from cffi import FFI
#import numpy as np

#=================================
# ++ CFFI Equivalent
#=================================

ffi = FFI()

ffi.cdef("""
  int main_like(int argv, char *argv[]);
""")
#print(em)
#"""
# ++ original source
#
# typedef struct energymon energymon;
#
# struct energymon {
#   energymon_init finit;
#   energymon_read_total fread;
#   energymon_finish ffinish;
#   energymon_get_source fsource;
#   energymon_get_interval finterval;
#   energymon_get_precision fprecision;
#   energymon_is_exclusive fexclusive;
#   void* state;
# };
#"""
