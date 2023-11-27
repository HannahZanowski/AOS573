import numpy as np
import matplotlib.pyplot as plt
import cartopy
import cartopy.crs as ccrs
import pytest

from make_ax_circular.make_ax_circular_module import make_ax_circular

def test_make_ax_circular():
    #Check that we can't give the wrong type of axes
    with pytest.raises(AttributeError):
        make_ax_circular(plt.axes())

    #Check that we can't give the incorrect number of arguments
    with pytest.raises(TypeError):
        make_ax_circular(1,2)

    #Check that the output is a cartopy.mpl.geoaxes instance
    assert type(make_ax_circular(plt.axes(projection=ccrs.PlateCarree())))==cartopy.mpl.geoaxes.GeoAxesSubplot
