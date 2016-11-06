
#include "dtoolbase.h"
#include "interrogate_request.h"

#include "py_panda.h"

extern LibraryDef libp3distort_moddef;
extern void Dtool_libp3distort_RegisterTypes();
extern void Dtool_libp3distort_ResolveExternals();
extern void Dtool_libp3distort_BuildInstants(PyObject *module);

#if PY_MAJOR_VERSION >= 3 || !defined(NDEBUG)
#ifdef _WIN32
extern "C" __declspec(dllexport) PyObject *PyInit_fx();
#elif __GNUC__ >= 4
extern "C" __attribute__((visibility("default"))) PyObject *PyInit_fx();
#else
extern "C" PyObject *PyInit_fx();
#endif
#endif
#if PY_MAJOR_VERSION < 3 || !defined(NDEBUG)
#ifdef _WIN32
extern "C" __declspec(dllexport) void initfx();
#elif __GNUC__ >= 4
extern "C" __attribute__((visibility("default"))) void initfx();
#else
extern "C" void initfx();
#endif
#endif

#if PY_MAJOR_VERSION >= 3
static struct PyModuleDef py_fx_module = {
  PyModuleDef_HEAD_INIT,
  "fx",
  NULL,
  -1,
  NULL,
  NULL, NULL, NULL, NULL
};

PyObject *PyInit_fx() {
  PyImport_Import(PyUnicode_FromString("panda3d.core"));
  Dtool_libp3distort_RegisterTypes();
  Dtool_libp3distort_ResolveExternals();

  LibraryDef *defs[] = {&libp3distort_moddef, NULL};

  PyObject *module = Dtool_PyModuleInitHelper(defs, &py_fx_module);
  if (module != NULL) {
    Dtool_libp3distort_BuildInstants(module);
  }
  return module;
}

#ifndef NDEBUG
void initfx() {
  PyErr_SetString(PyExc_ImportError, "panda3d.fx was compiled for Python " PY_VERSION ", which is incompatible with Python 2");
}
#endif
#else  // Python 2 case

void initfx() {
  PyImport_Import(PyUnicode_FromString("panda3d.core"));
  Dtool_libp3distort_RegisterTypes();
  Dtool_libp3distort_ResolveExternals();

  LibraryDef *defs[] = {&libp3distort_moddef, NULL};

  PyObject *module = Dtool_PyModuleInitHelper(defs, "panda3d.fx");
  if (module != NULL) {
    Dtool_libp3distort_BuildInstants(module);
  }
}

#ifndef NDEBUG
PyObject *PyInit_fx() {
  PyErr_SetString(PyExc_ImportError, "panda3d.fx was compiled for Python " PY_VERSION ", which is incompatible with Python 3");
  return (PyObject *)NULL;
}
#endif
#endif

