# Noise-Prediction-Algorithm
<html><body><h2>Algorithm description</h2>
<p>Noise Estimation From Point Source Algorithm
British Standard - BS 5228-1:2009+A1:2014

Factors For consideration
1) the sound power outputs of processes and plant; 
2) the periods of operation of processes and plant; 
3) the distances from sources to receiver; 
4) the presence of screening by barriers; 
5) the reflection of sound; 
6) soft ground attenuation. 

Other factors such as meteorological conditions (particularly wind speed and direction) and atmospheric absorption can also influence the level of noise received. The estimation of the effects of these factors is complicated, not least because of interaction between these factors, and is beyond the scope of this standard.</p>
<h2>Input parameters</h2>
<h3>Dem File (PCS)</h3>
<p>Elevation (dem) can get easily from OpenTopgraphy Dem Downloader Plugin by extent(aoi). SRTM30m is recommended to use for large scale noise mapping.
<p>Download via https://github.com/knwin/OpenTopography-DEM-Downloader-qgis-plugin.
<p></p>
<h3>Creating Noise Source Point</h3>
<p>Point Source or Observer Location

This point should be the representative point for all project activities' noise sources. </p>
<h3>Receptor Areas/Polygon (residential & industrial)</h3>
<p>Receptors Layer must be polygon feature with no gemetory errors.

Attribute field & names must be standardized for model calculation steps. Field names (Unique id, landuse) are mandatory for tool. Others can be added for your study purposes optionally.

Remark:
Polygon can be 
- landuse area
- Categories accepted by model: residential, industrial
- Case Sensitive
- Wrong attribute and feild names, values will be invalid.
</p>
<h3>Noise Source Height</h3>
<p>Height of noise source (observer point)

Value can be customized more or less.
For example:
- 1.8 m or 1.7 m for human average height
- 20 m, 30 m, etc... for building height
- etc...</p>
<h3>CRS (Choose PCS)</h3>
<p>CRS (Coordinate Reference System)
PCS (Projected Coordinate System)

CRS should be PCS for some calculation in model algroithm such as viewshed analysis, distance analysis, etc...). This input CRS will be used in all model calculation steps.

For example:
- WGS84 UTM 46N</p>
<h3>Grid Value For Output Resolution</h3>
<p>Horizontal Grid Length Meter
Vertical Grid Length Meter

- Grid Value should be considered depend on your study extent/area and visual purpose. 
- Grid Value should not be less than and 30 m because input elevation pixel resolution is 30 m when the model extract the elevation values.

For example:
- 300 m x 300 m (horizontal x vertical)

<br><p align="right">Algorithm author: Htetarkar Soe</p><p align="right">Help author: Htetarkar Soe</p></body></html>
