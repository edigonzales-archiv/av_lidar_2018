<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis maxScale="0" version="3.4.0-Madeira" hasScaleBasedVisibilityFlag="0" minScale="1e+8" styleCategories="AllStyleCategories">
  <flags>
    <Identifiable>1</Identifiable>
    <Removable>1</Removable>
    <Searchable>1</Searchable>
  </flags>
  <customproperties>
    <property key="WMSBackgroundLayer" value="false"/>
    <property key="WMSPublishDataSourceUrl" value="false"/>
    <property key="embeddedWidgets/count" value="0"/>
    <property key="identify/format" value="Value"/>
  </customproperties>
  <pipe>
    <rasterrenderer opacity="1" type="singlebandpseudocolor" classificationMax="11.7534" alphaBand="-1" classificationMin="0.3945" band="1">
      <rasterTransparency/>
      <minMaxOrigin>
        <limits>None</limits>
        <extent>WholeRaster</extent>
        <statAccuracy>Estimated</statAccuracy>
        <cumulativeCutLower>0.02</cumulativeCutLower>
        <cumulativeCutUpper>0.98</cumulativeCutUpper>
        <stdDevFactor>2</stdDevFactor>
      </minMaxOrigin>
      <rastershader>
        <colorrampshader classificationMode="1" colorRampType="INTERPOLATED" clip="0">
          <colorramp name="[source]" type="gradient">
            <prop v="250,250,250,255" k="color1"/>
            <prop v="5,5,5,255" k="color2"/>
            <prop v="0" k="discrete"/>
            <prop v="gradient" k="rampType"/>
          </colorramp>
          <item label="0.394" alpha="255" color="#ffd8d8" value="0.394499987363815"/>
          <item label="11.8" alpha="255" color="#ff9999" value="11.753399848938"/>
        </colorrampshader>
      </rastershader>
    </rasterrenderer>
    <brightnesscontrast contrast="0" brightness="0"/>
    <huesaturation grayscaleMode="0" colorizeBlue="128" colorizeGreen="128" saturation="0" colorizeStrength="100" colorizeRed="255" colorizeOn="0"/>
    <rasterresampler maxOversampling="4" zoomedOutResampler="bilinear"/>
  </pipe>
  <blendMode>6</blendMode>
</qgis>
