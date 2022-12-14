import cv2
import numpy as np
from matplotlib import pyplot as plt
img=cv2.imread("Lenagray.jpg",0)

f=np.fft.fft2(img)
fourieBild=np.fft.fftshift(f)
fourieraum=20*np.log(np.abs(fourieBild))
#####Representation of the image in position space and Fourier space
# plt.subplot(121), plt.imshow(img,cmap="gray"),
# plt.title("Ortsraum"),plt.xticks([]),plt.yticks([])
# plt.subplot(122),plt.imshow(fourieraum,cmap="gray"),
# plt.title("Fourierraum"),plt.xticks([]),plt.yticks([])
# plt.show()

############################
#ideal low pass Filter
w,h=img.shape
D0=10
out=np.zeros((w,h),dtype=np.float32)
for u in range(w):
    for v in range(h):
        D=np.sqrt((u-w/2)**2 + (v-h/2)**2)
        if D <= D0:
            out[u,v]=1
        else:
            out[u,v]=0
resultFilterRaum=fourieraum*out
resultFilterBild=fourieBild*out
backshift=np.fft.ifftshift(resultFilterBild)
GlättungBild=np.abs(np.fft.ifft2(backshift))
plt.imshow(GlättungBild,cmap="gray"),plt.xticks([]),plt.yticks([]),
plt.title("Ideal-Filter")
plt.show()
####################################
#Butterworth-Filter
# w,h=img.shape
# D0=10
# n=1
# out=np.zeros((w,h),dtype=np.float32)
# for u in range(w):
#     for v in range(h):
#         D=np.sqrt((u-w/2)**2 + (v-h/2)**2)
#         out[u,v]=1/(1+(D/D0)**(2*n))
#
# resultFilterRaum=fourieraum*out
# resultFilterBild=fourieBild*out
# backshift=np.fft.ifftshift(resultFilterBild)
# GlättungBild=np.abs(np.fft.ifft2(backshift))
# plt.imshow(GlättungBild,cmap="gray"),plt.xticks([]),plt.yticks([]),
# plt.title("Butterworth-Filter")
# plt.show()

#######################################
##GaußFilter
# w,h=img.shape
# D0=10
# out=np.zeros((w,h),dtype=np.float32)
# for u in range(w):
#     for v in range(h):
#         D=np.sqrt((u-w/2)**2 + (v-h/2)**2)
#         out[u,v]=np.exp(-D**2/(2*D0*D0))
#
# resultFilterRaum=fourieraum*out
# resultFilterBild=fourieBild*out
# backshift=np.fft.ifftshift(resultFilterBild)
# GlättungBild=np.abs(np.fft.ifft2(backshift))
# plt.imshow(GlättungBild,cmap="gray"),plt.xticks([]),plt.yticks([]),
# plt.title("Gaiß-Filter")
# plt.show()