from unicodedata import name
import folium
from folium import plugins
import os
import json

# Create map object
m = folium.Map(location=[19.021378410670604,73.01832318305968], zoom_start=20)

mapOutline = os.path.join('Map Files', 'malloutline.geojson')

fgm = folium.FeatureGroup(Name="My Map")
#fga = folium.FeatureGroup(Name="Layout")

fgm.add_child(folium.GeoJson(mapOutline, name='SGC'))


# Creating Store Markers
fgm.add_child(folium.Marker([19.022648817789207,73.01741391420364],
              popup='<strong>Store One</strong>', icon=folium.Icon(color='green')))

fgm.add_child(folium.Marker([19.022179706511068,73.01795303821564],
              popup='<strong>Store Two</strong>',icon=folium.Icon(color='green')))

fgm.add_child(folium.Marker([19.021860202936526,73.01831245422363],
              popup='<strong>Store Three</strong>',icon=folium.Icon(color='green')))

fgm.add_child(folium.Marker([19.0213302313672,73.01884889602661],
              popup='<strong>Store Four</strong>',icon=folium.Icon(color='green')))

fgm.add_child(folium.Marker([19.020949867955153,73.01929146051407],
              popup='<strong>Store Five</strong>',icon=folium.Icon(color='green')))

fgm.add_child(folium.Marker([19.022344529543467,73.01695257425307],
              popup='<strong>Store Six</strong>',icon=folium.Icon(color='green')))

fgm.add_child(folium.Marker([19.022050383709637,73.01729053258896],
              popup='<strong>Store Seven</strong>',icon=folium.Icon(color='green')))

fgm.add_child(folium.Marker([19.02169791517136,73.01767140626907],
              popup='<strong>Store Eight</strong>',icon=folium.Icon(color='green')))

fgm.add_child(folium.Marker([19.021216122434982,73.01824808120728],
              popup='<strong>Store Nine</strong>',icon=folium.Icon(color='green')))
fgm.add_child(folium.Marker([19.020561896378098,73.01890254020691],
              popup='<strong>Store Ten</strong>',icon=folium.Icon(color='green')))


# Creating Store Borders
store1 = os.path.join('Map Files', 'store1.geojson')
store2 = os.path.join('Map Files', 'store2.geojson')
store3 = os.path.join('Map Files', 'store3.geojson')
store4 = os.path.join('Map Files', 'store4.geojson')
store5 = os.path.join('Map Files', 'store5.geojson')
store6 = os.path.join('Map Files', 'store6.geojson')
store7 = os.path.join('Map Files', 'store7.geojson')
store8 = os.path.join('Map Files', 'store8.geojson')
store9 = os.path.join('Map Files', 'store9.geojson')
store10 = os.path.join('Map Files', 'store10.geojson')

fgm.add_child(folium.GeoJson(store1, name="store1"))
fgm.add_child(folium.GeoJson(store2, name="store2"))
fgm.add_child(folium.GeoJson(store3, name="store3"))
fgm.add_child(folium.GeoJson(store4, name="store4"))
fgm.add_child(folium.GeoJson(store5, name="store5"))
fgm.add_child(folium.GeoJson(store6, name="store6"))
fgm.add_child(folium.GeoJson(store7, name="store7"))
fgm.add_child(folium.GeoJson(store8, name="store8"))
fgm.add_child(folium.GeoJson(store9, name="store9"))
fgm.add_child(folium.GeoJson(store10, name="store10"))


# Creating AntPaths

#Gate to Store1
fgr1 = folium.FeatureGroup(name="Gate to Store1")
fgr1.add_child(folium.plugins.AntPath([[19.021786666312583, 73.0186316370964],
                [19.02152548424725, 73.01837682723999],
                [19.022549924170445, 73.01721811294556]]))

#Gate to Store2
fgr2 = folium.FeatureGroup(name="Gate to Store2")
fgr2.add_child(folium.plugins.AntPath([[19.021753701608517, 73.01864236593246],
                [19.021510269745352, 73.018379509449],
                [19.02200981182964, 73.01781088113785]]))

#Gate to Store3
fgr3 = folium.FeatureGroup(name="Gate to Store3")
fgr3.add_child(folium.plugins.AntPath([[19.021743558621335, 73.01864504814147],
                [19.021545770247613, 73.01838755607605],
                [19.0217156654034, 73.01818907260895]]))

#Gate to Store4
fgr4 = folium.FeatureGroup(name="Gate to Store4")
fgr4.add_child(folium.plugins.AntPath([[19.0217156654034, 73.01867455244064],
                [19.021500126743327, 73.01841706037521],
                [19.02124401573677, 73.01871478557587]]))

#Gate to Store5
fgr5 = folium.FeatureGroup(name="Gate to Store5")
fgr5.add_child(folium.plugins.AntPath([[19.021751165861783, 73.01864236593246],
                [19.021530555747574, 73.01837682723999],
                [19.02081547267478, 73.01914393901825]]))

#Gate to Store6
fgr6 = folium.FeatureGroup(name="Gate to Store6")
fgr6.add_child(folium.plugins.AntPath([[19.021781594820066, 73.01862895488739],
                [19.021497590992723, 73.01835000514984],
                [19.022400315763548, 73.01736027002335],
                [19.02220506391129, 73.01714837551117]]))

#Gate to Store7
fgr7 = folium.FeatureGroup(name="Gate to Store7")
fgr7.add_child(folium.plugins.AntPath([[19.021741022874448, 73.01865309476852],
                [19.021441804469603, 73.01836878061295],
                [19.02207574112962, 73.0176231265068],
                [19.021898239108566, 73.01741659641264]]))

#Gate to Store8
fgr8 = folium.FeatureGroup(name="Gate to Store8")
fgr8.add_child(folium.plugins.AntPath([[19.021741022874448, 73.01866918802261],
                [19.021500126743327, 73.01835536956787],
                [19.02177398758102, 73.01802814006805],
                [19.021621842726905, 73.01780819892883]]))

#Gate to Store9
fgr9 = folium.FeatureGroup(name="Gate to Store9")
fgr9.add_child(folium.plugins.AntPath([[19.021753701608517, 73.01864236593246],
                [19.021451947475203, 73.01832586526871]]))

#Gate to Store10
fgr10 = folium.FeatureGroup(name="Gate to Store10")
fgr10.add_child(folium.plugins.AntPath([[19.021763844595075, 73.01863431930542],
                [19.02147730498648, 73.01835268735886],
                [19.021043691011002, 73.01885157823563],
                [19.020807865391497, 73.01865845918655]]))

#Store1 to Gate
fgr11 = folium.FeatureGroup(name="Store1 to Gate ")
fgr11.add_child(folium.plugins.AntPath([[19.022544852701234, 73.01722884178162],
                [19.021530555747574, 73.01837682723999],
                [19.021766380341617, 73.0186316370964]]))

#Store2 to Gate
fgr12 = folium.FeatureGroup(name="Store2 to Gate")
fgr12.add_child(folium.plugins.AntPath([[19.022052919451816, 73.01777601242065],
                [19.021535627247736, 73.01837682723999],
                [19.021761308848493, 73.01863968372345]]))

#Store3 to Gate
fgr13 = folium.FeatureGroup(name="Store3 to Gate")
fgr13.add_child(folium.plugins.AntPath([[19.02172327264512, 73.01819443702698],
                [19.02152548424725, 73.01840901374817],
                [19.021738487127525, 73.01866382360458]]))

#Store4 to Gate
fgr14 = folium.FeatureGroup(name="Store4 to Gate")
fgr14.add_child(folium.plugins.AntPath([[19.021193300639144, 73.0187577009201],
                [19.02148744798991, 73.0184143781662],
                [19.021720736897926, 73.01867187023163]]))

#Store5 to Gate
fgr15 = folium.FeatureGroup(name="Store5 to Gate")
fgr15.add_child(folium.plugins.AntPath([[19.02081547267478, 73.01914662122726],
                [19.021500126743327, 73.01842510700226],
                [19.02169791517136, 73.01867455244064]]))

#Store6 to Gate
fgr16 = folium.FeatureGroup(name="Store6 to Gate")
fgr16.add_child(folium.plugins.AntPath([[19.022199992431563, 73.01713764667511],
                [19.022357208231494, 73.01731199026108],
                [19.02147730498648, 73.01827490329742],
                [19.021781594820066, 73.01859140396118]]))

#Store7 to Gate
fgr17 = folium.FeatureGroup(name="Store7 to Gate")
fgr17.add_child(folium.plugins.AntPath([[19.02189316761946, 73.01739513874054],
                [19.022073205387795, 73.01763117313385],
                [19.021459554728995, 73.01831781864166],
                [19.021753701608517, 73.01862359046936]]))

#Store8 to Gate
fgr18 = folium.FeatureGroup(name="Store8 to Gate")
fgr18.add_child(folium.plugins.AntPath([[19.02161423548054, 73.01779747009277],
                [19.02180188078916, 73.01799863576889],
                [19.021467161982432, 73.01840096712112],
                [19.021705522413903, 73.01866918802261]]))

#Store9 to Gate
fgr19 = folium.FeatureGroup(name="Store9 to Gate")
fgr19.add_child(folium.plugins.AntPath([[19.021416446952905, 73.01836609840393],
                [19.02170045091892, 73.01869869232178]]))

#Store10 to Gate
fgr20 = folium.FeatureGroup(name="Store10 to Gate")
fgr20.add_child(folium.plugins.AntPath([[19.020785043539604, 73.01866114139557],
                [19.02098790433553, 73.01887571811676],
                [19.021469697733504, 73.01835268735886],
                [19.021725808392286, 73.01865577697754]]))


m.add_child(fgr1)
m.add_child(fgr2)
m.add_child(fgr3)
m.add_child(fgr4)
m.add_child(fgr5)
m.add_child(fgr6)
m.add_child(fgr7)
m.add_child(fgr8)
m.add_child(fgr9)
m.add_child(fgr10)
m.add_child(fgr11)
m.add_child(fgr12)
m.add_child(fgr13)
m.add_child(fgr14)
m.add_child(fgr15)
m.add_child(fgr16)
m.add_child(fgr17)
m.add_child(fgr18)
m.add_child(fgr19)
m.add_child(fgr20)

#m.add_child(fga)

m.add_child(fgm)
#m.add_child(folium.LayerControl())
m.add_child(folium.LayerControl())
#folium.LayerControl().add_child(m)

#Generate HTML Page
m.save('map.html')
