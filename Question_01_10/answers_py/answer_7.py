import cv2
import numpy as np


# average pooling
def average_pooling(img, G=8):
    out = img.copy()

    H, W, C = img.shape
    Nh = int(H / G)
    Nw = int(W / G)

    for y in range(Nh):
        for x in range(Nw):
            for c in range(C):
                index = np.s_[G*y:G*(y+1), G*x:G*(x+1), c]
                print(index)
                out[index] = np.mean(out[index]).astype(np.int)
    
    return out


# Read image
img = cv2.imread("../imori.jpg")

# Average Pooling
out = average_pooling(img)

# Save result
cv2.imwrite("out.jpg", out)
cv2.imshow("result", out)
cv2.waitKey(0)
cv2.destroyAllWindows()
