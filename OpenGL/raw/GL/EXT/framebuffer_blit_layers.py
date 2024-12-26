'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.raw.GL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GL_EXT_framebuffer_blit_layers'
def _f( function ):
    return _p.createFunction( function,_p.PLATFORM.GL,'GL_EXT_framebuffer_blit_layers',error_checker=_errors._error_checker)

@_f
@_p.types(None,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLbitfield,_cs.GLenum)
def glBlitFramebufferLayerEXT(srcX0,srcY0,srcX1,srcY1,srcLayer,dstX0,dstY0,dstX1,dstY1,dstLayer,mask,filter):pass
@_f
@_p.types(None,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLint,_cs.GLbitfield,_cs.GLenum)
def glBlitFramebufferLayersEXT(srcX0,srcY0,srcX1,srcY1,dstX0,dstY0,dstX1,dstY1,mask,filter):pass
