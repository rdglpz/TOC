#!/usr/bin/env python3

#Test for the computation of the
#TOC= Total Operating Charcateristic Curve
#Author:S. Ivvan Valdez 
#Centro de Investigación en Ciencias de Información Geoespacial AC
#Querétaro, México.


# if __name__ == '__main__':
import ootoc as otoc
import pandas as pd
import numpy as np
import tocdata 
import importlib
import matplotlib.pyplot as plt
#Loading training data,  
dataY=pd.read_csv('data/Morelia_train_Y.csv')
dataX=pd.read_csv('data/Morelia_train_X.csv')

#Selecting a feature and class labels
feature=dataX.dist_carreteras.to_numpy()
label=dataY.incremento_urbano.to_numpy()

####################################################################
##--Fisrt part, TOC and probability density function computation--##
#Continuous case
#Computes the TOC, notice the minus sign because the predictor is the inverse of the distance. T.plot() shows the TOC
importlib.reload(otoc)
T=otoc.TOC(rank=-feature,groundtruth=label)
T.plot(filename='TOC.png')
#Plotting versus the thresholds
T.plot(kind="tTOC",filename='TPvsThresholds.png')
#Representation by vectors
V=T.vector(nmeans=200)
V.plot(title='Plotting the vector representation of a TOC',filename='TOCVector.png')
V.plot(kind='tVector',title='TP versus Thresholds',filename='VectorvsThresholds.png')
#Computes the density probability function
D=V.density()
#Shows the smoothed version of the density with differentiated quartiles
D.plot(kind="Smoothed",title="Distance to roads vs ULC, smooth probability density",filename='Density.png')
D.plot(kind="tSmoothed", title='Probabilty Dist2Roads versus Thresholds',filename='tDensity.png')




#########################################################################
##--Second part, assing the probability to the corresponding location--##
#Assigns the corresponding probability to each rank value
prob=D.rank2prob(rank=-feature)
#Loading lat and lon, the data set has interchanged names
lat=dataX.lon.to_numpy()  
lon=dataX.lat.to_numpy()  
#Computes a raster from points and assigns the probability
rasterTOC=tocdata.TOCData(feature=prob,lat=lat,lon=lon,crs=32641)
#Plotting the raster with the probabilities
plot=plt.imshow(rasterTOC.raster, cmap='RdBu')
plt.colorbar()
plt.minorticks_on()
plt.show()



####################################################################
importlib.reload(otoc)
##--Second part, TOC and probability density function computation--##
feature=dataX.pendiente.to_numpy()
#Computes the TOC, notice the minus sign because the predictor is the inverse of the distance. T.plot() shows the TOC
T=otoc.TOC(rank=-feature,groundtruth=label)
#Computes the TOC, notice the minus sign because the predictor is the inverse of the distance. T.plot() shows the TOC
T.plot(filename='DiscontinuousTOC.png')
T.plot(kind="tTOC",filename='DiscontinuousTPvsThresholds.png')
V=T.vector()
V.plot(filename='DiscontinuousTOCVector.png')
V.plot(kind='tVector',filename='DiscontinuousVectorvsThresholds.png')
D=V.density()
D.plot(filename='Histogram.png')
D.plot(kind='tHistogram',filename='tHistogram.png')


#########################################################################
##--Second part, assing the probability to the corresponding location--##
prob=D.rank2prob(rank=-feature)
#Loading lat and lon, the data set has interchanged names
lat=dataX.lon.to_numpy()  
lon=dataX.lat.to_numpy()  
#Computes a raster from points and assigns the probability
rasterTOC=tocdata.TOCData(feature=prob,lat=lat,lon=lon,crs=32641)

#Plotting the raster with the probabilities
plot=plt.imshow(rasterTOC.raster, cmap='RdBu')
plt.colorbar()
plt.minorticks_on()
plt.show()


