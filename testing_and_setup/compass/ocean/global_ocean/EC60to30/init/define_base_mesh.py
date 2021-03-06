# /usr/bin/env python
"""
% Create cell width for this mesh on a regular latitude-longitude grid.
% Outputs:
%    cellWidth - m x n array, entries are desired cell width in km
%    lon - longitude, vector of length m, with entries between -180 and 180, degrees
%    lat - latitude, vector of length n, with entries between -90 and 90, degrees
"""
import numpy as np
import mesh_definition_tools as mdt


def cellWidthVsLatLon():
    lat = np.arange(-90, 90.01, 0.1)
    lon = np.arange(-180, 180.01, 10.0)

    cellWidthVsLat = mdt.EC_CellWidthVsLat(lat)
    cellWidth = np.outer(cellWidthVsLat, np.ones([1, lon.size]))

    return cellWidth, lon, lat
