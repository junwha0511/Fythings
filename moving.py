import cv2
import time 
n = 1
flag = False
def diffImg(t0, t1, t2):
    d1 = cv2.absdiff(t2,t1)
    d2 = cv2.absdiff(t1,t0)
    return cv2.bitwise_and(d1, d2)

video = cv2.VideoCapture(0)

winName = "Movement Detector"
cv2.namedWindow(winName)

t_minus = cv2.cvtColor(video.read()[1], cv2.COLOR_RGB2GRAY)
t = cv2.cvtColor(video.read()[1], cv2.COLOR_RGB2GRAY)
t_plus = cv2.cvtColor(video.read()[1], cv2.COLOR_RGB2GRAY)

detectedNum = 0

while True:
    diff = diffImg(t_minus, t, t_plus)
    sum1 = 0
    sum0 = 0
    for i in diff:
        for j in i:
            if j>0:
                j=1
                sum1 +=1
            sum0 += 1
    
    #print('sum0: '+str(sum0))
    #print('sum1: '+str(sum1))
    if sum1>=110000:
        print(str(detectedNum)+'detected')
        detectedNum+=1
        flag = True
    else:
        if flag:
            cv2.imwrite('C:/a'+n+'.jpg',video.read()[1])
            if n==5:
                n=0
            n+=1
            flag = False

    cv2.imshow(winName, diff)
    t_minus = cv2.cvtColor(video.read()[1], cv2.COLOR_RGB2GRAY) 
    t = cv2.cvtColor(video.read()[1], cv2.COLOR_RGB2GRAY)
    t_plus = cv2.cvtColor(video.read()[1], cv2.COLOR_RGB2GRAY)
    
    key = cv2.waitKey(10)
    if key == 27:
        cv2.destroyWindow(winName)
        break

    #time.sleep(3)
