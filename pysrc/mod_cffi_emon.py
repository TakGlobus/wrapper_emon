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
#     1.0  2018/11/20  T.Kurihana   objecte-oriented code based wrapper for  
#                                   energymon API
#
#
# ++ Bug Report
#   1. When user calls get_address, should add print(type(ad_em))
#      after the line. *ad_em => return of get_address
#
#   2. Interval energy sometimes showed minus values
#
# ++ TODO
#   ! Bug fix
#
#                                   
from cffi import FFI
import ctypes

#================================================
# ++ Decoration 
#================================================
def deco_sharp(func):
  def _wrapper(*args, **kwargs):
    _deco = "  ###  "
    if args[0] is 'ffi':
      _write= " Load Module == "
    elif args[0] is 'NORMAL END':
      _write= " Energymon Termination : "
    else:
      _write= " "
    res = _deco
    res += _write
    res += func(args[0], **kwargs)
    res += _deco
    return res
  return _wrapper

@deco_sharp
def func_print(str):
    return str


#================================================
# ++ Class _emon :   Energymon API 
#================================================
class _emon:

  def _init_(self, FLAG_debug=False):
    self.FLAG_debug = FLAG_debug
    pass

  def get_address(self):
      # load 
      ffi = FFI()
      # 
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

      if self.FLAG_debug is True:
        # checkio: em
        print(em)
        print(ffi.typeof(em)) # ctype
        print(' ========================')

      # cast convert object type
      em_cast = ctypes.cast(int(ffi.cast("intptr_t", em)), ctypes.c_char_p)

      if self.FLAG_debug is True:
        # checkio: em_cast type
        print(em_cast)
        print(type(em_cast))
        print(' ========================')

      # change type from c_char_p to bytes
      em_cast = bytes(em_cast)
      if self.FLAG_debug is True:
        print(type(em_cast)) 

      # creates a mutable character buffer
      em_cast = ctypes.create_string_buffer(em_cast, 32)

      # get address of object(buffer)
      ad_em = ctypes.addressof(em_cast)
      if self.FLAG_debug is True:
        print(ad_em)
        print('ad_em type ==', type(ad_em))

      return ad_em
  
  def energymon_getinit_osp(self, ad_em):
    # open shared library
    sharedlib_path = '/usr/local/lib/libenergymon-osp.so'
    energymon_osp = ctypes.cdll.LoadLibrary(sharedlib_path) 
    # DONOT DO like
    # seld.energymon_osp = ctypes ... ==> cause error
    self.energymon_osp = energymon_osp 

    # Getter & initialize energymon
    energymon_osp.energymon_get_osp(ad_em)
    energymon_osp.energymon_init_osp(ad_em)

  def energymon_read_total_osp(self,ad_em):
    # FLAG
    return self.energymon_osp.energymon_read_total_osp(ad_em)

  def energymon_finish_osp(self, ad_em):
    # Print Normal End
    print(func_print('NORMAL END'))
    # Finilize 
    return self.energymon_osp.energymon_finish_osp(ad_em)

