//
// wrapper for py3
// Py_InitModule is no longer available in py3
//
#include <python3.6/Python.h>

static PyObject * 
test_system(PyObject *self, PyObject *args){
  const char *command;
  int sts;

  // return NULL pointer in normal
  if(!PyArg_ParseTuple(args, "s", &command)){
    return NULL;
  }  

  sts = system(command);
return PyLong_FromLong(sts);
}

static PyMethodDef TestMethods[] = {
  {"system", test_system, METH_VARARGS, 
   "Exexcute a python command."},
  {NULL, NULL, 0, NULL}
};


static struct PyModuleDef testmodule = {
  PyModuleDef_HEAD_INIT,
  "test",  // name of module 
   NULL,   //
  -1,      // size of pre-interprenter 
   TestMethods  
};

PyMODINIT_FUNC
PyInit_test(void){
  return PyModule_Create(&testmodule);
}

int main(int argc , char *argv[]){
  wchar_t *program = Py_DecodeLocale(argv[0], NULL);
  if (program == NULL){
  fprintf(stderr, "Fatal error: cannot decode argv[0]\n");
  exit(1);
  } 


PyImport_AppendInittab("test", PyInit_test);

Py_SetProgramName(program);

Py_Initialize();

PyImport_ImportModule("test");

PyMem_RawFree(program);
return 0;


}

