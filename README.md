# av_lidar_2018

gdaltindex lidar2018.shp /lidar2018/05_DTM_ASCII_25cm/*.asc




gdalbuildvrt (mit/ohne alpha)

gdal befehle 5m
gdal befehle 1 image (via vrt?)

ramps? color picker

**DTM:**
```
gdalbuildvrt -addalpha dtm_25cm.vrt *.tif

export GDAL_CACHEMAX=2048
gdalwarp -tr 5.0 5.0 -r bilinear -of GTiff -co 'TILED=YES' -co 'PROFILE=GeoTIFF'  -co 'INTERLEAVE=PIXEL' -co 'COMPRESS=DEFLATE' -co 'PREDICTOR=2' -wo NUM_THREADS=ALL_CPUS -s_srs epsg:2056 -t_srs epsg:2056 dtm_25cm.vrt dtm_5m.tif
gdaladdo -r average dtm_5m.tif 2 4 8 16 32 64 128 256

gdalwarp -tr 2.0 2.0 -r bilinear -of GTiff -co 'TILED=YES' -co 'PROFILE=GeoTIFF'  -co 'INTERLEAVE=PIXEL' -co 'COMPRESS=DEFLATE' -co 'PREDICTOR=2' -wo NUM_THREADS=ALL_CPUS -s_srs epsg:2056 -t_srs epsg:2056 dtm_25cm.vrt dtm_2m.tif
gdaladdo -r average dtm_2m.tif 2 4 8 16 32 64 128 256

gdalwarp -tr 1.0 1.0 -r bilinear -of GTiff -co 'TILED=YES' -co 'PROFILE=GeoTIFF'  -co 'INTERLEAVE=PIXEL' -co 'COMPRESS=DEFLATE' -co 'PREDICTOR=2' -wo NUM_THREADS=ALL_CPUS -s_srs epsg:2056 -t_srs epsg:2056 dtm_25cm.vrt dtm_1m.tif
gdaladdo -r average dtm_1m.tif 2 4 8 16 32 64 128 256

gdalwarp -tr 0.5 0.5 -r bilinear -of GTiff -co 'BIGTIFF=YES' -co 'TILED=YES' -co 'PROFILE=GeoTIFF'  -co 'INTERLEAVE=PIXEL' -co 'COMPRESS=DEFLATE' -co 'PREDICTOR=2' -wo NUM_THREADS=ALL_CPUS -s_srs epsg:2056 -t_srs epsg:2056 dtm_25cm.vrt dtm_50cm.tif
gdaladdo -r average dtm_50cm.tif 2 4 8 16 32 64 128 256


```

**DOM:**
```
gdalbuildvrt -addalpha dom_25cm.vrt *.tif

export GDAL_CACHEMAX=2048
gdalwarp -tr 5.0 5.0 -r bilinear -of GTiff -co 'TILED=YES' -co 'PROFILE=GeoTIFF'  -co 'INTERLEAVE=PIXEL' -co 'COMPRESS=DEFLATE' -co 'PREDICTOR=2' -wo NUM_THREADS=ALL_CPUS -s_srs epsg:2056 -t_srs epsg:2056 dom_25cm.vrt dom_5m.tif
gdaladdo -r average dom_5m.tif 2 4 8 16 32 64 128 256

gdalwarp -tr 2.0 2.0 -r bilinear -of GTiff -co 'TILED=YES' -co 'PROFILE=GeoTIFF'  -co 'INTERLEAVE=PIXEL' -co 'COMPRESS=DEFLATE' -co 'PREDICTOR=2' -wo NUM_THREADS=ALL_CPUS -s_srs epsg:2056 -t_srs epsg:2056 dom_25cm.vrt dom_2m.tif
gdaladdo -r average dom_2m.tif 2 4 8 16 32 64 128 256

gdalwarp -tr 1.0 1.0 -r bilinear -of GTiff -co 'TILED=YES' -co 'PROFILE=GeoTIFF'  -co 'INTERLEAVE=PIXEL' -co 'COMPRESS=DEFLATE' -co 'PREDICTOR=2' -wo NUM_THREADS=ALL_CPUS -s_srs epsg:2056 -t_srs epsg:2056 dom_25cm.vrt dom_1m.tif
gdaladdo -r average dom_1m.tif 2 4 8 16 32 64 128 256

gdalwarp -tr 0.5 0.5 -r bilinear -of GTiff -co 'BIGTIFF=YES' -co 'TILED=YES' -co 'PROFILE=GeoTIFF'  -co 'INTERLEAVE=PIXEL' -co 'COMPRESS=DEFLATE' -co 'PREDICTOR=2' -wo NUM_THREADS=ALL_CPUS -s_srs epsg:2056 -t_srs epsg:2056 dom_25cm.vrt dom_50cm.tif
gdaladdo -r average dom_50cm.tif 2 4 8 16 32 64 128 256


```




**DTM Hillshade:**
```
gdalbuildvrt -addalpha dtm_25cm_hillshade.vrt *.tif

export GDAL_CACHEMAX=2048
gdalwarp -tr 5.0 5.0 -r bilinear -of GTiff -co 'TILED=YES' -co 'PROFILE=GeoTIFF'  -co 'INTERLEAVE=PIXEL' -co 'COMPRESS=DEFLATE' -co 'PREDICTOR=2' -wo NUM_THREADS=ALL_CPUS -s_srs epsg:2056 -t_srs epsg:2056 dtm_25cm_hillshade.vrt dtm_5m_hillshade.tif

gdaladdo -r average dtm_5m_hillshade.tif 2 4 8 16 32 64 128 256

# Version 2 (via 5m DTM)
gdaldem hillshade -compute_edges -multidirectional ../dtm_25cm/dtm_5m.tif dtm_5m_hillshade_v2.tif
gdaladdo -r average dtm_5m_hillshade_v2.tif 2 4 8 16 32 64 128 256

gdaldem hillshade -compute_edges -multidirectional ../dtm_25cm/dtm_2m.tif dtm_2m_hillshade_v2.tif
gdaladdo -r average dtm_2m_hillshade_v2.tif 2 4 8 16 32 64 128 256

gdaldem hillshade -compute_edges -multidirectional ../dtm_25cm/dtm_1m.tif dtm_1m_hillshade_v2.tif
gdaladdo -r average dtm_1m_hillshade_v2.tif 2 4 8 16 32 64 128 256

gdaldem hillshade -co 'BIGTIFF=YES' -compute_edges -multidirectional ../dtm_25cm/dtm_50cm.tif dtm_50cm_hillshade_v2.tif
gdaladdo -r average dtm_50cm_hillshade_v2.tif 2 4 8 16 32 64 128 256

# Einzelnes 25cm BigTIFF
export GDAL_CACHEMAX=2048
gdalwarp -tr 0.25 0.25 -of GTiff  -co 'BIGTIFF=YES' -co 'TILED=YES' -co 'PROFILE=GeoTIFF'  -co 'INTERLEAVE=PIXEL' -co 'COMPRESS=DEFLATE' -co 'PREDICTOR=2' -wo NUM_THREADS=ALL_CPUS -s_srs epsg:2056 -t_srs epsg:2056 dtm_25cm_hillshade.vrt dtm_25cm_hillshade.tif

gdaladdo -ro -r average dtm_25cm_hillshade.tif 2
gdaladdo -ro -r average dtm_25cm_hillshade.tif.ovr 2
gdaladdo -ro -r average dtm_25cm_hillshade.tif.ovr.ovr 2
gdaladdo -ro -r average dtm_25cm_hillshade.tif.ovr.ovr.ovr 2
gdaladdo -ro -r average dtm_25cm_hillshade.tif.ovr.ovr.ovr.ovr 2
gdaladdo -ro -r average dtm_25cm_hillshade.tif.ovr.ovr.ovr.ovr.ovr 2
gdaladdo -ro -r average dtm_25cm_hillshade.tif.ovr.ovr.ovr.ovr.ovr.ovr 2
gdaladdo -ro -r average dtm_25cm_hillshade.tif.ovr.ovr.ovr.ovr.ovr.ovr.ovr 2
gdal_translate dtm_25cm_hillshade.tif dtm_25cm_hillshade_with_ovr.tif -co 'COPY_SRC_OVERVIEWS=YES' -co 'COMPRESS=DEFLATE' -co 'PREDICTOR=2' -co 'TILED=YES' -co 'BIGTIFF=YES'

```



**DOM Hillshade:**
```
gdalbuildvrt -addalpha dom_25cm_hillshade.vrt *.tif

export GDAL_CACHEMAX=2048
gdalwarp -tr 5.0 5.0 -r bilinear -of GTiff -co 'TILED=YES' -co 'PROFILE=GeoTIFF'  -co 'INTERLEAVE=PIXEL' -co 'COMPRESS=DEFLATE' -co 'PREDICTOR=2' -wo NUM_THREADS=ALL_CPUS -s_srs epsg:2056 -t_srs epsg:2056 dom_25cm_hillshade.vrt dom_5m_hillshade.tif

gdaladdo -r average dom_5m_hillshade.tif 2 4 8 16 32 64 128 256

# Version 2 (via 5m DOM)
gdaldem hillshade -compute_edges -multidirectional ../dom_25cm/dom_5m.tif dom_5m_hillshade_v2.tif
gdaladdo -r average dom_5m_hillshade_v2.tif 2 4 8 16 32 64 128 256

gdaldem hillshade -compute_edges -multidirectional ../dom_25cm/dom_2m.tif dom_2m_hillshade_v2.tif
gdaladdo -r average dom_2m_hillshade_v2.tif 2 4 8 16 32 64 128 256

gdaldem hillshade -compute_edges -multidirectional ../dom_25cm/dom_1m.tif dom_1m_hillshade_v2.tif
gdaladdo -r average dom_1m_hillshade_v2.tif 2 4 8 16 32 64 128 256

gdaldem hillshade -co 'BIGTIFF=YES' -compute_edges -multidirectional ../dom_25cm/dom_50cm.tif dom_50cm_hillshade_v2.tif
gdaladdo -r average dom_50cm_hillshade_v2.tif 2 4 8 16 32 64 128 256


# Einzelnes 25cm BigTIFF
export GDAL_CACHEMAX=2048
gdalwarp -tr 0.25 0.25 -of GTiff -co 'BIGTIFF=YES' -co 'TILED=YES' -co 'PROFILE=GeoTIFF'  -co 'INTERLEAVE=PIXEL' -co 'COMPRESS=DEFLATE' -co 'PREDICTOR=2' -wo NUM_THREADS=ALL_CPUS -s_srs epsg:2056 -t_srs epsg:2056 dom_25cm_hillshade.vrt dom_25cm_hillshade.tif

export GDAL_CACHEMAX=2048
gdaladdo -ro -r average dom_25cm_hillshade.tif 2
gdaladdo -ro -r average dom_25cm_hillshade.tif.ovr 2
gdaladdo -ro -r average dom_25cm_hillshade.tif.ovr.ovr 2
gdaladdo -ro -r average dom_25cm_hillshade.tif.ovr.ovr.ovr 2
gdaladdo -ro -r average dom_25cm_hillshade.tif.ovr.ovr.ovr.ovr 2
gdaladdo -ro -r average dom_25cm_hillshade.tif.ovr.ovr.ovr.ovr.ovr 2
gdaladdo -ro -r average dom_25cm_hillshade.tif.ovr.ovr.ovr.ovr.ovr.ovr 2
gdaladdo -ro -r average dom_25cm_hillshade.tif.ovr.ovr.ovr.ovr.ovr.ovr.ovr 2

gdal_translate dom_25cm_hillshade.tif dom_25cm_hillshade_with_ovr.tif -co 'COPY_SRC_OVERVIEWS=YES' -co 'COMPRESS=DEFLATE' -co 'PREDICTOR=2' -co 'TILED=YES' -co 'BIGTIFF=YES'

```


**DOM Hillshade default**
```
gdalbuildvrt -addalpha dom_25cm_hillshade.vrt *.tif

export GDAL_CACHEMAX=2048
gdalwarp -tr 0.25 0.25 -of GTiff -co 'BIGTIFF=YES' -co 'TILED=YES' -co 'PROFILE=GeoTIFF'  -co 'INTERLEAVE=PIXEL' -co 'COMPRESS=DEFLATE' -co 'PREDICTOR=2' -wo NUM_THREADS=ALL_CPUS -s_srs epsg:2056 -t_srs epsg:2056 dom_25cm_hillshade.vrt dom_25cm_hillshade.tif

gdaladdo -ro -r average dom_25cm_hillshade.tif 2
gdaladdo -ro -r average dom_25cm_hillshade.tif.ovr 2
gdaladdo -ro -r average dom_25cm_hillshade.tif.ovr.ovr 2
gdaladdo -ro -r average dom_25cm_hillshade.tif.ovr.ovr.ovr 2
gdaladdo -ro -r average dom_25cm_hillshade.tif.ovr.ovr.ovr.ovr 2
gdaladdo -ro -r average dom_25cm_hillshade.tif.ovr.ovr.ovr.ovr.ovr 2
gdaladdo -ro -r average dom_25cm_hillshade.tif.ovr.ovr.ovr.ovr.ovr.ovr 2
gdaladdo -ro -r average dom_25cm_hillshade.tif.ovr.ovr.ovr.ovr.ovr.ovr.ovr 2
gdaladdo -ro -r average dom_25cm_hillshade.tif.ovr.ovr.ovr.ovr.ovr.ovr.ovr.ovr 2

gdal_translate dom_25cm_hillshade.tif dom_25cm_hillshade_with_ovr.tif -co 'COPY_SRC_OVERVIEWS=YES' -co 'COMPRESS=DEFLATE' -co 'PREDICTOR=2' -co 'TILED=YES' -co 'BIGTIFF=YES'

```


**DTM Slope**:
```
gdalbuildvrt -addalpha dtm_25cm_slope.vrt *.tif

# Einzelnes 25cm BigTIFF
export GDAL_CACHEMAX=2048
gdalwarp -tr 0.25 0.25 -of GTiff -co 'BIGTIFF=YES' -co 'TILED=YES' -co 'PROFILE=GeoTIFF'  -co 'INTERLEAVE=PIXEL' -co 'COMPRESS=DEFLATE' -co 'PREDICTOR=2' -wo NUM_THREADS=ALL_CPUS -s_srs epsg:2056 -t_srs epsg:2056 dtm_25cm_slope.vrt dtm_25cm_slope.tif

gdaladdo -ro -r average dtm_25cm_slope.tif 2
gdaladdo -ro -r average dtm_25cm_slope.tif.ovr 2
gdaladdo -ro -r average dtm_25cm_slope.tif.ovr.ovr 2
gdaladdo -ro -r average dtm_25cm_slope.tif.ovr.ovr.ovr 2
gdaladdo -ro -r average dtm_25cm_slope.tif.ovr.ovr.ovr.ovr 2
gdaladdo -ro -r average dtm_25cm_slope.tif.ovr.ovr.ovr.ovr.ovr 2
gdaladdo -ro -r average dtm_25cm_slope.tif.ovr.ovr.ovr.ovr.ovr.ovr 2
gdaladdo -ro -r average dtm_25cm_slope.tif.ovr.ovr.ovr.ovr.ovr.ovr.ovr 2

gdal_translate dtm_25cm_slope.tif dtm_25cm_slope_with_ovr.tif -co 'COPY_SRC_OVERVIEWS=YES' -co 'COMPRESS=DEFLATE' -co 'PREDICTOR=2' -co 'TILED=YES' -co 'BIGTIFF=YES'


```




**PDAL**:

```
gdalbuildvrt -addalpha buildings_25cm.vrt *.tif

export GDAL_CACHEMAX=2048
gdalwarp -tr 0.25 0.25 -of GTiff -co 'BIGTIFF=YES' -co 'TILED=YES' -co 'PROFILE=GeoTIFF'  -co 'INTERLEAVE=PIXEL' -co 'COMPRESS=DEFLATE' -co 'PREDICTOR=2' -wo NUM_THREADS=ALL_CPUS -s_srs epsg:2056 -t_srs epsg:2056 buildings_25cm.vrt buildings_25cm.tif

gdaladdo -ro -r average buildings_25cm.tif 2
gdaladdo -ro -r average buildings_25cm.tif.ovr 2
gdaladdo -ro -r average buildings_25cm.tif.ovr.ovr 2
gdaladdo -ro -r average buildings_25cm.tif.ovr.ovr.ovr 2
gdaladdo -ro -r average buildings_25cm.tif.ovr.ovr.ovr.ovr 2
gdaladdo -ro -r average buildings_25cm.tif.ovr.ovr.ovr.ovr.ovr 2
gdaladdo -ro -r average buildings_25cm.tif.ovr.ovr.ovr.ovr.ovr.ovr 2
gdaladdo -ro -r average buildings_25cm.tif.ovr.ovr.ovr.ovr.ovr.ovr.ovr 2

gdal_translate buildings_25cm.tif buildings_25cm_with_ovr.tif -co 'COPY_SRC_OVERVIEWS=YES' -co 'COMPRESS=DEFLATE' -co 'PREDICTOR=2' -co 'TILED=YES' -co 'BIGTIFF=YES'


----


gdalbuildvrt -addalpha vegetation_25cm.vrt *.tif

export GDAL_CACHEMAX=2048
gdalwarp -tr 0.25 0.25 -of GTiff -co 'BIGTIFF=YES' -co 'TILED=YES' -co 'PROFILE=GeoTIFF'  -co 'INTERLEAVE=PIXEL' -co 'COMPRESS=DEFLATE' -co 'PREDICTOR=2' -wo NUM_THREADS=ALL_CPUS -s_srs epsg:2056 -t_srs epsg:2056 vegetation_25cm.vrt vegetation_25cm.tif

gdaladdo -ro -r average vegetation_25cm.tif 2
gdaladdo -ro -r average vegetation_25cm.tif.ovr 2
gdaladdo -ro -r average vegetation_25cm.tif.ovr.ovr 2
gdaladdo -ro -r average vegetation_25cm.tif.ovr.ovr.ovr 2
gdaladdo -ro -r average vegetation_25cm.tif.ovr.ovr.ovr.ovr 2
gdaladdo -ro -r average vegetation_25cm.tif.ovr.ovr.ovr.ovr.ovr 2
gdaladdo -ro -r average vegetation_25cm.tif.ovr.ovr.ovr.ovr.ovr.ovr 2
gdaladdo -ro -r average vegetation_25cm.tif.ovr.ovr.ovr.ovr.ovr.ovr.ovr 2
gdaladdo -ro -r average vegetation_25cm.tif.ovr.ovr.ovr.ovr.ovr.ovr.ovr.ovr 2

gdal_translate vegetation_25cm.tif vegetation_25cm_with_ovr.tif -co 'COPY_SRC_OVERVIEWS=YES' -co 'COMPRESS=DEFLATE' -co 'PREDICTOR=2' -co 'TILED=YES' -co 'BIGTIFF=YES'




docker run -v /lidar2018/01_Punktwolke_LAS:/input -v /Samsung_T5/99_Derivate/buildings/las:/output pdal/pdal pdal translate -i /input/2590500_1253500.las -o /output/2590500_1253500_buildings.las -f range --filters.range.limits="Classification[6:6]"



docker run -v /lidar2018/01_Punktwolke_LAS:/input -v /Samsung_T5/99_Derivate/buildings/las:/output pdal/pdal pdal translate -i /input/2590500_1253500.las -o /output/2590500_1253500_hag_as_Z.las hag ferry --filters.ferry.dimensions="HeightAboveGround=Z"

docker run -v /lidar2018/01_Punktwolke_LAS:/input -v /Samsung_T5/99_Derivate/buildings/las:/output pdal/pdal pdal translate -i /input/2590500_1253500.las -o /output/2590500_1253500_hag_as_Z_buildings_fuuu.las hag ferry range --filters.ferry.dimensions="HeightAboveGround=Z" --filters.range.limits="Classification[6:6]"



docker run -v /Samsung_T5/99_Derivate/buildings:/input -v /Samsung_T5/99_Derivate/buildings/las:/output pdal/pdal pdal translate -i /output/2590500_1253500_hag_as_Z.las -o /output/2590500_1253500_hag_as_Z_buildings.las -f range --filters.range.limits="Classification[6:6]"



docker run -v /lidar2018/01_Punktwolke_LAS:/input pdal/pdal pdal info -i /intput/2590500_1254000.las


docker run -v /vagrant/rasterize:/data -v /Samsung_T5/99_Derivate/buildings/las:/input -v /Samsung_T5/99_Derivate/buildings/tif:/output pdal/pdal pdal pipeline --nostream  /data/rasterize.json

docker run -v /vagrant/rasterize:/data -v /lidar2018/01_Punktwolke_LAS:/input -v /Samsung_T5/99_Derivate/buildings/las:/output  pdal/pdal pdal pipeline --nostream /data/rasterize.json
docker run -v /vagrant/rasterize:/data -v /lidar2018/01_Punktwolke_LAS:/input -v /Samsung_T5/99_Derivate/buildings/las:/output  pdal/pdal pdal pipeline --nostream --readers.las.filename="/input/2590500_1254000.las" /data/rasterize.json


```