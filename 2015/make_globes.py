import cPickle, requests, json, csv, us

import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl

from mpl_toolkits.basemap import Basemap
from matplotlib.colors import rgb2hex
from matplotlib.patches import Polygon
from geopy import geocoders
from pprint import pprint
from random import random

from matplotlib import rcParams

READ = 'rU'
rcParams['text.usetex'] = True
# Lambert Conformal map of lower 48 states.
m = Basemap(llcrnrlon=-119,llcrnrlat=22,urcrnrlon=-64,urcrnrlat=49,
            projection='lcc',lat_1=33,lat_2=45,lon_0=-95)

# draw state boundaries.
shp_info = m.readshapefile('st99_d00','states',drawbounds=True)

with open('prevalence.csv',READ) as f:
    counts = {line[0]:int(line[1]) for line in csv.reader(f)}

denom = sum(counts.values())
colors={}
statenames=[]
cmap = plt.cm.seismic # use 'hot' colormap
vmin = 0; vmax = 1 # set range.
for shapedict in m.states_info:
    statename = us.states.lookup(shapedict['NAME']).abbr
    pop = counts[statename]/float(denom) if statename in counts else 0
#    colors[statename] = cmap((pop-mn)/float(mx-mn))[:3]
    colors[statename] = cmap(pop)[:3]#cmap((pop/float(denom)))[:3]
    statenames.append(statename)

ax = plt.gca() # get current axes instance
ax.patch.set_alpha(0)
for nshape,seg in enumerate(m.states):
    # skip DC and Puerto Rico.
    if statenames[nshape] not in ['District of Columbia','Puerto Rico']:
        color = rgb2hex(colors[statenames[nshape]]) 
        poly = Polygon(seg,facecolor=color,edgecolor=color)
        ax.add_patch(poly)
        ax.annotate(r'\Large \textbf{\textsc{SXSW}}', xy=(.5, .8),  xycoords='figure fraction',
             ha="left", va="bottom")
cbar = plt.gcf().add_axes([0.92, 0.2, 0.03,0.6])
norm = mpl.colors.Normalize(vmin=-2.5,vmax=2.5)
cb1 = mpl.colorbar.ColorbarBase(cbar,cmap=cmap,norm=norm,orientation='vertical')
ax.set_axis_off()
plt.show()