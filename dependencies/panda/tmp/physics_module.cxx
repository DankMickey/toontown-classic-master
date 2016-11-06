
#include "dtoolbase.h"
#include "interrogate_request.h"

#include "py_panda.h"

extern LibraryDef libp3physics_moddef;
extern void Dtool_libp3physics_RegisterTypes();
extern void Dtool_libp3physics_ResolveExternals();
extern void Dtool_libp3physics_BuildInstants(PyObject *module);
extern LibraryDef libp3particlesystem_moddef;
extern void Dtool_libp3particlesystem_RegisterTypes();
extern void Dtool_libp3particlesystem_ResolveExternals();
extern void Dtool_libp3particlesystem_BuildInstants(PyObject *module);

#if PY_MAJOR_VERSION >= 3 || !defined(NDEBUG)
#ifdef _WIN32
extern "C" __declspec(dllexport) PyObject *PyInit_physics();
#elif __GNUC__ >= 4
extern "C" __attribute__((visibility("default"))) PyObject *PyInit_physics();
#else
extern "C" PyObject *PyInit_physics();
#endif
#endif
#if PY_MAJOR_VERSION < 3 || !defined(NDEBUG)
#ifdef _WIN32
extern "C" __declspec(dllexport) void initphysics();
#elif __GNUC__ >= 4
extern "C" __attribute__((visibility("default"))) void initphysics();
#else
extern "C" void initphysics();
#endif
#endif

#if PY_MAJOR_VERSION >= 3
static struct PyModuleDef py_physics_module = {
  PyModuleDef_HEAD_INIT,
  "physics",
  NULL,
  -1,
  NULL,
  NULL, NULL, NULL, NULL
};

PyObject *PyInit_physics() {
  PyImport_Import(PyUnicode_FromString("panda3d.core"));
  Dtool_libp3physics_RegisterTypes();
  Dtool_libp3particlesystem_RegisterTypes();
  Dtool_libp3physics_ResolveExternals();
  Dtool_libp3particlesystem_ResolveExternals();

  LibraryDef *defs[] = {&libp3physics_moddef, &libp3particlesystem_moddef, NULL};

  PyObject *module = Dtool_PyModuleInitHelper(defs, &py_physics_module);
  if (module != NULL) {
    Dtool_libp3physics_BuildInstants(module);
    Dtool_libp3particlesystem_BuildInstants(module);
  }
  return module;
}

#ifndef NDEBUG
void initphysics() {
  PyErr_SetString(PyExc_ImportError, "panda3d.physics was compiled for Python " PY_VERSION ", which is incompatible with Python 2");
}
#endif
#else  // Python 2 case

void initphysics() {
  PyImport_Import(PyUnicode_FromString("panda3d.core"));
  Dtool_libp3physics_RegisterTypes();
  Dtool_libp3particlesystem_RegisterTypes();
  Dtool_libp3physics_ResolveExternals();
  Dtool_libp3particlesystem_ResolveExternals();

  LibraryDef *defs[] = {&libp3physics_moddef, &libp3particlesystem_moddef, NULL};

  PyObject *module = Dtool_PyModuleInitHelper(defs, "panda3d.physics");
  if (module != NULL) {
    Dtool_libp3physics_BuildInstants(module);
    Dtool_libp3particlesystem_BuildInstants(module);
  }
}

#ifndef NDEBUG
PyObject *PyInit_physics() {
  PyErr_SetString(PyExc_ImportError, "panda3d.physics was compiled for Python " PY_VERSION ", which is incompatible with Python 3");
  return (PyObject *)NULL;
}
#endif
#endif

