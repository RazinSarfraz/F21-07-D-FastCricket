import cv2
overs = 0
balls = 1

class LiveWebCam(object):
	def __init__(self):
		self.url = cv2.VideoCapture("http:/192.168.100.145:8080/video")

	def __del__(self):
		cv2.destroyAllWindows()

	def get_frame(self):
		#output_name = "camera1-" + str(overs) + "-" + str(balls)
		fourcc = cv2.VideoWriter_fourcc(*'XVID')
	#	out_frame = cv2.VideoWriter(f'recordings/{output_name}.avi', fourcc, 20.0, (640, 480))
		_,img = self.url.read()
		resize = cv2.resize(img, (640, 480)) 
		#cv2.imshow('Camera 1', resize)
		#out_frame.write(resize)
		_,jpeg = cv2.imencode('.jpg', resize)
		return jpeg.tobytes()
	# def save_video(self):
	# 	output_name = "camera1-" + str(overs) + "-" + str(balls)
	# 	fourcc = cv2.VideoWriter_fourcc(*'XVID')
	# 	out_frame = cv2.VideoWriter(f'recordings/{output_name}.avi', fourcc, 20.0, (500, 600))
	# 	while True:
	# 		ret, frame = self.url.read()
	# 		if ret:
	# 			b = cv2.resize(frame, (500, 600))
	# 			cv2.imshow('Camera 2', b)
	# 			out_frame.write(b)


class LiveWebCam2(object):
	def __init__(self):
		self.url = cv2.VideoCapture("http:/192.168.100.145:8080/video")

	def __del__(self):
		cv2.destroyAllWindows()

	def get_frame(self):
		success,img = self.url.read()
		resize = cv2.resize(img, (640, 480), interpolation = cv2.INTER_LINEAR) 
		ret,jpeg = cv2.imencode('.jpg', resize)
		return jpeg.tobytes()
	# def save_video(self):
	# 	output_name = "camera2-" + str(overs) + "-" + str(balls)
	# 	fourcc = cv2.VideoWriter_fourcc(*'XVID')
	# 	out_frame = cv2.VideoWriter(f'recordings/{output_name}.avi', fourcc, 20.0, (500, 600))
	# 	while True:
	# 		ret, frame = self.url.read()
	# 		if ret:
	# 			b = cv2.resize(frame, (500, 600))
	# 			cv2.imshow('Camera 2', b)
	# 			out_frame.write(b)
class LiveWebCam3(object):
	def __init__(self):
		self.url = cv2.VideoCapture("http://192.168.100.145:8080/video")

	def __del__(self):
		cv2.destroyAllWindows()

	def get_frame(self):
		success,img = self.url.read()
		resize = cv2.resize(img, (640, 480), interpolation = cv2.INTER_LINEAR) 
		ret,jpeg = cv2.imencode('.jpg', resize)
		return jpeg.tobytes()