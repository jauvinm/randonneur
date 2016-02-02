# -*- coding: utf-8 -*-
"""
Created on Tue Feb 02 11:01:27 2016

@author: jauvinm
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.colors import LightSource

def lire_header(path):
  f = open(path)
  lines = f.readlines()
  f.close()
  out = {}
  for line in lines :
    if "=" in line:
      key = line.split("=")[0].split()[0]
      if key in ["lines", "samples"]:
        out[key] = int( line.split("=")[1])
     
  return out
  
def read_data(path):
  f=open(path, "rb")
  #data = f.read()
  out= np.fromfile(f,dtype=np.float32)
  f.close()
  #out=struct.unpack(data, "<")
  return out
  
  

header_path = "images/BossonsDEM_ll8m.hdr"
header = lire_header(header_path)

data_path ="images/BossonsDEM_ll8m"
data = read_data(data_path)

dx= 1.03112519e1 #taille du pixel en x
dy= 7.19750606e0

nx= header["samples"]
ny= header["lines"]
x= np.arange(nx)*dx
y= (ny - np.arange(ny))*dy
X, Y = np.meshgrid(x,y)
Z=data.reshape(ny, nx)




fig = plt.figure(0)
plt.clf()
ax= fig.add_subplot(1,1,1)
ax.set_aspect("equal")
grad=plt.contourf(X,Y,Z, 100, cmap = matplotlib.cm.terrain)
cbar= plt.colorbar()
cbar.set_label("Altutide, $z$ [m]")
plt.grid()
plt.xlabel("Position, $x$ [m]")
plt.ylabel("Position, $y$ [m]")

ls=LightSource(azdeg=0, altdeg=65)
rgb = ls.shade(Z,plt.cm.terrain)
plt.figure(1)
plt.imshow(rgb, extent=[0,x.max(),0,y.max()],aspect=1, alpha= .5)
cbar=plt.colorbar(grad)
cbar.set_label("Altutide, $z$ [m]")
plt.xlabel("Position, $x$ [m]")
plt.ylabel("Position, $y$ [m]")
plt.contour(X,Y,Z, 10, colors = "k")

plt.show()
