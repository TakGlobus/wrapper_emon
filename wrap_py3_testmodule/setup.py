from distutils.core import setup, Extension

module1 = Extension('test',
                    sources = ['testpy3wrap.c'])

setup (name = 'TestMethod',
       version = '1.0',
       description = 'This is a demo package',
       ext_modules = [module1])
