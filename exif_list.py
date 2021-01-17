from PIL import Image
import PIL.ExifTags as ExifTags

# 画像ファイルを取り込む
img = Image.open('secondlife_002.jpg')
# Exif情報を得る
exif = img._getexif()
# Exif情報を列挙する
for id, value in exif.items():
    tag =ExifTags.TAGS[id]
    print(tag + ":", value)
