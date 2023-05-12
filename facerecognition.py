import cv2
from simple_facerec import SimpleFacerec

str = SimpleFacerec()
str.load_encoding_images('images/')


cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)


while True:
    ret, img = cap.read()
    
    face_locations, face_names = str.detect_known_faces(img)
    
    for face_loc, name in zip(face_locations, face_names):
        y1, x2, y2, x1  = face_loc[0], face_loc[1], face_loc[2], face_loc[3]
        
        cv2.putText(img, name, (x1,y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0,255,0), 2 )
        cv2.rectangle(img, (x1,y1), (x2,y2), (0,255,0), 2)
    
    
    cv2.imshow('frame', img)
    key = cv2.waitKey(1) & 0xFF
    
    if key == 27 or cv2.getWindowProperty('frame', cv2.WND_PROP_VISIBLE) < 1:
        cap.release()
        cv2.destroyAllWindows()
        break
    
    if key == ord('q'):
        cap.release()
        cv2.destroyAllWindows()
        break
    