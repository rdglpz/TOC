#!/usr/bin/env python3

#Converting pandas data frame to raster
#TOC= Total Operating Characteristic Curve
#Author: S. Ivvan Valdez 
#Centro de Investigación en Ciencias de Información Geoespacial AC
#Querétaro, México.

import numpy as np
import copy
import rasterio
from rasterio.transform import from_origin
import matplotlib.pyplot as plt
from rasterio import CRS


class TOCData:
    
    """
    
    This class can be used to translate lon, lat and feature values to a raster file, and a raster matrix.
    The intended use it to translateprobabilities or values from a TOC that are assocaited with lat,lon coordinates, 
    to a raster for visualization.
    
    :param feature: numpy array of feature or probability values. 
    
    :param lat: latitude coordinate associated, index-wise, to a feature value.
    
    :param lon: longitude coordinate associated, index-wise,  to a feature value.
    
    :param rfile: name of the raster file that is created during the process.
    
    :return: TOCData object.
    
    :rtype: TOCData
    
    """
    
    DeltaLat=None
    """
    Size of a pixel in the latitude axes.
    """
    
    DeltaLon=None
    """
    Size of a pixel in the longitude axes.
    """
    
    minLat=None
    """
    Minimum latitude coordinate.
    """
   
    minLon=None
    """
    Minmum longitude coordinate.
    """

    maxLat=None
    """
    Maximum latitude coordinate.
    """
    
    maxLon=None
    """
    Maximum latitude coordinate.
    """
    
    lenLat=None
    """
    Length of the raster in the latitude axes.
    """

    lenLon=None
    """
    Length of the raster in the longitude axes.
    """    
    
    nrow=None
    """
    Number of rows in the raster.
    
    """
    
    ncol=None
    """
    
    Number of cols in the raster.
    
    """
    
    raster=None
    """
    
    Raster matrix .
    
    """
    
    raster_file=None
    """
    
    Reference to the raster file as a rasterior object.
    
    """
    crs=6365
    def __init__(self,feature, lat=np.array([]), lon=np.array([]),nrow=0,ncol=0,crs=32641,rfile='raster.tif'):
        if (len(lat)!=0 and len(lon)!=0):
            latdif=np.abs(lat[1:]-lat[:-1])
            londif=np.abs(lon[1:]-lon[:-1])
            Dlat=np.min(latdif[latdif>0])
            Dlon=np.min(londif[londif>0])
            self.DeltaLat=Dlat
            self.DeltaLon=Dlon
            self.minLat=min(lat)
            self.minLon=min(lon)
            self.maxLat=max(lat)
            self.maxLon=max(lon)
            self.lenLat=(self.maxLat-self.minLat)
            self.lenLon=(self.maxLon-self.minLon)
            self.nrow=round(self.lenLat/Dlat+1)
            self.ncol=round(self.lenLon/Dlon+1)
            self.transform = from_origin( self.maxLon+Dlon/2,self.maxLat+Dlat/2, Dlon,Dlat)
            self.raster_file= rasterio.open(rfile, 'w+', driver='GTiff',height = self.nrow, width = self.ncol, count=1, dtype='float64',crs=CRS.from_epsg(crs),transform=self.transform)
            self.raster=self.raster_file.read(1)
            i,j=rasterio.transform.rowcol(self.raster_file.transform,xs=lon,ys=lat)
            self.i=i
            self.j=j
            self.raster[self.i,self.j]=feature
            self.raster_file.write(self.raster, 1)
        elif(nrow!=0 and ncol!=0):
            latdif=0.01
            londif=0.01
            Dlat=0.01
            Dlon=0.01
            self.DeltaLat=Dlat
            self.DeltaLon=Dlon
            self.minLat=23
            self.minLon=-103
            self.maxLat=23+Dlat*nrow
            self.maxLon=-103+Dlon*ncol
            self.lenLat=(self.maxLat-self.minLat)
            self.lenLon=(self.maxLon-self.minLon)
            self.nrow=round(self.lenLat/Dlat+1)
            self.ncol=round(self.lenLon/Dlon+1)
            self.transform = from_origin( self.maxLon+Dlon/2,self.maxLat+Dlat/2, Dlon,Dlat)
            self.raster_file= rasterio.open(rfile, 'w+', driver='GTiff',height = self.nrow, width = self.ncol, count=1, dtype='float64',crs=CRS.from_epsg(crs),transform=self.transform)
            self.raster=self.raster_file.read(1)
            # i,j=rasterio.transform.rowcol(self.raster_file.transform,xs=lon,ys=lat)   
            self.i=np.indices((nrow,ncol))[0]
            self.j=np.indices((nrow,ncol))[1]
            self.raster[self.i,self.j]=feature
            self.raster_file.write(self.raster, 1)            
 
    def __del__(self):
        self.raster_file.close() 
    pass
