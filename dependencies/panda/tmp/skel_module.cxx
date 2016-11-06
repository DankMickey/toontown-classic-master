
#include "dtoolbase.h"
#include "interrogate_request.h"

#include "py_panda.h"

extern LibraryDef libp3skel_moddef;
extern void Dtool_libp3skel_RegisterTypes();
extern void Dtool_libp3skel_ResolveExternals();
extern void Dtool_libp3skel_BuildInstants(PyObject *module);

#if PY_MAJOR_VERSION >= 3 || !defined(NDEBUG)
#ifdef _WIN32
extern "C" __declspec(dllexport) PyObject *PyInit_skel();
#elif __GNUC__ >= 4
extern "C" __attribute__((visibility("default"))) PyObject *PyInit_skel();
#else
extern "C" PyObject *PyInit_skel();
#endif
#endif
#if PY_MAJOR_VERSION < 3 || !defined(NDEBUG)
#ifdef _WIN32
extern "C" __declspec(dllexport) void initskel();
#elif __GNUC__ >= 4
extern "C" __attribute__((visibility("default"))) void initskel();
#else
extern "C" void initskel();
#endif
#endif

#if PY_MAJOR_VERSION >= 3
static struct PyModuleDef py_skel_module = {
  PyModuleDef_HEAD_INIT,
  "skel",
  NULL,
  -1,
  NULL,
  NULL, NULL, NULL, NULL
};

PyObject *PyInit_skel() {
  PyImport_Import(PyUnicode_FromString("panda3d.core"));
  Dtool_libp3skel_RegisterTypes();
  Dtool_libp3skel_ResolveExternals();

  LibraryDef *defs[] = {&libp3skel_moddef, NULL};

  PyObject *module = Dtool_PyModuleInitHelper(defs, &py_skel_module);
  if (module != NULL) {
    Dtool_libp3skel_BuildInstants(module);
  }
  return module;
}

#ifndef NDEBUG
void initskel() {
  PyErr_SetString(PyExc_ImportError, "panda3d.skel was compiled for Python " PY_VERSION ", which is incompatible with Python 2");
}
#endif
#else  // Python 2 case

void initskel() {
  PyImport_Import(PyUnicode_FromString("panda3d.core"));
  Dtool_libp3skel_RegisterTypes();
  Dtool_libp3skel_ResolveExternals();

  LibraryDef *defs[] = {&libp3skel_moddef, NULL};

  PyObject *module = Dtool_PyModuleInitHelper(defs, "panda3d.skel");
  if (module != NULL) {
    Dtool_libp3skel_BuildInstants(module);
  }
}

#ifndef NDEBUG
PyObject *PyInit_skel() {
  PyErr_SetString(PyExc_ImportError, "panda3d.skel was compiled for Python " PY_VERSION ", which is incompatible with Python 3");
  return (PyObject *)NULL;
}
#endif
#endif

