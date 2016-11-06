
#include "dtoolbase.h"
#include "interrogate_request.h"

#include "py_panda.h"

extern LibraryDef libp3vrpn_moddef;
extern void Dtool_libp3vrpn_RegisterTypes();
extern void Dtool_libp3vrpn_ResolveExternals();
extern void Dtool_libp3vrpn_BuildInstants(PyObject *module);

#if PY_MAJOR_VERSION >= 3 || !defined(NDEBUG)
#ifdef _WIN32
extern "C" __declspec(dllexport) PyObject *PyInit_vrpn();
#elif __GNUC__ >= 4
extern "C" __attribute__((visibility("default"))) PyObject *PyInit_vrpn();
#else
extern "C" PyObject *PyInit_vrpn();
#endif
#endif
#if PY_MAJOR_VERSION < 3 || !defined(NDEBUG)
#ifdef _WIN32
extern "C" __declspec(dllexport) void initvrpn();
#elif __GNUC__ >= 4
extern "C" __attribute__((visibility("default"))) void initvrpn();
#else
extern "C" void initvrpn();
#endif
#endif

#if PY_MAJOR_VERSION >= 3
static struct PyModuleDef py_vrpn_module = {
  PyModuleDef_HEAD_INIT,
  "vrpn",
  NULL,
  -1,
  NULL,
  NULL, NULL, NULL, NULL
};

PyObject *PyInit_vrpn() {
  PyImport_Import(PyUnicode_FromString("panda3d.core"));
  Dtool_libp3vrpn_RegisterTypes();
  Dtool_libp3vrpn_ResolveExternals();

  LibraryDef *defs[] = {&libp3vrpn_moddef, NULL};

  PyObject *module = Dtool_PyModuleInitHelper(defs, &py_vrpn_module);
  if (module != NULL) {
    Dtool_libp3vrpn_BuildInstants(module);
  }
  return module;
}

#ifndef NDEBUG
void initvrpn() {
  PyErr_SetString(PyExc_ImportError, "panda3d.vrpn was compiled for Python " PY_VERSION ", which is incompatible with Python 2");
}
#endif
#else  // Python 2 case

void initvrpn() {
  PyImport_Import(PyUnicode_FromString("panda3d.core"));
  Dtool_libp3vrpn_RegisterTypes();
  Dtool_libp3vrpn_ResolveExternals();

  LibraryDef *defs[] = {&libp3vrpn_moddef, NULL};

  PyObject *module = Dtool_PyModuleInitHelper(defs, "panda3d.vrpn");
  if (module != NULL) {
    Dtool_libp3vrpn_BuildInstants(module);
  }
}

#ifndef NDEBUG
PyObject *PyInit_vrpn() {
  PyErr_SetString(PyExc_ImportError, "panda3d.vrpn was compiled for Python " PY_VERSION ", which is incompatible with Python 3");
  return (PyObject *)NULL;
}
#endif
#endif

