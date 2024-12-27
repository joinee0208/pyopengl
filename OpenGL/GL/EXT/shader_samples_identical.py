'''OpenGL extension EXT.shader_samples_identical

This module customises the behaviour of the 
OpenGL.raw.GL.EXT.shader_samples_identical to provide a more 
Python-friendly API

Overview (from the spec)
	
	Multisampled antialiasing has become a common method for improving the
	quality of rendered images.  Multisampling differs from supersampling in
	that the color of a primitive that covers all or part of a pixel is
	resolved once, regardless of the number of samples covered.  If a large
	polygon is rendered, the colors of all samples in each interior pixel will
	be the same.  This suggests a simple compression scheme that can reduce
	the necessary memory bandwidth requirements.  In one such scheme, each
	sample is stored in a separate slice of the multisample surface.  An
	additional multisample control surface (MCS) contains a mapping from pixel
	samples to slices.
	
	If all the values stored in the MCS for a particular pixel are the same,
	then all the samples have the same value.  Applications can take advantage
	of this information to reduce the bandwidth of reading multisample
	textures.  A custom multisample resolve filter could optimize resolving
	pixels where every sample is identical by reading the color once.
	
	color = texelFetch(sampler, coordinate, 0);
	if (!textureSamplesIdenticalEXT(sampler, coordinate)) {
	    for (int i = 1; i < MAX_SAMPLES; i++) {
	        vec4 c = texelFetch(sampler, coordinate, i);
	
	        //... accumulate c into color
	
	    }
	}

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/EXT/shader_samples_identical.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GL import _types, _glgets
from OpenGL.raw.GL.EXT.shader_samples_identical import *
from OpenGL.raw.GL.EXT.shader_samples_identical import _EXTENSION_NAME

def glInitShaderSamplesIdenticalEXT():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )


### END AUTOGENERATED SECTION