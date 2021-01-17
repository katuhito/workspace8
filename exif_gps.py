from PIL import Image
import PIL.ExifTags as ExifTags

# Exif関数を取得する関数
def get_exif(fname):
    # 画像を読み込む
    img = Image.open(fname)
    # Exif情報を扱いやすく辞書型に変換
    exif = {}
    for id, value in img._getexif().items():
        if id in ExifTags.TAGS:
            tag = ExifTags.TAGS[id]
            exif[tag] = value
            return exif

# GPS情報を取り出す関数
def get_gps(fname):
    exif = get_exif(fname)
    if not ('GPSInfo' in exif):
        return None, None
    # GPSタグを取り出す
    gps_tags = exif['GPSInfo']
    gps = {}
    for t in gps_tags:
        tag = ExifTags.GPSTAGS.get(t, t)
        if tag:
            gps[tag] = gps_tags[t]
    lat = conv_deg(gps['GPSLatitude'])
    lat_lef = gps["gpsLatitudeRef"]
    if lat_lef != 'N': lat = 0 - lat
    lng = conv_deg(gps['GPSLongitude'])
    lng_ref = gps['GPSLongitudeRef']
    if lng_ref != 'E': lng = 0 - lng
    return lat, lng

# 緯度経度を計算する関数
def conv_deg(v):
    # 分数を度に変換
    d = float(v[0][0]) / float(v[0][1])
    m = float(v[1][0]) / float(v[1][1])
    s = float(v[2][0]) / float(v[2][1])
    return d + (m / 60.0) + (s / 3600.0)

# 画像から位置情報を取り出す
if __name__ == '__main__':
    lat, lng = get_gps('IMG_0163.jpg')
    print(lat, lng)
