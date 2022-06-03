import cv2
import webbrowser
a=cv2.VideoCapture(0)
dec=cv2.QRCodeDetector()
while True:
    _ , img=a.read()
    data,bbox,_=dec.detectAndDecode(img)
    if data:
        b=data
        break
    cv2.imshow("QRcode Scanner",img)
    if cv2.waitKey(1)==ord("q"):
        break
b=webbrowser.open(str(b))
a.release()
cv2.destroyAllWindows()