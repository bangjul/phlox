import exifread
# Open image file for reading (binary mode)
f = open('40.jpg', 'rb')

# Return Exif tags
tags = exifread.process_file(f)
ex = tags['EXIF ExposureTime']
print (ex)
# print("ExposureTime: %s" % (tags['EXIF ExposureTime']))
# for tag in tags.keys():
#     if tag not in ('JPEGThumbnail', 'TIFFThumbnail', 'Filename', 'EXIF MakerNote'):
#         print ("Key: %s, value %s" % (tag, tags[tag]))