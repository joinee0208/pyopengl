'''OpenGL extension HP.texture_lighting

This module customises the behaviour of the 
OpenGL.raw.GL.HP.texture_lighting to provide a more 
Python-friendly API
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL.HP.texture_lighting import *
### END AUTOGENERATED SECTION