import cv2
import os
cap=cv2.VideoCapture(0)
ret,photo = cap.read()
model = cv2.CascadeClassifier("/root/Downloads/haarcascade_frontalface_alt.xml")
os.system("tput setaf 3")
while True:
	os.system("tput setaf 3")
	print("""
Enter your choice
1.draw a line using mouse on photo     8.draw a rectangle on face in livevideo
2.draw a circle on photo               9.crop face of two photos and join them
3.draw a rectangle on photo            10.crop face of a photo
4.draw a rectangle on a dynamic image  11.blur the face in livevideo
5.start a live video                   12.Crop on run time
6.show only face in a livevideo        13.To have a side window in the photo
7.show only blur face in a livevideo   14.For main menu
	""")
	os.system("tput setaf 7")
	print('Note: Press "ENTER" to exit from the window')
	ch =int(input("Enter your choice: "))
	if ch == 1:
		    def cir(a,b,c,d,e):
		        if a==cv2.EVENT_MOUSEMOVE:
		            print("hii")
		            cv2.circle(photo,(b,c),5,[0,255,0],-1)
		    cv2.namedWindow("hii")
		    cv2.setMouseCallback("hii",cir)
		    while True:
		        cv2.imshow("hii",photo)
		        if cv2.waitKey(100)==13:
		            break
		    cv2.destroyAllWindows()
	elif ch == 2:
		os.system("clear")
		os.system("tput setaf 1")
		print("Press left mouse_button to draw a circle")
		os.system("sleep 3")
		os.system("tput setaf 7")
		def cir(a,b,c,d,e):
			if a == cv2.EVENT_LBUTTONDOWN:
				print("hii")
				cv2.circle(photo,(b,c),50,[0,255,0],5)
		cv2.namedWindow("hii")
		cv2.setMouseCallback("hii",cir)
		while True:
			cv2.imshow("hii" , photo)
			if cv2.waitKey(1) == 13:
				break
		cv2.destroyAllWindows()
	elif ch == 3:
		os.system("clear")
		os.system("tput setaf 1")
		print("Press left mouse_button to draw a rectangle")
		os.system("sleep 3")
		os.system("tput setaf 7")
		def reci(a,b,c,d,e):
			if a == cv2.EVENT_LBUTTONDOWN:
				print("hii")
				cv2.rectangle(photo,(b,c),(b+150,c+160),[0,255,0],5)
		cv2.namedWindow("hii")
		cv2.setMouseCallback("hii",reci)
		while True:
			cv2.imshow("hii" , photo)
			if cv2.waitKey(1000) == 13:
				break
		cv2.destroyAllWindows()
	elif ch == 4:
		os.system("clear")
		os.system("tput setaf 1")
		print("Press left mouse_button to draw a rectangle")
		os.system("sleep 3")
		os.system("tput setaf 7")
		cv2.namedWindow("hi")
		def rec(a,b,c,d,e):
			ret , photo = cap.read()
			if a == cv2.EVENT_LBUTTONDOWN:
				print("hi")
				new = cv2.rectangle(photo,(b,c),(b+150,c+160),[0,255,0],5)
				cv2.imshow("hi" ,photo)
				cv2.waitKey()
				cv2.destroyAllWindows()
		cv2.setMouseCallback("hi",rec)
		cv2.imshow("hi" , photo)
		cv2.waitKey()
		cv2.destroyAllWindows()
	elif ch == 5:
		while True:
			ret,photo = cap.read()
			cv2.imshow("hello" , photo)
			if cv2.waitKey(10) == 13:  
				    break
		cv2.destroyAllWindows()
	elif ch == 6:
		while True:
			ret,photo = cap.read()
			fdetect = model.detectMultiScale(photo)
			if len(fdetect) == 0:
				print("face not detected")
			else:    
				x1 = fdetect[0][0]
				y1 = fdetect[0][1]
				x2 = fdetect[0][2] + x1
				y2 = fdetect[0][3] + y1
				b = photo[y1:y2,x1:x2]
				cv2.imshow("hi", b)
				if cv2.waitKey(100) == 13:
					break
			cv2.destroyAllWindows()
	elif ch == 7:
		while True:
			ret,photo = cap.read()
			fdetect = model.detectMultiScale(photo)
			if len(fdetect) == 0:
				print("face not detected")
			else:    
				x1 = fdetect[0][0]
				y1 = fdetect[0][1]
				x2 = fdetect[0][2] + x1
				y2 = fdetect[0][3] + y1
				b = photo[y1:y2,x1:x2]
				blur = cv2.blur(b,(15,15))
				cv2.imshow("hi", blur)
				if cv2.waitKey(100) == 13:
					break
			cv2.destroyAllWindows()
	elif ch == 8:
		while True:
			ret,photo = cap.read()
			fdetect = model.detectMultiScale(photo)
			if len(fdetect) == 0:
				print("face not detected")
			else:    
				x1 = fdetect[0][0]
				y1 = fdetect[0][1]
				x2 = fdetect[0][2] + x1
				y2 = fdetect[0][3] + y1
				rec = cv2.rectangle(photo,(x1,y1),(x2,y2),0,5)
				cv2.imshow("hi", rec)
				if cv2.waitKey(100) == 13:
					break
			cv2.destroyAllWindows()
	elif ch == 9:
		i = input("Enter the location of 1st photo: ")
		j = input("Enter the location of 2nd photo: ")
		photo1 = cv2.imread(i)
		fdetect = model.detectMultiScale(photo1)
		if len(fdetect)==0:
			print("no face found")
			
		x1 = fdetect[0][0]
		y1 = fdetect[0][1]
		x2 = fdetect[0][2] + x1
		y2 = fdetect[0][3] + y1
		test1 = photo1[y1:y2,x1:x2]
		photo2 = cv2.imread(j)
		fdetect1 = model.detectMultiScale(photo2)
		if len(fdetect1)==0:
			print( "no face found")

		a1 = fdetect1[0][0]
		b1 = fdetect1[0][1]
		a2 = fdetect1[0][2] + a1
		b2 = fdetect1[0][3] + b1



		test2 = photo2[b1:b2,a1:a2]
		import numpy as np
		t_1 = cv2.resize(test1,(80,80))
		t_2 = cv2.resize(test2,(80,80))

		ch =input("""
		press h for horizontal attachment
		press y for vertical attachment
				     :  """)
		if "h" in ch:
			f_test = np.hstack((t_1,t_2))
			cv2.imshow("hello",f_test)
			cv2.waitKey()
			cv2.destroyAllWindows()
		elif "v" in ch:
			f_test = np.vstack((t_1,t_2))
			cv2.imshow("hello",f_test)
			cv2.waitKey()
			cv2.destroyAllWindows()
		else:
			print("u did not press the correct key")
		save =input('Press "s" to save photo: ')
		if "s" in save:
			cv2.imwrite("concat.png",f_test)
	elif ch == 10:
		x=input("Enter the location of the file:")
		photo1 = cv2.imread(x)
		fdetect = model.detectMultiScale(photo1)
		x1 = fdetect[0][0]
		y1 = fdetect[0][1]
		x2 = fdetect[0][2] + x1
		y2 = fdetect[0][3] + y1
		if len(fdetect) == 0:
			print("face not detected")
		else:
			b = photo1[y1:y2,x1:x2]
			cv2.imshow("hi",b)
			cv2.waitKey()
			cv2.destroyAllWindows()
			cv2.imwrite("crop.png" , b)
	elif ch == 11:
		while True:
			ret,photo = cap.read()
			fdetect = model.detectMultiScale(photo)
			if len(fdetect) == 0:
				print("face not detected")
			else:    
				x1 = fdetect[0][0]
				y1 = fdetect[0][1]
				x2 = fdetect[0][2] + x1
				y2 = fdetect[0][3] + y1
				b = photo[y1:y2,x1:x2]
				blur = cv2.blur(b,(20,20))
				photo[y1:y2,x1:x2] = blur
				cv2.imshow("hi",photo)
				if cv2.waitKey(100) == 13:
					break
		cv2.destroyAllWindows()
	
	elif ch == 12:
		os.system("clear")
		os.system("tput setaf 1")
		print("Press left mouse_button and drag to crop")
		os.system("sleep 3")
		os.system("tput setaf 7")
		ret,photo = cap.read()
		a=[]
		def lw(event,x,y,d,e):
			global a
			while event == 1 or event == 4:
				if event == 1:
				    a.append(x)
				    a.append(y)
				    print(x,y)
				    break
				if event == 4:
				    print(x,y)
				    a.append(x)
				    a.append(y)
				    break
			while event == 4:
				print(a)
				x1 = a[0]
				y1 = a[1]
				x2 = a[2]
				y2 = a[3]
				cv2.rectangle(photo,(x1,y1),(x2,y2),[0,255,0])
				global n_photo
				n_photo = photo[y1:y2,x1:x2]
				break
		cv2.namedWindow("hi")
		cv2.setMouseCallback("hi",lw)
		while True:
			cv2.imshow("hi",photo)
			if cv2.waitKey(1) == 13:
				break
		cv2.destroyAllWindows()
		while True:
			cv2.imshow("hi",n_photo)
			if cv2.waitKey(1) == 13:
				break
		cv2.destroyAllWindows()

	elif ch == 13:
		while True:
			ret,photo = cap.read()
			scale_percent = 30
			width = int(photo.shape[1] * scale_percent /100)
			height = int(photo.shape[0] * scale_percent /100)
			dim = (width,height)
			resize = cv2.resize(photo,dim,interpolation = cv2.INTER_AREA)
			photo[0:height,0:width] = resize
			cv2.imshow("hi",photo)
			if cv2.waitKey(1) == 13:
				break
		cv2.destroyAllWindows()

	elif ch == 14:
		break

	else:
		os.system("clear")
	input("press enter to continue..............")
	os.system("clear")	
