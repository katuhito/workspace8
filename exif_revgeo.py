import exif_gps
import geocoder

# 写真から位置情報を取得
lat, lng = exif_gps.get_gps('P1010098.JPG')
if lat is None:
    print('位置情報はありません。')
    quit()

# 逆ジオコーティング(OpenStreetMap API を利用)
g = geocorder.osm((lat, lng), method='reverse')
print('写真の住所：')
print(g.address)
