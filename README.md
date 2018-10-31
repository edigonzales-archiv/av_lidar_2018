# av_lidar_2018

gdaltindex lidar2018.shp /lidar2018/05_DTM_ASCII_25cm/*.asc




gdalbuildvrt (mit/ohne alpha)

gdal befehle 5m
gdal befehle 1 image (via vrt?)

ramps? color picker




gdalbuildvrt -addalpha dtm_25cm_hillshade.vrt *.tif

export GDAL_CACHEMAX=512
gdalwarp -tr 5.0 5.0 -of GTiff -co 'TILED=YES' -co 'PROFILE=GeoTIFF'  -co 'INTERLEAVE=PIXEL' -co 'COMPRESS=DEFLATE' -co 'PREDICTOR=2' -wo NUM_THREADS=ALL_CPUS -s_srs epsg:2056 -t_srs epsg:2056 dtm_25cm_hillshade.vrt dtm_5m_hillshade.tif

gdaladdo -r average dtm_5m_hillshade.tif 2 4 8 16 32 64 128 256



gdalbuildvrt -addalpha dom_25cm_hillshade.vrt *.tif

export GDAL_CACHEMAX=512
gdalwarp -tr 5.0 5.0 -of GTiff -co 'TILED=YES' -co 'PROFILE=GeoTIFF'  -co 'INTERLEAVE=PIXEL' -co 'COMPRESS=DEFLATE' -co 'PREDICTOR=2' -wo NUM_THREADS=ALL_CPUS -s_srs epsg:2056 -t_srs epsg:2056 dom_25cm_hillshade.vrt dom_25cm_hillshade.tif

gdaladdo -r average dom_25cm_hillshade.tif 2 4 8 16 32 64 128 256
