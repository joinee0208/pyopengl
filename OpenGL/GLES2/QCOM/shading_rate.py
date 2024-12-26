'''OpenGL extension QCOM.shading_rate

This module customises the behaviour of the 
OpenGL.raw.GLES2.QCOM.shading_rate to provide a more 
Python-friendly API

Overview (from the spec)
	
	By default, OpenGL runs a fragment shader once for each pixel covered by a
	primitive being rasterized.  When using multisampling, the outputs of that
	fragment shader are broadcast to each covered sample of the fragment's
	pixel.  When using multisampling, applications can optionally request that
	the fragment shader be run once per color sample (e.g., by using the "sample"
	qualifier on one or more active fragment shader inputs), or run a minimum
	number of times per pixel using SAMPLE_SHADING enable and the
	MinSampleShading frequency value.
	
	This extension allows applications to specify fragment shading rates of less
	than 1 invocation per pixel.  Instead of invoking the fragment shader
	once for each covered pixel, the fragment shader can be run once for a
	group of adjacent pixels in the framebuffer.  The outputs of that fragment
	shader invocation are broadcast to each covered samples for all of the pixels
	in the group.  The initial version of this extension allows for groups of
	1, 2, 4, 8, and 16 pixels.
	
	This can be useful for effects like motion volumetric rendering
	where a portion of scene is processed at full shading rate and a portion can
	be processed at a reduced shading rate, saving power and processing resources.
	The requested rate can vary from (finest and default) 1 fragment shader
	invocation per pixel to (coarsest) one fragment shader invocation for each
	4x4 block of pixels.  Implementations are given wide latitude to rasterize
	at the requested rate or any other rate that is less coarse.

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/QCOM/shading_rate.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GLES2 import _types, _glgets
from OpenGL.raw.GLES2.QCOM.shading_rate import *
from OpenGL.raw.GLES2.QCOM.shading_rate import _EXTENSION_NAME

def glInitShadingRateQCOM():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )


### END AUTOGENERATED SECTION