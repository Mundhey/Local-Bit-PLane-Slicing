import cv2
import numpy as np
from matplotlib import pyplot as plt

def get_pixel(img, center, x):
    new_value = 0
    try:
        if x >= center:
            new_value = 1
    except:
        pass
    return new_value

def lbp_pixel(img, x, y):
    # digits = [ int(char) for char in str(num) ]  
    c = img[x][y]
    img2=[]
    neighbours=[]
    
    d=[[0 for x in range(8)] for y in range(8)]
    power_val = [1, 2, 4, 8, 16, 32, 64, 128]
    neighbours.append([img[x-1][y+1],img[x][y+1],img[x+1][y+1],img[x+1][y],img[x+1][y-1],img[x][y-1],img[x-1][y-1],img[x-1][y]])
    for i in range(8):
       digits=[]
       digits.append([int(char) for char in "{0:08b}".format(neighbours[i])])
       d[i].append(digits)
    for i in range(8):
       val = 0
       for j in range(8):
         val+=d[i][j] * power_val[j]
       img2.append(val)
       print (val)
       
                                                                                                                                                                                    

    val_ar = []
    val_ar.append(get_pixel(img, c, img2[7]))    
    val_ar.append(get_pixel(img, c, img2[6]))       
    val_ar.append(get_pixel(img, c,img2[5] ))    
    val_ar.append(get_pixel(img, c, img2[4]))      
    val_ar.append(get_pixel(img, c, img2[3]))     
    val_ar.append(get_pixel(img, c, img2[2]))       
    val_ar.append(get_pixel(img, c, img2[1]))    
    val_ar.append(get_pixel(img, c,img2[0]))      
    
    
    val = 0
    for i in range(len(val_ar)):
        val += val_ar[i] * power_val[i]
    return val    



image = 'brain.jpg'
img_bgr = cv2.imread(image)

height, width ,channel= img_bgr.shape
img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
    
img_lbp = np.zeros((height, width), np.uint8)
for i in range(0, height):
 for j in range(0, width):
  img_lbp[i, j] = lbp_pixel(img_gray, i, j)
   
plt.subplot(1,2,1)
plt.title('gray  image')
plt.imshow(img_gray, cmap = plt.get_cmap('gray'))

plt.subplot(1,2,2)
plt.title('LBP Image')
plt.imshow(img_lbp)
    
plt.tight_layout()

plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
print("LBP Program is finished")

