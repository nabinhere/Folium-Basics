import folium
import math

map = folium.Map(location=[27.620759026376376, 85.53959291408165], zoom_start=10)

# add separate layers for rectangles, lines, and polygon
line_layer = folium.FeatureGroup(name="Line Layer").add_to(map)

# 1. Changunarayan 27.707477059545106, 85.43344618205137
# 2. Lamatar 27.62480469939209, 85.40183519246898
# 3. Chhatre Deurali (27.755926028638324, 85.2247010628135)
# 4. Hetauda = (27.45688823041509, 84.99138460821779)

# 1. Changunarayan
folium.PolyLine([(27.658844605753657, 85.324270818879340), 
                 (27.707477059545106, 85.43344618205137),
                ],
                 color='red',
                 weight=4.0).add_to(line_layer)

# 2. Lamatar
# folium.PolyLine([(27.658844605753657, 85.324270818879340), 
#                  (27.62480469939209, 85.40183519246898),
#                 ],
#                  color='red',
#                  weight=4.0).add_to(line_layer)

# 3. Chhatre Deurali
# folium.PolyLine([(27.658844605753657, 85.324270818879340), 
#                  (27.755926028638324, 85.2247010628135),
#                 ],
#                  color='red',
#                  weight=4.0).add_to(line_layer)


# 4. Hetauda
# folium.PolyLine([(27.658844605753657, 85.324270818879340), 
#                  (27.45688823041509, 84.99138460821779),
#                 ],
#                  color='red',
#                  weight=4.0).add_to(line_layer)


x1, y1 = 27.658844605753657, 85.324270818879340

# 1. Changunarayan
x2, y2 = 27.707477059545106, 85.43344618205137

# 2. Lamatar
# x2, y2 = 27.62480469939209, 85.40183519246898

# 3. Chhatre Deurali
# x2, y2 = 27.755926028638324, 85.2247010628135

# 4. Hetauda
# x2, y2 = 27.45688823041509, 84.99138460821779


x3, y3 = (x1+x2)/2, (y1+y2)/2
m = (x2-x1)/(y2-y1)
l = math.sqrt(pow(x2-x1, 2) + pow(y2-y1, 2))
# print(f'{line_name}: slope = {m}')
theta = math.atan(m)
theta = abs(theta)
phi = math.pi/10
p = l*math.sin(theta)/5
b = l*math.sin(theta)/5
p1=l*math.tan(phi)/5
b1=p1*math.cos(theta)
k1=b1*math.tan(theta)
p2 = p1
b2 = b1
k2 = k1
if (x1<x2) and (y1<y2):
    print("condition 1")
    yprime=y3-b
    xprime=x3-p
    y4=yprime-k1
    x4=xprime+b1
    y5=yprime+k2
    x5=xprime-b2

elif (x1>x2) and (y1<y2):
    print("condition 2")
    yprime=y3-b
    xprime=x3+p
    y4=yprime+k1
    x4=xprime+b1
    y5=yprime-k2
    x5=xprime-b2

elif (x1<x2) and (y1>y2):
    print("condition 3")
    yprime=y3+b
    xprime=x3-p
    y4=yprime-k1
    x4=xprime-b1
    y5=yprime+k2
    x5=xprime+b2

elif (x1>x2) and (y1>y2):
    print("condition 4")
    yprime=y3+b
    xprime=x3+p
    y4=yprime+k1
    x4=xprime-b1
    y5=yprime-k2
    x5=xprime+b2

# add lines to the line layer
folium.PolyLine([(x4, y4), (x3, y3), (x5, y5)],
                 color='red',
                 weight=4.0).add_to(line_layer)

# # add a polygon the the polygon layer
# folium.Polygon([(x4, y4), (x3, y3), (x5, y5)],
#                  color='red', weight=4.0,
#               fill=True, fill_color='red', fill_opacity=0.8).add_to(line_layer)

# add layer control to the map
folium.LayerControl().add_to(map)
map.save('line_test_py.html')