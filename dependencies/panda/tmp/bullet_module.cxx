
#include "dtoolbase.h"
#include "interrogate_request.h"

#include "py_panda.h"

extern LibraryDef libpandabullet_moddef;
extern void Dtool_libpandabullet_RegisterTypes();
extern void Dtool_libpandabullet_ResolveExternals();
extern void Dtool_libpandabullet_BuildInstants(PyObject *module);

#if PY_MAJOR_VERSION >= 3 || !defined(NDEBUG)
#ifdef _WIN32
extern "C" __declspec(dllexport) PyObject *PyInit_bullet();
#elif __GNUC__ >= 4
extern "C" __attribute__((visibility("default"))) PyObject *PyInit_bullet();
#else
extern "C" PyObject *PyInit_bullet();
#endif
#endif
#if PY_MAJOR_VERSION < 3 || !defined(NDEBUG)
#ifdef _WIN32
extern "C" __declspec(dllexport) void initbullet();
#elif __GNUC__ >= 4
extern "C" __attribute__((visibility("default"))) void initbullet();
#else
extern "C" void initbullet();
#endif
#endif

#if PY_MAJOR_VERSION >= 3
static struct PyModuleDef py_bullet_module = {
  PyModuleDef_HEAD_INIT,
  "bullet",
  NULL,
  -1,
  NULL,
  NULL, NULL, NULL, NULL
};

PyObject *PyInit_bullet() {
  PyImport_Import(PyUnicode_FromString("panda3d.core"));
  Dtool_libpandabullet_RegisterTypes();
  Dtool_libpandabullet_ResolveExternals();

  LibraryDef *defs[] = {&libpandabullet_moddef, NULL};

  PyObject *module = Dtool_PyModuleInitHelper(defs, &py_bullet_module);
  if (module != NULL) {
    Dtool_libpandabullet_BuildInstants(module);
  }
  return module;
}

#ifndef NDEBUG
void initbullet() {
  PyErr_SetString(PyExc_ImportError, "panda3d.bullet was compiled for Python " PY_VERSION ", which is incompatible with Python 2");
}
#endif
#else  // Python 2 case

void initbullet() {
  PyImport_Import(PyUnicode_FromString("panda3d.core"));
  Dtool_libpandabullet_RegisterTypes();
  Dtool_libpandabullet_ResolveExternals();

  LibraryDef *defs[] = {&libpandabullet_moddef, NULL};

  PyObject *module = Dtool_PyModuleInitHelper(defs, "panda3d.bullet");
  if (module != NULL) {
    Dtool_libpandabullet_BuildInstants(module);
  }
}

#ifndef NDEBUG
PyObject *PyInit_bullet() {
  PyErr_SetString(PyExc_ImportError, "panda3d.bullet was compiled for Python " PY_VERSION ", which is incompatible with Python 3");
  return (PyObject *)NULL;
}
#endif
#endif

