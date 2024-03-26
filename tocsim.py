#!/usr/bin/env python3

#Converting pandas data frame to raster
#TOC= Total Operating Characteristic Curve
#Author: S. Ivvan Valdez 
#Centro de Investigación en Ciencias de Información Geoespacial AC
#Querétaro, México.
#29 de ferebreo de 2024

import tocdata as dtoc
import ootoc as otoc

class TOCsim:
    """
    
    This class implements operations for simulating changes in the land cover using the Total Operating Characteristics, nevertheless it could serve as a wrapper for computing a TOC and structuring data
    
    :param rank: The class is instantiated with the optional parameter ``rank`` that is a numpy array of a predicting feature.
    
    :param groundtruth: The class is instantiated with the optional parameter ``groundtruth`` that is a numpy array of binary labels (0,1). 
    
    :param T: The could be instantiated using an ootoc object T
        
    :return: The class instance, if ``rank`` and ``grountruth`` are given it computes the TOC.
    
    :rtype: ``TOCsim``
    
    """   
    TOC T
    
    
    def __init__(self,T=None, rank=np.array([]), groundtruth=np.array([]),sortw=1.0):
    """
    
    """
    
        if (len(rank)!=0 and len(groundtruth)!=0 and len(rank)==len(groundtruth)):
            T=otoc.TOC(rank,groundtruth,sortw)
        
    
    
    pass



