import sys
import folium
import pandas

data=pandas.read_csv("volcano.txt",delimiter="\t")
#data=list(pandas.read_csv("volcano.csv"))

lat=list(data["LAT"])
lon=list(data["LON"])
elev=list(data["ELEV"])
name=list(data["NAME"])
def color_producer(elevation):
    if elevation<0:
        return 'orange'
    elif 0<=elevation<1000:
        return 'purple'
    elif 1000<=elevation<=2000:
        return 'blue'
    else:return 'pink'



map=folium.Map(location=[38.58,-99.09],zoom_start=6,tiles="Stamen Terrain")

fgv=folium.FeatureGroup(name="Volcanoes")

for lt,ln,el,na in zip(lat,lon,elev,name):
    
    fgv.add_child(folium.CircleMarker(location=[lt,ln],radius=6,popup=str(na)+":"+str(el)+"m",
    fill_color=color_producer(el),color='grey',fill_opacity=0.7))

fgp=folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data=open('world.json','r',encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005']<10000000 else 'orange' if 1000000 <= x['properties']['POP2005']<50000000 else 'red'}))

map.add_child(fgv)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("Map_html_popup_advanced.html")