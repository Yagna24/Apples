#!/usr/bin/env python
# coding: utf-8

# In[9]:


import numpy as np
import cv2

img = cv2.imread('C:/Users/Yagna/Desktop/yagnaaa/projects/assignment_apples/red.jpeg')


red = np.array([179, 255, 255])
diff = 20
boundaries = [([red[2]-diff, red[1]-diff, red[0]-diff],
               [red[2]+diff, red[1]+diff, red[0]+diff])]
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)




for (lower, upper) in boundaries:
        lower = np.array([0,50,50])
        upper = np.array([10,255,255])
        mask = cv2.inRange(hsv, lower, upper)
        output = cv2.bitwise_and(img, img, mask=mask)
      
        ratio_red = cv2.countNonZero(mask)/(img.size/3)
        print('red percentage:', np.round(ratio_red*100, 2))
        
        cv2.imshow("images", np.hstack([img, output]))
        cv2.waitKey(0)
        res = cv2.bitwise_and(img,img, mask= mask)
        cv2.imshow('res',res)
        k = cv2.waitKey(5) & 0xFF
        if k == 27:
            break

cv2.destroyAllWindows()


# In[ ]:





# In[ ]:




