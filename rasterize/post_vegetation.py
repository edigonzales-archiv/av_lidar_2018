#!/usr/bin/python
# -*- coding: utf-8 -*-

from osgeo import ogr, osr
import os
import sys

VRT = "/lidar2018/99_Derivate/dtm_25cm/dtm_25cm.vrt"
TINDEX = "../tileindex/lidar2018.shp"
INPATH = "/Samsung_T5/99_Derivate/vegetation/tif.orig"
OUTPATH = "/Samsung_T5/99_Derivate/vegetation/tif"
TMPPATH = "/tmp/vegetation/"
BUFFER = 10

shp = ogr.Open("../tileindex/lidar2018.shp")
layer = shp.GetLayer(0)

for feature in layer:
    infile = feature.GetField('location')
    path, infileName = os.path.split(infile)
    basename = os.path.splitext(infileName)[0]
    print "**********************: " + infileName

    geom = feature.GetGeometryRef()
    env = geom.GetEnvelope()

    minX = int(env[0] + 0.001)
    minY = int(env[2] + 0.001)
    maxX = int(env[1] + 0.001)
    maxY = int(env[3] + 0.001)
    
    print minX 
    print minY

    cmd = "mkdir -p " + TMPPATH
    #print cmd
    #os.system(cmd)

    infile = os.path.join(INPATH, basename + "_vegetation.tif")
    outfile = os.path.join(OUTPATH, basename + "_vegetation.tif")
    cmd = "gdal_translate -a_srs epsg:2056 "
    cmd += " -co 'TILED=YES' -co 'PROFILE=GeoTIFF'"
    cmd += " -co 'INTERLEAVE=PIXEL' -co 'COMPRESS=DEFLATE' -co 'PREDICTOR=2' "
    cmd += " -r bilinear " + infile + " " + outfile
    print cmd
    os.system(cmd)

    cmd = "gdaladdo -r average "
    cmd += outfile + " 2 4 8 16 32 64 "
    print cmd
    os.system(cmd)

    cmd = "rm -rf " + TMPPATH
    #print cmd
    #os.system(cmd)
