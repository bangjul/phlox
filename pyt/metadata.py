import cv2
import exifread

class Metadata(object):
 	"""docstring for metadata"""
 	def __init__(self):
 		super(Metadata, self)

 	def exif(self, filename):
 		# Open image file for reading (binary mode)
 		f = open('project/static/public/images/test/' + filename, 'rb')
 		# Return Exif tags
 		tags = exifread.process_file(f)
 		exposureTime = tags['EXIF ExposureTime']
 		focalLength = tags['EXIF FocalLength']
 		ccd = 0.0136
 		# iso = tags['EXIF ISOSpeedRatings']
 		# fStop = tags['EXIF FNumber']
 		# makAperture = tags['EXIF MaxApertureValue']
 		return exposureTime, focalLength, ccd
		# print("ExposureTime: %s" % (tags['EXIF ExposureTime']))
		# for tag in tags.keys():
		#     if tag not in ('JPEGThumbnail', 'TIFFThumbnail', 'Filename', 'EXIF MakerNote'):
		#         print ("Key: %s, value %s" % (tag, tags[tag]))


