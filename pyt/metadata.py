import cv2
import exifread

class Metadata(object):
 	"""docstring for metadata"""
 	def __init__(self):
 		super(Metadata, self)

 	def exif(self, filename):
 		# Open image file for reading (binary mode)
 		f = open('static/public/images/' + filename, 'rb')
 		# Return Exif tags
 		tags = exifread.process_file(f)
 		exposureTime = tags['EXIF ExposureTime']
 		focalLength = tags['EXIF FocalLength']
 		iso = tags['EXIF ISOSpeedRatings']
 		fStop = tags['EXIF FNumber']
 		makAperture = tags['EXIF MaxApertureValue']
 		ccd = tags['EXIF FocalLengthIn35mmFilm']
 		return exposureTime, focalLength, iso, fStop, makAperture, ccd
		# print("ExposureTime: %s" % (tags['EXIF ExposureTime']))
		# for tag in tags.keys():
		#     if tag not in ('JPEGThumbnail', 'TIFFThumbnail', 'Filename', 'EXIF MakerNote'):
		#         print ("Key: %s, value %s" % (tag, tags[tag]))


