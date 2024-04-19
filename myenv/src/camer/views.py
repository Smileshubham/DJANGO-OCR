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
import base64
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

def home(request):
    return render(request, 'index.html')

@csrf_exempt

def open_camera (request):
    cam1 = cv2.VideoCapture(0)
    while True:
        ret,frame=cam1.read()
        if not ret:
            print("Error")
            break
    cv2.imshow("testing",frame)
    cam1.release()

    # while True:
    #     ret,frame=cam.read()
    #     if not ret:
    #         print ("Error")
    #         break
    #     return cv2.imshow("testing",frame)

    # if not cam.isOpened():
    #     return JsonResponse({'error': 'Failed to open camera'}, status=500)

    # return JsonResponse({'success': 'Camera opened successfully'})


def capture_image(request):
    cam = cv2.VideoCapture(0)

    if not cam.isOpened():
        return JsonResponse({'error': 'Failed to open camera'}, status=500)

    ret, frame = cam.read()
    # cv2.imshow(frame)
    cam.release()

    if not ret:
        return JsonResponse({'error': 'Failed to capture image'}, status=500)

    _, buffer = cv2.imencode('.png', frame)
    img_data = base64.b64encode(buffer).decode()

    return JsonResponse({'img_data': img_data})


