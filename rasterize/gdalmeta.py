#!/usr/bin/python
# -*- coding: utf-8 -*-

from osgeo import ogr, osr, gdal
import os
import sys

#gtif = gdal.Open( "/Samsung_T5/99_Derivate/buildings/tif/2590500_1254000_buildings.tif" )
gtif = gdal.Open( "/Samsung_T5/99_Derivate/buildings/tif/2590500_1253500_buildings.tif" )
print gtif.GetMetadata()

srcband = gtif.GetRasterBand(1)
print srcband

# falls alle vier stats = 0 -> leeres File -> löschen
stats = srcband.GetStatistics( True, True )
print stats[0]