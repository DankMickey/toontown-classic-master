
#include "dtoolbase.h"
#include "interrogate_request.h"

#include "py_panda.h"

extern LibraryDef libp3vision_moddef;
extern void Dtool_libp3vision_RegisterTypes();
extern void Dtool_libp3vision_ResolveExternals();
extern void Dtool_libp3vision_BuildInstants(PyObject *module);

#if PY_MAJOR_VERSION >= 3 || !defined(NDEBUG)
#ifdef _WIN32
extern "C" __declspec(dllexport) PyObject *PyInit_vision();
#elif __GNUC__ >= 4
extern "C" __attribute__((visibility("default"))) PyObject *PyInit_vision();
#else
extern "C" PyObject *PyInit_vision();
#endif
#endif
#if PY_MAJOR_VERSION < 3 || !defined(NDEBUG)
#ifdef _WIN32
extern "C" __declspec(dllexport) void initvision();
#elif __GNUC__ >= 4
extern "C" __attribute__((visibility("default"))) void initvision();
#else
extern "C" void initvision();
#endif
#endif

#if PY_MAJOR_VERSION >= 3
static struct PyModuleDef py_vision_module = {
  PyModuleDef_HEAD_INIT,
  "vision",
  NULL,
  -1,
  NULL,
  NULL, NULL, NULL, NULL
};

PyObject *PyInit_vision() {
  PyImport_Import(PyUnicode_FromString("panda3d.core"));
  Dtool_libp3vision_RegisterTypes();
  Dtool_libp3vision_ResolveExternals();

  LibraryDef *defs[] = {&libp3vision_moddef, NULL};

  PyObject *module = Dtool_PyModuleInitHelper(defs, &py_vision_module);
  if (module != NULL) {
    Dtool_libp3vision_BuildInstants(module);
  }
  return module;
}

#ifndef NDEBUG
void initvision() {
  PyErr_SetString(PyExc_ImportError, "panda3d.vision was compiled for Python " PY_VERSION ", which is incompatible with Python 2");
}
#endif
#else  // Python 2 case

void initvision() {
  PyImport_Import(PyUnicode_FromString("panda3d.core"));
  Dtool_libp3vision_RegisterTypes();
  Dtool_libp3vision_ResolveExternals();

  LibraryDef *defs[] = {&libp3vision_moddef, NULL};

  PyObject *module = Dtool_PyModuleInitHelper(defs, "panda3d.vision");
  if (module != NULL) {
    Dtool_libp3vision_BuildInstants(module);
  }
}

#ifndef NDEBUG
PyObject *PyInit_vision() {
  PyErr_SetString(PyExc_ImportError, "panda3d.vision was compiled for Python " PY_VERSION ", which is incompatible with Python 3");
  return (PyObject *)NULL;
}
#endif
#endif

