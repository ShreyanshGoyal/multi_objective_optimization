from .utils import gaussian
import numpy as np

def job(s):  
    return (9*(s.acads)**2 + 4*(s.research)**2 + 3*(s.pors)**2 + 5*(s.tech_team)**2 + 5*(s.tech_club)**2) * gaussian(s.sleep, 49, 14**2)

def gradstudy(s):
    return gaussian(s.sleep, 49, 14**2)*(8*(s.acads)**2+10*(s.research)**2+5*(s.tech_team)**2+5*(s.tech_club)**2)

def health(s): 
    return gaussian(s.sleep, 49, 7**2)*(1 + s.sports**2/5 + (1 - np.exp(-s.leisure/15)))

def social(s):
    return gaussian(s.sleep, 49, 14**2)*((s.sports**2)+7*(s.pors**2)+3*(s.tech_team)**2+3*(s.tech_club)**2+7*(s.nc_club**2)+7*(s.cult**2))

def explore(s):
    return gaussian(s.sleep, 49, 14**2)*(5*(s.sports**2)+5*(s.pors**2)+5*(s.tech_team)**2+5*(s.tech_club)**2+5*(s.nc_club**2)+5*(s.cult**2)+5*(s.acads**2)+5*(s.research**2))
