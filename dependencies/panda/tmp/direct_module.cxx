
#include "dtoolbase.h"
#include "interrogate_request.h"

#include "py_panda.h"

extern LibraryDef libp3dcparser_moddef;
extern void Dtool_libp3dcparser_RegisterTypes();
extern void Dtool_libp3dcparser_ResolveExternals();
extern void Dtool_libp3dcparser_BuildInstants(PyObject *module);
extern LibraryDef libp3showbase_moddef;
extern void Dtool_libp3showbase_RegisterTypes();
extern void Dtool_libp3showbase_ResolveExternals();
extern void Dtool_libp3showbase_BuildInstants(PyObject *module);
extern LibraryDef libp3deadrec_moddef;
extern void Dtool_libp3deadrec_RegisterTypes();
extern void Dtool_libp3deadrec_ResolveExternals();
extern void Dtool_libp3deadrec_BuildInstants(PyObject *module);
extern LibraryDef libp3interval_moddef;
extern void Dtool_libp3interval_RegisterTypes();
extern void Dtool_libp3interval_ResolveExternals();
extern void Dtool_libp3interval_BuildInstants(PyObject *module);
extern LibraryDef libp3distributed_moddef;
extern void Dtool_libp3distributed_RegisterTypes();
extern void Dtool_libp3distributed_ResolveExternals();
extern void Dtool_libp3distributed_BuildInstants(PyObject *module);
extern LibraryDef libp3motiontrail_moddef;
extern void Dtool_libp3motiontrail_RegisterTypes();
extern void Dtool_libp3motiontrail_ResolveExternals();
extern void Dtool_libp3motiontrail_BuildInstants(PyObject *module);

#if PY_MAJOR_VERSION >= 3 || !defined(NDEBUG)
#ifdef _WIN32
extern "C" __declspec(dllexport) PyObject *PyInit_direct();
#elif __GNUC__ >= 4
extern "C" __attribute__((visibility("default"))) PyObject *PyInit_direct();
#else
extern "C" PyObject *PyInit_direct();
#endif
#endif
#if PY_MAJOR_VERSION < 3 || !defined(NDEBUG)
#ifdef _WIN32
extern "C" __declspec(dllexport) void initdirect();
#elif __GNUC__ >= 4
extern "C" __attribute__((visibility("default"))) void initdirect();
#else
extern "C" void initdirect();
#endif
#endif

#if PY_MAJOR_VERSION >= 3
static struct PyModuleDef py_direct_module = {
  PyModuleDef_HEAD_INIT,
  "direct",
  NULL,
  -1,
  NULL,
  NULL, NULL, NULL, NULL
};

PyObject *PyInit_direct() {
  PyImport_Import(PyUnicode_FromString("panda3d.core"));
  Dtool_libp3dcparser_RegisterTypes();
  Dtool_libp3showbase_RegisterTypes();
  Dtool_libp3deadrec_RegisterTypes();
  Dtool_libp3interval_RegisterTypes();
  Dtool_libp3distributed_RegisterTypes();
  Dtool_libp3motiontrail_RegisterTypes();
  Dtool_libp3dcparser_ResolveExternals();
  Dtool_libp3showbase_ResolveExternals();
  Dtool_libp3deadrec_ResolveExternals();
  Dtool_libp3interval_ResolveExternals();
  Dtool_libp3distributed_ResolveExternals();
  Dtool_libp3motiontrail_ResolveExternals();

  LibraryDef *defs[] = {&libp3dcparser_moddef, &libp3showbase_moddef, &libp3deadrec_moddef, &libp3interval_moddef, &libp3distributed_moddef, &libp3motiontrail_moddef, NULL};

  PyObject *module = Dtool_PyModuleInitHelper(defs, &py_direct_module);
  if (module != NULL) {
    Dtool_libp3dcparser_BuildInstants(module);
    Dtool_libp3showbase_BuildInstants(module);
    Dtool_libp3deadrec_BuildInstants(module);
    Dtool_libp3interval_BuildInstants(module);
    Dtool_libp3distributed_BuildInstants(module);
    Dtool_libp3motiontrail_BuildInstants(module);
  }
  return module;
}

#ifndef NDEBUG
void initdirect() {
  PyErr_SetString(PyExc_ImportError, "panda3d.direct was compiled for Python " PY_VERSION ", which is incompatible with Python 2");
}
#endif
#else  // Python 2 case

void initdirect() {
  PyImport_Import(PyUnicode_FromString("panda3d.core"));
  Dtool_libp3dcparser_RegisterTypes();
  Dtool_libp3showbase_RegisterTypes();
  Dtool_libp3deadrec_RegisterTypes();
  Dtool_libp3interval_RegisterTypes();
  Dtool_libp3distributed_RegisterTypes();
  Dtool_libp3motiontrail_RegisterTypes();
  Dtool_libp3dcparser_ResolveExternals();
  Dtool_libp3showbase_ResolveExternals();
  Dtool_libp3deadrec_ResolveExternals();
  Dtool_libp3interval_ResolveExternals();
  Dtool_libp3distributed_ResolveExternals();
  Dtool_libp3motiontrail_ResolveExternals();

  LibraryDef *defs[] = {&libp3dcparser_moddef, &libp3showbase_moddef, &libp3deadrec_moddef, &libp3interval_moddef, &libp3distributed_moddef, &libp3motiontrail_moddef, NULL};

  PyObject *module = Dtool_PyModuleInitHelper(defs, "panda3d.direct");
  if (module != NULL) {
    Dtool_libp3dcparser_BuildInstants(module);
    Dtool_libp3showbase_BuildInstants(module);
    Dtool_libp3deadrec_BuildInstants(module);
    Dtool_libp3interval_BuildInstants(module);
    Dtool_libp3distributed_BuildInstants(module);
    Dtool_libp3motiontrail_BuildInstants(module);
  }
}

#ifndef NDEBUG
PyObject *PyInit_direct() {
  PyErr_SetString(PyExc_ImportError, "panda3d.direct was compiled for Python " PY_VERSION ", which is incompatible with Python 3");
  return (PyObject *)NULL;
}
#endif
#endif

