
#include "dtoolbase.h"
#include "interrogate_request.h"

#include "py_panda.h"

extern LibraryDef libp3egg2pg_moddef;
extern void Dtool_libp3egg2pg_RegisterTypes();
extern void Dtool_libp3egg2pg_ResolveExternals();
extern void Dtool_libp3egg2pg_BuildInstants(PyObject *module);
extern LibraryDef libp3egg_moddef;
extern void Dtool_libp3egg_RegisterTypes();
extern void Dtool_libp3egg_ResolveExternals();
extern void Dtool_libp3egg_BuildInstants(PyObject *module);

#if PY_MAJOR_VERSION >= 3 || !defined(NDEBUG)
#ifdef _WIN32
extern "C" __declspec(dllexport) PyObject *PyInit_egg();
#elif __GNUC__ >= 4
extern "C" __attribute__((visibility("default"))) PyObject *PyInit_egg();
#else
extern "C" PyObject *PyInit_egg();
#endif
#endif
#if PY_MAJOR_VERSION < 3 || !defined(NDEBUG)
#ifdef _WIN32
extern "C" __declspec(dllexport) void initegg();
#elif __GNUC__ >= 4
extern "C" __attribute__((visibility("default"))) void initegg();
#else
extern "C" void initegg();
#endif
#endif

#if PY_MAJOR_VERSION >= 3
static struct PyModuleDef py_egg_module = {
  PyModuleDef_HEAD_INIT,
  "egg",
  NULL,
  -1,
  NULL,
  NULL, NULL, NULL, NULL
};

PyObject *PyInit_egg() {
  PyImport_Import(PyUnicode_FromString("panda3d.core"));
  Dtool_libp3egg2pg_RegisterTypes();
  Dtool_libp3egg_RegisterTypes();
  Dtool_libp3egg2pg_ResolveExternals();
  Dtool_libp3egg_ResolveExternals();

  LibraryDef *defs[] = {&libp3egg2pg_moddef, &libp3egg_moddef, NULL};

  PyObject *module = Dtool_PyModuleInitHelper(defs, &py_egg_module);
  if (module != NULL) {
    Dtool_libp3egg2pg_BuildInstants(module);
    Dtool_libp3egg_BuildInstants(module);
  }
  return module;
}

#ifndef NDEBUG
void initegg() {
  PyErr_SetString(PyExc_ImportError, "panda3d.egg was compiled for Python " PY_VERSION ", which is incompatible with Python 2");
}
#endif
#else  // Python 2 case

void initegg() {
  PyImport_Import(PyUnicode_FromString("panda3d.core"));
  Dtool_libp3egg2pg_RegisterTypes();
  Dtool_libp3egg_RegisterTypes();
  Dtool_libp3egg2pg_ResolveExternals();
  Dtool_libp3egg_ResolveExternals();

  LibraryDef *defs[] = {&libp3egg2pg_moddef, &libp3egg_moddef, NULL};

  PyObject *module = Dtool_PyModuleInitHelper(defs, "panda3d.egg");
  if (module != NULL) {
    Dtool_libp3egg2pg_BuildInstants(module);
    Dtool_libp3egg_BuildInstants(module);
  }
}

#ifndef NDEBUG
PyObject *PyInit_egg() {
  PyErr_SetString(PyExc_ImportError, "panda3d.egg was compiled for Python " PY_VERSION ", which is incompatible with Python 3");
  return (PyObject *)NULL;
}
#endif
#endif

