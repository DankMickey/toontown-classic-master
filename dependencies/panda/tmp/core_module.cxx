
#include "dtoolbase.h"
#include "interrogate_request.h"

#include "py_panda.h"

extern LibraryDef libp3downloader_moddef;
extern void Dtool_libp3downloader_RegisterTypes();
extern void Dtool_libp3downloader_ResolveExternals();
extern void Dtool_libp3downloader_BuildInstants(PyObject *module);
extern LibraryDef libp3express_moddef;
extern void Dtool_libp3express_RegisterTypes();
extern void Dtool_libp3express_ResolveExternals();
extern void Dtool_libp3express_BuildInstants(PyObject *module);
extern LibraryDef libp3recorder_moddef;
extern void Dtool_libp3recorder_RegisterTypes();
extern void Dtool_libp3recorder_ResolveExternals();
extern void Dtool_libp3recorder_BuildInstants(PyObject *module);
extern LibraryDef libp3pgraphnodes_moddef;
extern void Dtool_libp3pgraphnodes_RegisterTypes();
extern void Dtool_libp3pgraphnodes_ResolveExternals();
extern void Dtool_libp3pgraphnodes_BuildInstants(PyObject *module);
extern LibraryDef libp3pgraph_moddef;
extern void Dtool_libp3pgraph_RegisterTypes();
extern void Dtool_libp3pgraph_ResolveExternals();
extern void Dtool_libp3pgraph_BuildInstants(PyObject *module);
extern LibraryDef libp3grutil_moddef;
extern void Dtool_libp3grutil_RegisterTypes();
extern void Dtool_libp3grutil_ResolveExternals();
extern void Dtool_libp3grutil_BuildInstants(PyObject *module);
extern LibraryDef libp3chan_moddef;
extern void Dtool_libp3chan_RegisterTypes();
extern void Dtool_libp3chan_ResolveExternals();
extern void Dtool_libp3chan_BuildInstants(PyObject *module);
extern LibraryDef libp3pstatclient_moddef;
extern void Dtool_libp3pstatclient_RegisterTypes();
extern void Dtool_libp3pstatclient_ResolveExternals();
extern void Dtool_libp3pstatclient_BuildInstants(PyObject *module);
extern LibraryDef libp3char_moddef;
extern void Dtool_libp3char_RegisterTypes();
extern void Dtool_libp3char_ResolveExternals();
extern void Dtool_libp3char_BuildInstants(PyObject *module);
extern LibraryDef libp3collide_moddef;
extern void Dtool_libp3collide_RegisterTypes();
extern void Dtool_libp3collide_ResolveExternals();
extern void Dtool_libp3collide_BuildInstants(PyObject *module);
extern LibraryDef libp3device_moddef;
extern void Dtool_libp3device_RegisterTypes();
extern void Dtool_libp3device_ResolveExternals();
extern void Dtool_libp3device_BuildInstants(PyObject *module);
extern LibraryDef libp3dgraph_moddef;
extern void Dtool_libp3dgraph_RegisterTypes();
extern void Dtool_libp3dgraph_ResolveExternals();
extern void Dtool_libp3dgraph_BuildInstants(PyObject *module);
extern LibraryDef libp3display_moddef;
extern void Dtool_libp3display_RegisterTypes();
extern void Dtool_libp3display_ResolveExternals();
extern void Dtool_libp3display_BuildInstants(PyObject *module);
extern LibraryDef libp3pipeline_moddef;
extern void Dtool_libp3pipeline_RegisterTypes();
extern void Dtool_libp3pipeline_ResolveExternals();
extern void Dtool_libp3pipeline_BuildInstants(PyObject *module);
extern LibraryDef libp3event_moddef;
extern void Dtool_libp3event_RegisterTypes();
extern void Dtool_libp3event_ResolveExternals();
extern void Dtool_libp3event_BuildInstants(PyObject *module);
extern LibraryDef libp3gobj_moddef;
extern void Dtool_libp3gobj_RegisterTypes();
extern void Dtool_libp3gobj_ResolveExternals();
extern void Dtool_libp3gobj_BuildInstants(PyObject *module);
extern LibraryDef libp3gsgbase_moddef;
extern void Dtool_libp3gsgbase_RegisterTypes();
extern void Dtool_libp3gsgbase_ResolveExternals();
extern void Dtool_libp3gsgbase_BuildInstants(PyObject *module);
extern LibraryDef libp3linmath_moddef;
extern void Dtool_libp3linmath_RegisterTypes();
extern void Dtool_libp3linmath_ResolveExternals();
extern void Dtool_libp3linmath_BuildInstants(PyObject *module);
extern LibraryDef libp3mathutil_moddef;
extern void Dtool_libp3mathutil_RegisterTypes();
extern void Dtool_libp3mathutil_ResolveExternals();
extern void Dtool_libp3mathutil_BuildInstants(PyObject *module);
extern LibraryDef libp3parametrics_moddef;
extern void Dtool_libp3parametrics_RegisterTypes();
extern void Dtool_libp3parametrics_ResolveExternals();
extern void Dtool_libp3parametrics_BuildInstants(PyObject *module);
extern LibraryDef libp3pnmimage_moddef;
extern void Dtool_libp3pnmimage_RegisterTypes();
extern void Dtool_libp3pnmimage_ResolveExternals();
extern void Dtool_libp3pnmimage_BuildInstants(PyObject *module);
extern LibraryDef libp3text_moddef;
extern void Dtool_libp3text_RegisterTypes();
extern void Dtool_libp3text_ResolveExternals();
extern void Dtool_libp3text_BuildInstants(PyObject *module);
extern LibraryDef libp3tform_moddef;
extern void Dtool_libp3tform_RegisterTypes();
extern void Dtool_libp3tform_ResolveExternals();
extern void Dtool_libp3tform_BuildInstants(PyObject *module);
extern LibraryDef libp3putil_moddef;
extern void Dtool_libp3putil_RegisterTypes();
extern void Dtool_libp3putil_ResolveExternals();
extern void Dtool_libp3putil_BuildInstants(PyObject *module);
extern LibraryDef libp3audio_moddef;
extern void Dtool_libp3audio_RegisterTypes();
extern void Dtool_libp3audio_ResolveExternals();
extern void Dtool_libp3audio_BuildInstants(PyObject *module);
extern LibraryDef libp3nativenet_moddef;
extern void Dtool_libp3nativenet_RegisterTypes();
extern void Dtool_libp3nativenet_ResolveExternals();
extern void Dtool_libp3nativenet_BuildInstants(PyObject *module);
extern LibraryDef libp3net_moddef;
extern void Dtool_libp3net_RegisterTypes();
extern void Dtool_libp3net_ResolveExternals();
extern void Dtool_libp3net_BuildInstants(PyObject *module);
extern LibraryDef libp3pgui_moddef;
extern void Dtool_libp3pgui_RegisterTypes();
extern void Dtool_libp3pgui_ResolveExternals();
extern void Dtool_libp3pgui_BuildInstants(PyObject *module);
extern LibraryDef libp3movies_moddef;
extern void Dtool_libp3movies_RegisterTypes();
extern void Dtool_libp3movies_ResolveExternals();
extern void Dtool_libp3movies_BuildInstants(PyObject *module);
extern LibraryDef libp3dxml_moddef;
extern void Dtool_libp3dxml_RegisterTypes();
extern void Dtool_libp3dxml_ResolveExternals();
extern void Dtool_libp3dxml_BuildInstants(PyObject *module);
extern LibraryDef libp3pnmtext_moddef;
extern void Dtool_libp3pnmtext_RegisterTypes();
extern void Dtool_libp3pnmtext_ResolveExternals();
extern void Dtool_libp3pnmtext_BuildInstants(PyObject *module);

#if PY_MAJOR_VERSION >= 3 || !defined(NDEBUG)
#ifdef _WIN32
extern "C" __declspec(dllexport) PyObject *PyInit_core();
#elif __GNUC__ >= 4
extern "C" __attribute__((visibility("default"))) PyObject *PyInit_core();
#else
extern "C" PyObject *PyInit_core();
#endif
#endif
#if PY_MAJOR_VERSION < 3 || !defined(NDEBUG)
#ifdef _WIN32
extern "C" __declspec(dllexport) void initcore();
#elif __GNUC__ >= 4
extern "C" __attribute__((visibility("default"))) void initcore();
#else
extern "C" void initcore();
#endif
#endif

#if PY_MAJOR_VERSION >= 3
static struct PyModuleDef py_core_module = {
  PyModuleDef_HEAD_INIT,
  "core",
  NULL,
  -1,
  NULL,
  NULL, NULL, NULL, NULL
};

PyObject *PyInit_core() {
  Dtool_libp3downloader_RegisterTypes();
  Dtool_libp3express_RegisterTypes();
  Dtool_libp3recorder_RegisterTypes();
  Dtool_libp3pgraphnodes_RegisterTypes();
  Dtool_libp3pgraph_RegisterTypes();
  Dtool_libp3grutil_RegisterTypes();
  Dtool_libp3chan_RegisterTypes();
  Dtool_libp3pstatclient_RegisterTypes();
  Dtool_libp3char_RegisterTypes();
  Dtool_libp3collide_RegisterTypes();
  Dtool_libp3device_RegisterTypes();
  Dtool_libp3dgraph_RegisterTypes();
  Dtool_libp3display_RegisterTypes();
  Dtool_libp3pipeline_RegisterTypes();
  Dtool_libp3event_RegisterTypes();
  Dtool_libp3gobj_RegisterTypes();
  Dtool_libp3gsgbase_RegisterTypes();
  Dtool_libp3linmath_RegisterTypes();
  Dtool_libp3mathutil_RegisterTypes();
  Dtool_libp3parametrics_RegisterTypes();
  Dtool_libp3pnmimage_RegisterTypes();
  Dtool_libp3text_RegisterTypes();
  Dtool_libp3tform_RegisterTypes();
  Dtool_libp3putil_RegisterTypes();
  Dtool_libp3audio_RegisterTypes();
  Dtool_libp3nativenet_RegisterTypes();
  Dtool_libp3net_RegisterTypes();
  Dtool_libp3pgui_RegisterTypes();
  Dtool_libp3movies_RegisterTypes();
  Dtool_libp3dxml_RegisterTypes();
  Dtool_libp3pnmtext_RegisterTypes();
  Dtool_libp3downloader_ResolveExternals();
  Dtool_libp3express_ResolveExternals();
  Dtool_libp3recorder_ResolveExternals();
  Dtool_libp3pgraphnodes_ResolveExternals();
  Dtool_libp3pgraph_ResolveExternals();
  Dtool_libp3grutil_ResolveExternals();
  Dtool_libp3chan_ResolveExternals();
  Dtool_libp3pstatclient_ResolveExternals();
  Dtool_libp3char_ResolveExternals();
  Dtool_libp3collide_ResolveExternals();
  Dtool_libp3device_ResolveExternals();
  Dtool_libp3dgraph_ResolveExternals();
  Dtool_libp3display_ResolveExternals();
  Dtool_libp3pipeline_ResolveExternals();
  Dtool_libp3event_ResolveExternals();
  Dtool_libp3gobj_ResolveExternals();
  Dtool_libp3gsgbase_ResolveExternals();
  Dtool_libp3linmath_ResolveExternals();
  Dtool_libp3mathutil_ResolveExternals();
  Dtool_libp3parametrics_ResolveExternals();
  Dtool_libp3pnmimage_ResolveExternals();
  Dtool_libp3text_ResolveExternals();
  Dtool_libp3tform_ResolveExternals();
  Dtool_libp3putil_ResolveExternals();
  Dtool_libp3audio_ResolveExternals();
  Dtool_libp3nativenet_ResolveExternals();
  Dtool_libp3net_ResolveExternals();
  Dtool_libp3pgui_ResolveExternals();
  Dtool_libp3movies_ResolveExternals();
  Dtool_libp3dxml_ResolveExternals();
  Dtool_libp3pnmtext_ResolveExternals();

  LibraryDef *defs[] = {&libp3downloader_moddef, &libp3express_moddef, &libp3recorder_moddef, &libp3pgraphnodes_moddef, &libp3pgraph_moddef, &libp3grutil_moddef, &libp3chan_moddef, &libp3pstatclient_moddef, &libp3char_moddef, &libp3collide_moddef, &libp3device_moddef, &libp3dgraph_moddef, &libp3display_moddef, &libp3pipeline_moddef, &libp3event_moddef, &libp3gobj_moddef, &libp3gsgbase_moddef, &libp3linmath_moddef, &libp3mathutil_moddef, &libp3parametrics_moddef, &libp3pnmimage_moddef, &libp3text_moddef, &libp3tform_moddef, &libp3putil_moddef, &libp3audio_moddef, &libp3nativenet_moddef, &libp3net_moddef, &libp3pgui_moddef, &libp3movies_moddef, &libp3dxml_moddef, &libp3pnmtext_moddef, NULL};

  PyObject *module = Dtool_PyModuleInitHelper(defs, &py_core_module);
  if (module != NULL) {
    Dtool_libp3downloader_BuildInstants(module);
    Dtool_libp3express_BuildInstants(module);
    Dtool_libp3recorder_BuildInstants(module);
    Dtool_libp3pgraphnodes_BuildInstants(module);
    Dtool_libp3pgraph_BuildInstants(module);
    Dtool_libp3grutil_BuildInstants(module);
    Dtool_libp3chan_BuildInstants(module);
    Dtool_libp3pstatclient_BuildInstants(module);
    Dtool_libp3char_BuildInstants(module);
    Dtool_libp3collide_BuildInstants(module);
    Dtool_libp3device_BuildInstants(module);
    Dtool_libp3dgraph_BuildInstants(module);
    Dtool_libp3display_BuildInstants(module);
    Dtool_libp3pipeline_BuildInstants(module);
    Dtool_libp3event_BuildInstants(module);
    Dtool_libp3gobj_BuildInstants(module);
    Dtool_libp3gsgbase_BuildInstants(module);
    Dtool_libp3linmath_BuildInstants(module);
    Dtool_libp3mathutil_BuildInstants(module);
    Dtool_libp3parametrics_BuildInstants(module);
    Dtool_libp3pnmimage_BuildInstants(module);
    Dtool_libp3text_BuildInstants(module);
    Dtool_libp3tform_BuildInstants(module);
    Dtool_libp3putil_BuildInstants(module);
    Dtool_libp3audio_BuildInstants(module);
    Dtool_libp3nativenet_BuildInstants(module);
    Dtool_libp3net_BuildInstants(module);
    Dtool_libp3pgui_BuildInstants(module);
    Dtool_libp3movies_BuildInstants(module);
    Dtool_libp3dxml_BuildInstants(module);
    Dtool_libp3pnmtext_BuildInstants(module);
  }
  return module;
}

#ifndef NDEBUG
void initcore() {
  PyErr_SetString(PyExc_ImportError, "panda3d.core was compiled for Python " PY_VERSION ", which is incompatible with Python 2");
}
#endif
#else  // Python 2 case

void initcore() {
  Dtool_libp3downloader_RegisterTypes();
  Dtool_libp3express_RegisterTypes();
  Dtool_libp3recorder_RegisterTypes();
  Dtool_libp3pgraphnodes_RegisterTypes();
  Dtool_libp3pgraph_RegisterTypes();
  Dtool_libp3grutil_RegisterTypes();
  Dtool_libp3chan_RegisterTypes();
  Dtool_libp3pstatclient_RegisterTypes();
  Dtool_libp3char_RegisterTypes();
  Dtool_libp3collide_RegisterTypes();
  Dtool_libp3device_RegisterTypes();
  Dtool_libp3dgraph_RegisterTypes();
  Dtool_libp3display_RegisterTypes();
  Dtool_libp3pipeline_RegisterTypes();
  Dtool_libp3event_RegisterTypes();
  Dtool_libp3gobj_RegisterTypes();
  Dtool_libp3gsgbase_RegisterTypes();
  Dtool_libp3linmath_RegisterTypes();
  Dtool_libp3mathutil_RegisterTypes();
  Dtool_libp3parametrics_RegisterTypes();
  Dtool_libp3pnmimage_RegisterTypes();
  Dtool_libp3text_RegisterTypes();
  Dtool_libp3tform_RegisterTypes();
  Dtool_libp3putil_RegisterTypes();
  Dtool_libp3audio_RegisterTypes();
  Dtool_libp3nativenet_RegisterTypes();
  Dtool_libp3net_RegisterTypes();
  Dtool_libp3pgui_RegisterTypes();
  Dtool_libp3movies_RegisterTypes();
  Dtool_libp3dxml_RegisterTypes();
  Dtool_libp3pnmtext_RegisterTypes();
  Dtool_libp3downloader_ResolveExternals();
  Dtool_libp3express_ResolveExternals();
  Dtool_libp3recorder_ResolveExternals();
  Dtool_libp3pgraphnodes_ResolveExternals();
  Dtool_libp3pgraph_ResolveExternals();
  Dtool_libp3grutil_ResolveExternals();
  Dtool_libp3chan_ResolveExternals();
  Dtool_libp3pstatclient_ResolveExternals();
  Dtool_libp3char_ResolveExternals();
  Dtool_libp3collide_ResolveExternals();
  Dtool_libp3device_ResolveExternals();
  Dtool_libp3dgraph_ResolveExternals();
  Dtool_libp3display_ResolveExternals();
  Dtool_libp3pipeline_ResolveExternals();
  Dtool_libp3event_ResolveExternals();
  Dtool_libp3gobj_ResolveExternals();
  Dtool_libp3gsgbase_ResolveExternals();
  Dtool_libp3linmath_ResolveExternals();
  Dtool_libp3mathutil_ResolveExternals();
  Dtool_libp3parametrics_ResolveExternals();
  Dtool_libp3pnmimage_ResolveExternals();
  Dtool_libp3text_ResolveExternals();
  Dtool_libp3tform_ResolveExternals();
  Dtool_libp3putil_ResolveExternals();
  Dtool_libp3audio_ResolveExternals();
  Dtool_libp3nativenet_ResolveExternals();
  Dtool_libp3net_ResolveExternals();
  Dtool_libp3pgui_ResolveExternals();
  Dtool_libp3movies_ResolveExternals();
  Dtool_libp3dxml_ResolveExternals();
  Dtool_libp3pnmtext_ResolveExternals();

  LibraryDef *defs[] = {&libp3downloader_moddef, &libp3express_moddef, &libp3recorder_moddef, &libp3pgraphnodes_moddef, &libp3pgraph_moddef, &libp3grutil_moddef, &libp3chan_moddef, &libp3pstatclient_moddef, &libp3char_moddef, &libp3collide_moddef, &libp3device_moddef, &libp3dgraph_moddef, &libp3display_moddef, &libp3pipeline_moddef, &libp3event_moddef, &libp3gobj_moddef, &libp3gsgbase_moddef, &libp3linmath_moddef, &libp3mathutil_moddef, &libp3parametrics_moddef, &libp3pnmimage_moddef, &libp3text_moddef, &libp3tform_moddef, &libp3putil_moddef, &libp3audio_moddef, &libp3nativenet_moddef, &libp3net_moddef, &libp3pgui_moddef, &libp3movies_moddef, &libp3dxml_moddef, &libp3pnmtext_moddef, NULL};

  PyObject *module = Dtool_PyModuleInitHelper(defs, "panda3d.core");
  if (module != NULL) {
    Dtool_libp3downloader_BuildInstants(module);
    Dtool_libp3express_BuildInstants(module);
    Dtool_libp3recorder_BuildInstants(module);
    Dtool_libp3pgraphnodes_BuildInstants(module);
    Dtool_libp3pgraph_BuildInstants(module);
    Dtool_libp3grutil_BuildInstants(module);
    Dtool_libp3chan_BuildInstants(module);
    Dtool_libp3pstatclient_BuildInstants(module);
    Dtool_libp3char_BuildInstants(module);
    Dtool_libp3collide_BuildInstants(module);
    Dtool_libp3device_BuildInstants(module);
    Dtool_libp3dgraph_BuildInstants(module);
    Dtool_libp3display_BuildInstants(module);
    Dtool_libp3pipeline_BuildInstants(module);
    Dtool_libp3event_BuildInstants(module);
    Dtool_libp3gobj_BuildInstants(module);
    Dtool_libp3gsgbase_BuildInstants(module);
    Dtool_libp3linmath_BuildInstants(module);
    Dtool_libp3mathutil_BuildInstants(module);
    Dtool_libp3parametrics_BuildInstants(module);
    Dtool_libp3pnmimage_BuildInstants(module);
    Dtool_libp3text_BuildInstants(module);
    Dtool_libp3tform_BuildInstants(module);
    Dtool_libp3putil_BuildInstants(module);
    Dtool_libp3audio_BuildInstants(module);
    Dtool_libp3nativenet_BuildInstants(module);
    Dtool_libp3net_BuildInstants(module);
    Dtool_libp3pgui_BuildInstants(module);
    Dtool_libp3movies_BuildInstants(module);
    Dtool_libp3dxml_BuildInstants(module);
    Dtool_libp3pnmtext_BuildInstants(module);
  }
}

#ifndef NDEBUG
PyObject *PyInit_core() {
  PyErr_SetString(PyExc_ImportError, "panda3d.core was compiled for Python " PY_VERSION ", which is incompatible with Python 3");
  return (PyObject *)NULL;
}
#endif
#endif

