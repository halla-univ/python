import cv2		# (1)
 
img1 = cv2.imread('dog.jpg', cv2.IMREAD_COLOR)		# (2)
img2 = cv2.stylization(img1, sigma_s=100, sigma_r=0.9) # (3) 

cv2.imshow('original', img1)				# (4)
cv2.imshow('result', img2)  				# (5)
cv2.waitKey(0)  					# (6)
cv2.destroyAllWindows() 				# (7)

cv2.imwrite('result.jpg', img2)			# (8)
