
#include "dtoolbase.h"
#include "interrogate_request.h"

#include "py_panda.h"

extern LibraryDef libpandaai_moddef;
extern void Dtool_libpandaai_RegisterTypes();
extern void Dtool_libpandaai_ResolveExternals();
extern void Dtool_libpandaai_BuildInstants(PyObject *module);

#if PY_MAJOR_VERSION >= 3 || !defined(NDEBUG)
#ifdef _WIN32
extern "C" __declspec(dllexport) PyObject *PyInit_ai();
#elif __GNUC__ >= 4
extern "C" __attribute__((visibility("default"))) PyObject *PyInit_ai();
#else
extern "C" PyObject *PyInit_ai();
#endif
#endif
#if PY_MAJOR_VERSION < 3 || !defined(NDEBUG)
#ifdef _WIN32
extern "C" __declspec(dllexport) void initai();
#elif __GNUC__ >= 4
extern "C" __attribute__((visibility("default"))) void initai();
#else
extern "C" void initai();
#endif
#endif

#if PY_MAJOR_VERSION >= 3
static struct PyModuleDef py_ai_module = {
  PyModuleDef_HEAD_INIT,
  "ai",
  NULL,
  -1,
  NULL,
  NULL, NULL, NULL, NULL
};

PyObject *PyInit_ai() {
  PyImport_Import(PyUnicode_FromString("panda3d.core"));
  Dtool_libpandaai_RegisterTypes();
  Dtool_libpandaai_ResolveExternals();

  LibraryDef *defs[] = {&libpandaai_moddef, NULL};

  PyObject *module = Dtool_PyModuleInitHelper(defs, &py_ai_module);
  if (module != NULL) {
    Dtool_libpandaai_BuildInstants(module);
  }
  return module;
}

#ifndef NDEBUG
void initai() {
  PyErr_SetString(PyExc_ImportError, "panda3d.ai was compiled for Python " PY_VERSION ", which is incompatible with Python 2");
}
#endif
#else  // Python 2 case

void initai() {
  PyImport_Import(PyUnicode_FromString("panda3d.core"));
  Dtool_libpandaai_RegisterTypes();
  Dtool_libpandaai_ResolveExternals();

  LibraryDef *defs[] = {&libpandaai_moddef, NULL};

  PyObject *module = Dtool_PyModuleInitHelper(defs, "panda3d.ai");
  if (module != NULL) {
    Dtool_libpandaai_BuildInstants(module);
  }
}

#ifndef NDEBUG
PyObject *PyInit_ai() {
  PyErr_SetString(PyExc_ImportError, "panda3d.ai was compiled for Python " PY_VERSION ", which is incompatible with Python 3");
  return (PyObject *)NULL;
}
#endif
#endif

