# views.py

# import cv2
# from django.http import HttpResponse

# def capture_image(request):
#     cam = cv2.VideoCapture(0)
#     ret, frame = cam.read()
#     cam.release()
#     cv2.destroyAllWindows()

#     if ret:
#         # Save the captured image
#         img_name = "Screen_shot.png"
#         cv2.imwrite(img_name, frame)
#         return HttpResponse(status=200)
#     else:
#         return HttpResponse(status=500)

# views.py

# import os
# import cv2
# from django.http import HttpResponse
# from django.conf import settings

# def capture_image(request):
#     cam = cv2.VideoCapture(0)
#     ret, frame = cam.read()
#     cam.release()
#     cv2.destroyAllWindows()

#     if ret:
#         # Save the captured image to the media folder
#         img_name = "Screen_shot.png"
#         img_path = os.path.join(settings.MEDIA_ROOT, 'mycam', img_name)
#         cv2.imwrite(img_path, frame)
#         return HttpResponse(status=200)
#     else:
#         return HttpResponse(status=500)

# views.py

import cv2
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def capture_image(request):
    # Open the camera
    cam = cv2.VideoCapture(0)

    # Check if the camera is opened successfully
    if not cam.isOpened():
        return HttpResponse(status=500)

    while True:
        # Check if the frame is captured successfully
        ret, frame = cam.read()

        # Capture frame-by-frame
        if not ret:
            break

        # Display the frame
        cv2.imshow("Captured Image", frame)
        
        # Check for key press to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        elif cv2.waitKey(1)%256==32:
            img_name="Screen_shot.png"
            cv2.imwrite(img_name,frame)

            # DISPLAY IMAGE TAKEN
            cv2.imshow(img_name,frame) 
    # Release the camera and close OpenCV windows
    cam.release()
    cv2.destroyAllWindows()

    return HttpResponse(status=200)
