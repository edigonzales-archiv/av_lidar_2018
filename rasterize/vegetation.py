#!/usr/bin/python
# -*- coding: utf-8 -*-

from osgeo import ogr, osr
import os
import sys

#VRT = "/lidar2018/99_Derivate/dtm_25cm/dtm_25cm.vrt"
TINDEX = "../tileindex/lidar2018.shp"
INPATH = "/lidar2018/01_Punktwolke_LAS/"
OUTPATH = "/Samsung_T5/99_Derivate/vegetation/tif/"
#TMPPATH = "/tmp/hillshade/dtm/"
#BUFFER = 10

shp = ogr.Open(TINDEX)
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
    
    bounds = "(["+str(minX)+","+str(maxX-0.25)+"],["+str(minY)+","+str(maxY-0.25)+"])"

    #cmd = 'docker run -v /vagrant/rasterize:/data -v /lidar2018/01_Punktwolke_LAS:/input -v /Samsung_T5/99_Derivate/buildings/tif:/output pdal/pdal pdal pipeline --nostream --readers.las.filename="/input/'+basename+'.las" --writers.gdal.filename="/output/'+basename+'_buildings.tif" --filters.range.limits="Classification[6:6]" /data/rasterize.json'
    cmd = 'docker run -v /vagrant/rasterize:/data -v /lidar2018/01_Punktwolke_LAS:/input -v /Samsung_T5/99_Derivate/vegetation/tif:/output pdal/pdal pdal pipeline --nostream --readers.las.filename="/input/'+basename+'.las" --writers.gdal.filename="/output/'+basename+'_vegetation.tif" --writers.gdal.bounds="'+bounds+'" --filters.range.limits="Classification[4:5]" /data/rasterize.json'
    print cmd
    x = os.system(cmd)


#docker run -v /vagrant/rasterize:/data -v /lidar2018/01_Punktwolke_LAS:/input -v /Samsung_T5/99_Derivate/vegetation/tif:/output pdal/pdal pdal pipeline --nostream --readers.las.filename="/input/2593000_1252000.las" --writers.gdal.filename="/output/2593000_1252000_vegetation.tif" --writers.gdal.bounds="([2593000,2593499.75],[1252000,1252499.75])" --filters.range.limits="Classification[4:5]" /data/rasterize.json
#(pdal pipeline readers.las Error) Invalid SRS specification.  GeoTiff not allowed with point formats 6 - 10.

#docker run -v /vagrant/rasterize:/data -v /lidar2018/01_Punktwolke_LAS:/input -v /Samsung_T5/99_Derivate/vegetation/tif:/output pdal/pdal pdal pipeline --nostream --readers.las.filename="/input/2593500_1252000.las" --writers.gdal.filename="/output/2593500_1252000_vegetation.tif" --writers.gdal.bounds="([2593500,2593999.75],[1252000,1252499.75])" --filters.range.limits="Classification[4:5]" /data/rasterize.json
#(pdal pipeline readers.las Error) Invalid SRS specification.  GeoTiff not allowed with point formats 6 - 10.

#docker run -v /vagrant/rasterize:/data -v /lidar2018/01_Punktwolke_LAS:/input -v /Samsung_T5/99_Derivate/vegetation/tif:/output pdal/pdal pdal pipeline --nostream --readers.las.filename="/input/2597000_1253000.las" --writers.gdal.filename="/output/2597000_1253000_vegetation.tif" --writers.gdal.bounds="([2597000,2597499.75],[1253000,1253499.75])" --filters.range.limits="Classification[4:5]" /data/rasterize.json
#(pdal pipeline readers.las Error) Invalid SRS specification.  GeoTiff not allowed with point formats 6 - 10.

#docker run -v /vagrant/rasterize:/data -v /lidar2018/01_Punktwolke_LAS:/input -v /Samsung_T5/99_Derivate/vegetation/tif:/output pdal/pdal pdal pipeline --nostream --readers.las.filename="/input/2598000_1253000.las" --writers.gdal.filename="/output/2598000_1253000_vegetation.tif" --writers.gdal.bounds="([2598000,2598499.75],[1253000,1253499.75])" --filters.range.limits="Classification[4:5]" /data/rasterize.json
#(pdal pipeline readers.las Error) Invalid SRS specification.  GeoTiff not allowed with point formats 6 - 10.