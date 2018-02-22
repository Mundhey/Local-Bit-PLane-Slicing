import cv2
import numpy as np


def compare(a,b):
    if a > b:
        return '1'
    else:
        return '0'





img = cv2.imread('brain.jpg',0)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()



height, width= img.shape


new_image=np.zeros([height,width],dtype=np.uint8)

for count in range(1,8):

 if count>1:
  for row in range(1,height-2):
     for column in range(1,width-2):

         img[row,column]=int(img[row,column]/2)


 for i in range(1,height-2):
     for j in range(1,width-2):



        a = img[i, j]
        b = img[i + 1, j + 1]
        c = img[i, j + 1]
        d = img[i - 1, j + 1]
        e = img[i - 1, j]
        f = img[i - 1, j - 1]
        g = img[i, j - 1]
        h = img[i + 1, j - 1]
        z = img[i + 1, j]


        p=(f'{b:08b}')
        q=(f'{c:08b}')
        r=(f'{d:08b}')
        s=(f'{e:08b}')
        t=(f'{f:08b}')
        u=(f'{g:08b}')
        v=(f'{h:08b}')
        w=(f'{z:08b}')


        p1 = p[0] + q[0] + r[0] + s[0] + t[0] + u[0] + v[0] + w[0]
        p2 = p[1] + q[1] + r[1] + s[1] + t[1] + u[1] + v[1] + w[1]
        p3 = p[2] + q[2] + r[2] + s[2] + t[2] + u[2] + v[2] + w[2]
        p4 = p[3] + q[3] + r[3] + s[3] + t[3] + u[3] + v[3] + w[3]
        p5 = p[4] + q[4] + r[4] + s[4] + t[4] + u[4] + v[4] + w[4]
        p6 = p[5] + q[5] + r[5] + s[5] + t[5] + u[5] + v[5] + w[5]
        p7 = p[6] + q[6] + r[6] + s[6] + t[6] + u[6] + v[6] + w[6]
        p8 = p[7] + q[7] + r[7] + s[7] + t[7] + u[7] + v[7] + w[7]


        mm=int(p1,2)
        k=int(p2,2)
        l=int(p3,2)
        m=int(p4,2)
        n=int(p5,2)
        o=int(p6,2)
        x=int(p7,2)
        y=int(p8,2)


        new=compare(mm,a)+compare(k,a)+compare(l,a)+compare(m,a)+compare(n,a)+compare(o,a)+compare(x,a)+compare(y,a)
        pixel=int(new,2)

        new_image[i,j]=pixel

 cv2.imshow('new_image', img)
 cv2.waitKey(0)
 cv2.destroyAllWindows()




