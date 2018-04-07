import cv2
import exifread

class metadata(object):
 	"""docstring for metadata"""
 	def __init__(self):
 		super(metadata, self)

 	def exif(self, filename):
 		# Open image file for reading (binary mode)
 		f = open('static/public/images/' + filename, 'rb')
 		# Return Exif tags
 		tags = exifread.process_file(f)
 		exposure = tags['EXIF ExposureTime']
 		return exposure
		# print("ExposureTime: %s" % (tags['EXIF ExposureTime']))
		# for tag in tags.keys():
		#     if tag not in ('JPEGThumbnail', 'TIFFThumbnail', 'Filename', 'EXIF MakerNote'):
		#         print ("Key: %s, value %s" % (tag, tags[tag]))


