'''Autogenerated by xml_generate script, do not edit!'''
from OpenGL import platform as _p, arrays
# Code generation uses this
from OpenGL.raw.GL import _types as _cs
# End users want this...
from OpenGL.raw.GL._types import *
from OpenGL.raw.GL import _errors
from OpenGL.constant import Constant as _C

import ctypes
_EXTENSION_NAME = 'GL_NV_primitive_shading_rate'
def _f( function ):
    return _p.createFunction( function,_p.PLATFORM.GL,'GL_NV_primitive_shading_rate',error_checker=_errors._error_checker)
GL_SHADING_RATE_IMAGE_PALETTE_COUNT_NV=_C('GL_SHADING_RATE_IMAGE_PALETTE_COUNT_NV',0x95B2)
GL_SHADING_RATE_IMAGE_PER_PRIMITIVE_NV=_C('GL_SHADING_RATE_IMAGE_PER_PRIMITIVE_NV',0x95B1)

