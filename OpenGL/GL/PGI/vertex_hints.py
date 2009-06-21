'''OpenGL extension PGI.vertex_hints

This module customises the behaviour of the 
OpenGL.raw.GL.PGI.vertex_hints to provide a more 
Python-friendly API
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL.PGI.vertex_hints import *
### END AUTOGENERATED SECTION