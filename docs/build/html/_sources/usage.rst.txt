Total-Operating-Characteristic Curve's Implementation
++++++++++++++++++++++++++++++++++++++++++++++++++++++

This project consist of classes and methods to compute and plot a TOC curve. The operations include, normalization, approximation by vectors (means of subsets of data).


TOC class
----------
.. autoclass:: ootoc::TOC
..    :members:   area, areaRatio, basenpos, basentppfp, kind, indices, ndata, npos, ntppfp,  PDataProp, TPplusFP, TP,  density, diff, normalize, plot, rank2prob, resample, vector

   
Area
====
.. autoattribute:: ootoc::TOC.area
   
Area Ratio
==========
.. autoattribute:: ootoc::TOC.areaRatio

Base number of positives
========================
.. autoattribute:: ootoc::TOC.basenpos

Base number of true positve plus false positives
================================================
.. autoattribute:: ootoc::TOC.basentppfp

Kind of TOC curve
=================
.. autoattribute:: ootoc::TOC.kind

Indices of the sorted rank
==========================
.. autoattribute:: ootoc::TOC.indices

Number of data
===============
.. autoattribute:: ootoc::TOC.ndata

Number of positive instances
=============================
.. autoattribute:: ootoc::TOC.npos

Number of true positives plus false positives
==============================================
.. autoattribute:: ootoc::TOC.ntppfp

Positive-class data proportion
==============================
.. autoattribute:: ootoc::TOC.PDataProp

Thresholds used for the TOC computation
=======================================
.. autoattribute:: ootoc::TOC.thresholds

Array of true positives plus false postives
===========================================
.. autoattribute:: ootoc::TOC.TPplusFP

Array of true positives
=======================
.. autoattribute:: ootoc::TOC.TP

Probability density function computation
========================================
.. automethod:: ootoc::TOC.density

Computation of the difference of two TOCs
=========================================
.. automethod:: ootoc::TOC.diff

TOC normalization
===================
.. automethod:: ootoc::TOC.normalize

Plotting the TOC curve
======================
.. automethod:: ootoc::TOC.plot

Compute a probability from a rank value
=======================================
.. automethod:: ootoc::TOC.rank2prob

Increasing the TOC data by interpolation
=========================================
.. automethod:: ootoc::TOC.resample
   

Vector representation of a TOC
===============================
.. automethod:: ootoc::TOC.vector   
   
   
   
TOCData class
--------------

This class is useful to translate longitude and latitud coordinates and values to a raster object (a rasterio file).
The intende use is to translate probabilities from the TOC density to a georeferenced raster object. 


.. autoclass:: tocdata::TOCData
..    :members:  DeltaLat,DeltaLon, lenLat, lenLon, maxLat, maxLon, minLat, minLon, nrow, ncol, raster, raster_file   


Pixel size in latitude and longitude units
==========================================
.. autoattribute:: tocdata::TOCData.DeltaLat
.. autoattribute:: tocdata::TOCData.DeltaLon

Dimensions of the raster in latitude and longitude units
========================================================
.. autoattribute:: tocdata::TOCData.lenLat
.. autoattribute:: tocdata::TOCData.lenLon

Bounding box of the raster in latitude and longitude units
==========================================================
.. autoattribute:: tocdata::TOCData.maxLat
.. autoattribute:: tocdata::TOCData.maxLon
.. autoattribute:: tocdata::TOCData.minLat
.. autoattribute:: tocdata::TOCData.minLon

Number of rows and cols of the raster
======================================
.. autoattribute:: tocdata::TOCData.nrow
.. autoattribute:: tocdata::TOCData.ncol

Raster matrix
==============
.. autoattribute:: tocdata::TOCData.raster

Raster file
============
.. autoattribute:: tocdata::TOCData.raster_file






