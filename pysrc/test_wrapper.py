# _*_ coding : utf-8 _*_

from ctypes import *
import numpy as np

libpath = '/usr/local/lib/libenergymon-osp.so'

lib = cdll.LoadLibrary(libpath)

