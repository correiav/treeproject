# Import Libraries
import pandas as pd 
import folium 

fingal_map = folium.Map(location=[53.45909, -6.21942],
zoom_start=11)

fingal_map.save('output/fingal_trees.html')

# Reading data from 'trees.xz' file
trees = pd.read_csv('data/trees.xz')
#print(trees.shape)
#print(trees.head())

# Plotting few trees in the map
few_trees_fingal = fingal_map

tree1 = trees.iloc[0]
folium.Marker(
    location=[tree1['lat'], tree1['long']],
).add_to(few_trees_fingal)

tree2 = trees.iloc[1]
folium.Marker(
    location=[tree2['lat'], tree2['long']],
).add_to(few_trees_fingal)

few_trees_fingal.save('output/few_trees_fingal.html')
 

'''
# Plotting all trees in the map - It can take a long time and crash your computer.
fingal_all_trees = fingal_map

for _, tree in trees.iterrows():
     folium.Marker(
        location=[trees['lat'], trees['long']],
    ).add_to(fingal_all_trees)

fingal_all_trees.save('output/fingal_all_trees.html')
'''

# Plotting only trees from one town 
trees_blanch = trees[trees['town']  == 'Blanchardstown'] 
trees.shape, trees_blanch.shape

blanchardstown= folium.Map(
    location=[53.393095, -6.389936],
    zoom_start=14,
    control_scale=True
)
blanchardstown.add_child(folium.LayerControl(position='topleft', collapsed=True))
for _, tree in trees_blanch.iterrows():
    folium.Marker(
        location=[tree['lat'], tree['long']],
    ).add_to(blanchardstown)

blanchardstown.save('output/blanchardstown.html') 











