#!/usr/bin/python
# -*- coding: utf-8 -*-

from osgeo import ogr, osr
import os
import sys

#INPATH = "/lidar2018/05_DTM_ASCII_25cm/"
INPATH = "/lidar2018/07_DOM_ASCII_25cm/"
#OUTPATH = "/lidar2018/99_Derivate/dtm_25cm/"
OUTPATH = "/lidar2018/99_Derivate/dom_25cm/"
#TMPPATH = "/tmp/"
TMPPATH = "/tmp/dom/"

shp = ogr.Open("../tileindex/lidar2018.shp")
layer = shp.GetLayer(0)

for feature in layer:
    infile = feature.GetField('location')
    path, infileName = os.path.split(infile)
    print "**********************: " + infileName

    basename = os.path.splitext(infileName)[0]
    infile = os.path.join(INPATH, infileName)
    outfile = os.path.join(TMPPATH, basename + ".tif")
    cmd = "gdal_translate -a_srs epsg:2056  -of GTiff -co 'TILED=YES' "
    cmd += infile + " " + outfile
    print cmd
    os.system(cmd)
    print "**********************: "

    infile = outfile
    outfile = os.path.join(OUTPATH, basename + ".tif")
    cmd = "gdal_translate -a_srs epsg:2056  -of GTiff -co 'TILED=YES' -co 'COMPRESS=DEFLATE' -co 'PREDICTOR=2' "
    cmd += "-ot Float32 " + infile + " " + outfile
    print cmd
    os.system(cmd)
    print "**********************: "

    infile = outfile
    cmd = "gdaladdo -r average " + infile + " 2 4 8 16 32"
    print cmd
    os.system(cmd)

    cmd = "rm " + os.path.join(TMPPATH, "*.tif")
    print cmd
    os.system(cmd)
    print "**********************: "

