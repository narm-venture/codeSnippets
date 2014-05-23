from imgproc import *
import picamera
from time import sleep

camera=picamera.PiCamera()
my_camera=Camera(320,240)

#open a view setting the view to the size of the captured image
my_view=Viewer(my_image.width,my_image.height,"Basic Image Processing")
white=(255,255,255)
x_pix=0,y_pix=0,pix=0
while True:
	my_image=my_camera.grabImage()

	for i in range(my_image.height):
		for j in range(my_image.width):
			red,green,blue=my_image[i][j]
			if red>green and red>blue:
				x_pix+=i
				y_pix+=j
				#my_image[i][j]=0,0,0
			pix+=1
	#display the image on screen
	mean_x=x_pix/pix
	mean_y=y_pix/pix
	my_image[mean_x][mean_y-1]=white
	my_image[mean_x-1][mean_y]=white
	my_image[mean_x][mean_y+1]=white
	my_image[mean_x+1][mean_y]=white
	my_image[mean_x][mean_y]=white
	my_view.displayImage(my_image)

