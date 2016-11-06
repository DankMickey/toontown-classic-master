
#include "dtoolbase.h"
#include "interrogate_request.h"

#include "py_panda.h"

extern LibraryDef libpandaode_moddef;
extern void Dtool_libpandaode_RegisterTypes();
extern void Dtool_libpandaode_ResolveExternals();
extern void Dtool_libpandaode_BuildInstants(PyObject *module);

#if PY_MAJOR_VERSION >= 3 || !defined(NDEBUG)
#ifdef _WIN32
extern "C" __declspec(dllexport) PyObject *PyInit_ode();
#elif __GNUC__ >= 4
extern "C" __attribute__((visibility("default"))) PyObject *PyInit_ode();
#else
extern "C" PyObject *PyInit_ode();
#endif
#endif
#if PY_MAJOR_VERSION < 3 || !defined(NDEBUG)
#ifdef _WIN32
extern "C" __declspec(dllexport) void initode();
#elif __GNUC__ >= 4
extern "C" __attribute__((visibility("default"))) void initode();
#else
extern "C" void initode();
#endif
#endif

#if PY_MAJOR_VERSION >= 3
static struct PyModuleDef py_ode_module = {
  PyModuleDef_HEAD_INIT,
  "ode",
  NULL,
  -1,
  NULL,
  NULL, NULL, NULL, NULL
};

PyObject *PyInit_ode() {
  PyImport_Import(PyUnicode_FromString("panda3d.core"));
  Dtool_libpandaode_RegisterTypes();
  Dtool_libpandaode_ResolveExternals();

  LibraryDef *defs[] = {&libpandaode_moddef, NULL};

  PyObject *module = Dtool_PyModuleInitHelper(defs, &py_ode_module);
  if (module != NULL) {
    Dtool_libpandaode_BuildInstants(module);
  }
  return module;
}

#ifndef NDEBUG
void initode() {
  PyErr_SetString(PyExc_ImportError, "panda3d.ode was compiled for Python " PY_VERSION ", which is incompatible with Python 2");
}
#endif
#else  // Python 2 case

void initode() {
  PyImport_Import(PyUnicode_FromString("panda3d.core"));
  Dtool_libpandaode_RegisterTypes();
  Dtool_libpandaode_ResolveExternals();

  LibraryDef *defs[] = {&libpandaode_moddef, NULL};

  PyObject *module = Dtool_PyModuleInitHelper(defs, "panda3d.ode");
  if (module != NULL) {
    Dtool_libpandaode_BuildInstants(module);
  }
}

#ifndef NDEBUG
PyObject *PyInit_ode() {
  PyErr_SetString(PyExc_ImportError, "panda3d.ode was compiled for Python " PY_VERSION ", which is incompatible with Python 3");
  return (PyObject *)NULL;
}
#endif
#endif

