#include "ccircle.h"

/* TODO : Free gl handle */

typedef struct {
  PyObject_HEAD
  uint handle;
} CC_Image;

static int CC_Image_Init ( CC_Image* self, PyObject* args ) {
  if (!CC_GLContext_Exists())
    Fatal("A window must be created before images can be loaded");

  cstr path;
  if (!PyArg_ParseTuple(args, "s", &path))
    return -1;

  int sx, sy, channels;
  uchar* data = CC_Image_Load(path, &sx, &sy, &channels);
  if (!data)
    return -1;

  if (channels != 3 && channels != 4) {
    Fatal("Image type unsupported: must have 3 or 4 channels");
    return -1;
  }

  glGenTextures(1, &self->handle);
  glBindTexture(GL_TEXTURE_2D, self->handle);
  glPixelStorei(GL_PACK_ALIGNMENT, 1);
  glPixelStorei(GL_UNPACK_ALIGNMENT, 1);
  glTexImage2D(GL_TEXTURE_2D,
    0,
    GL_RGBA8,
    sx, sy, 0,
    channels == 3 ? GL_RGB : GL_RGBA,
    GL_UNSIGNED_BYTE,
    data);

  glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR);
  glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR);
  CC_Image_Free(data);
  return 0;
}

/* --- Image::draw ---------------------------------------------------------- */

static PyObject* CC_Image_Draw ( CC_Image* self, PyObject* args ) {
  float x, y, sx, sy;
  float angle = 0;
  if (!PyArg_ParseTuple(args, "ffff|f", &x, &y, &sx, &sy, &angle))
    return 0;

  glEnable(GL_TEXTURE_2D);
  glBindTexture(GL_TEXTURE_2D, self->handle);
  glColor4f(1, 1, 1, 1);

  glMatrixMode(GL_MODELVIEW);
  glPushMatrix();
  glLoadIdentity();
  glRotatef(angle, 0, 0, 1);

  glBegin(GL_QUADS);
  glTexCoord2f(0, 0); glVertex2f(x, y);
  glTexCoord2f(0, 1); glVertex2f(x, y + sy);
  glTexCoord2f(1, 1); glVertex2f(x + sx, y + sy);
  glTexCoord2f(1, 0); glVertex2f(x + sx, y);
  glEnd();

  glPopMatrix();
  glDisable(GL_TEXTURE_2D);
  Py_RETURN_NONE;
}

/* -------------------------------------------------------------------------- */

static PyMethodDef methods[] = {
  { "draw", (PyCFunction)CC_Image_Draw, METH_VARARGS,
    "Draw the image to the current window" },
  { 0 },
};


/* -------------------------------------------------------------------------- */

static PyTypeObject CC_Image_PyType = {
  PyVarObject_HEAD_INIT(0, 0)
  "ccircle.Image",
  sizeof(CC_Image),
  0,                                  /* tp_itemsize */
  0,                                  /* tp_dealloc */
  0,                                  /* tp_print */
  0,                                  /* tp_getattr */
  0,                                  /* tp_setattr */
  0,                                  /* tp_reserved */
  0,                                  /* tp_repr */
  0,                                  /* tp_as_number */
  0,                                  /* tp_as_sequence */
  0,                                  /* tp_as_mapping */
  0,                                  /* tp_hash  */
  0,                                  /* tp_call */
  0,                                  /* tp_str */
  0,                                  /* tp_getattro */
  0,                                  /* tp_setattro */
  0,                                  /* tp_as_buffer */
  Py_TPFLAGS_DEFAULT,                 /* tp_flags */
  "A 2D Image",                       /* tp_doc */
  0,                                  /* tp_traverse */
  0,                                  /* tp_clear */
  0,                                  /* tp_richcompare */
  0,                                  /* tp_weaklistoffset */
  0,                                  /* tp_iter */
  0,                                  /* tp_iternext */
  methods,                            /* tp_methods */
  0,                                  /* tp_members */
  0,                                  /* tp_getset */
  0,                                  /* tp_base */
  0,                                  /* tp_dict */
  0,                                  /* tp_descr_get */
  0,                                  /* tp_descr_set */
  0,                                  /* tp_dictoffset */
  (initproc)CC_Image_Init,            /* tp_init */
  0,                                  /* tp_alloc */
  0,                                  /* tp_new */
};

/* -------------------------------------------------------------------------- */

void CC_Init_Image ( PyObject* self ) {
  CC_Image_PyType.tp_new = PyType_GenericNew;
  if (PyType_Ready(&CC_Image_PyType) < 0) Fatal("Failed to create image type");
  Py_INCREF(self);
  PyModule_AddObject(self, "Image", (PyObject*)&CC_Image_PyType);
}
