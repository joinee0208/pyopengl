'''OpenGL extension EXT.framebuffer_blit_layers

This module customises the behaviour of the 
OpenGL.raw.GL.EXT.framebuffer_blit_layers to provide a more 
Python-friendly API

Overview (from the spec)
	
	This extensions defines the behaviour for copying data from one layered
	framebuffer to another layered framebuffer.

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/EXT/framebuffer_blit_layers.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GL import _types, _glgets
from OpenGL.raw.GL.EXT.framebuffer_blit_layers import *
from OpenGL.raw.GL.EXT.framebuffer_blit_layers import _EXTENSION_NAME

def glInitFramebufferBlitLayersEXT():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )


### END AUTOGENERATED SECTION