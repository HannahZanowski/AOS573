"""
A python module for making cartopy polar stereographic plots
with circular axes.
"""
import numpy as np
import matplotlib.path as mpath

def make_ax_circular(axis):
    """ Make a cartopy plotting axis that is circular instead of rectangular.
    See https://scitools.org.uk/cartopy/docs/v0.15/examples/always_circular_stereo.html
    
    PARAMETERS
    ----------
    axis : a cartopy.mpl.geoaxes instance
    
    RETURNS
    ----------
    axis : the same cartopy.mpl.geoaxes instance but now circular
    """
    
    #Compute the angle
    theta = np.linspace(0, 2*np.pi, 100)
    
    #Center and radius of the circle
    center, radius = [0.5, 0.5], 0.5
    
    #Get the vertices of the points along the circle
    verts = np.vstack([np.sin(theta), np.cos(theta)]).T
    
    #Create the circle line using the vertices, radius,
    #and center of the circle
    circle = mpath.Path(verts * radius + center)
    
    #Set the axis boundary to be the created circle
    axis.set_boundary(circle, transform=axis.transAxes)
    
    return axis
