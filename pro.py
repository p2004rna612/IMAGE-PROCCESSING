import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread(r'c:\Users\SAHYADRI\Downloads\panda.jpg')  
newimg = np.asarray(img)
X, Y, D = newimg.shape
div1 = X // 2
div2 = Y // 2
top_left = newimg[:div1, :div2]
top_right = newimg[:div1, div2:]
bottom_left = newimg[div1:, :div2]
bottom_right = newimg[div1:, div2:]
fig, axs = plt.subplots(2, 2, figsize=(8, 8))
axs[0, 0].imshow(cv2.cvtColor(top_left, cv2.COLOR_BGR2RGB), aspect='auto')
axs[0, 0].set_title('Top Left')
axs[0, 1].imshow(cv2.cvtColor(top_right, cv2.COLOR_BGR2RGB), aspect='auto')
axs[0, 1].set_title('Top Right')
axs[1, 0].imshow(cv2.cvtColor(bottom_left, cv2.COLOR_BGR2RGB), aspect='auto')
axs[1, 0].set_title('Bottom Left')
axs[1, 1].imshow(cv2.cvtColor(bottom_right, cv2.COLOR_BGR2RGB), aspect='auto')
axs[1, 1].set_title('Bottom Right')
for ax in axs.flat:
    ax.axis('on') 

plt.tight_layout()
plt.subplots_adjust(wspace=0.11,hspace=0.3,bottom=0.1)
plt.show()
