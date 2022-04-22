from django.shortcuts import render
from django.http.response import StreamingHttpResponse
from control.camera import LiveWebCam ,LiveWebCam2 ,LiveWebCam3



contentType='multipart/x-mixed-replace; boundary=frame'
def index(request):
	return render(request, 'control/home.html')


def gen(camera):
	while True:
		frame = camera.get_frame()
		yield (b'--frame\r\n'
		b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')



def gen2(camera):	
	while True:
		frame = camera.get_frame()
		yield (b'--frame\r\n'
		b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


def gen3(camera):	
	while True:
		frame = camera.get_frame()
		yield (b'--frame\r\n'
		b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')




	
def livecam_feed(request):
	return StreamingHttpResponse(gen(LiveWebCam()),content_type=contentType)

def livecam_feed2(request):
	return StreamingHttpResponse(gen2(LiveWebCam2()),content_type=contentType)

def livecam_feed3(request):
	return StreamingHttpResponse(gen3(LiveWebCam3()),content_type=contentType)