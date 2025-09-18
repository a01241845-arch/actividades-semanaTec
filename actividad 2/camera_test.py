#------------------------------------------------------------------------------------------------------------------
#   Camera test program
#------------------------------------------------------------------------------------------------------------------

import cv2

cam_port = 1
cam = cv2.VideoCapture(cam_port)

while True:

    result, frame = cam.read()    
    
    if result: 

        # Convertir a escala de grises
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # Detectar bordes con Canny
        edges = cv2.Canny(gray, 100, 200)

        cv2.imshow("Press q to quit", edges)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cam.release()
cv2.destroyAllWindows()

#------------------------------------------------------------------------------------------------------------------
#   End of file
#------------------------------------------------------------------------------------------------------------------
