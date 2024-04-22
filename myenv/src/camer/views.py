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
import os
import io
import cv2
import base64
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import pytesseract as tess
from PIL import Image


def home(request):
    return render(request, 'index.html')

@csrf_exempt

# def open_camera(request):
#     cam1 = cv2.VideoCapture(0)
#     while True:
#         ret,frame=cam1.read()
        
#         if not ret:
#             print("Error")
#             break
    
#         cv2.imshow("testing",frame)
        # k=cv2.waitKey(1)
        # if k%256==27:
        #     print("Closed")
        #     break
        # elif k%256==32:
        #     img_name="Screen_shot.png"
        #     cv2.imwrite(img_name,frame)

        #     # DISPLAY IMAGE TAKEN
        #     cv2.imshow(img_name,frame) 
            
    # cam1.release()
    # cv2.destroyAllWindows()
    # cam1.release()


    # while True:
    #     ret,frame=cam.read()
    #     if not ret:
    #         print ("Error")
    #         break
    #     return cv2.imshow("testing",frame)

    # if not cam.isOpened():
    #     return JsonResponse({'error': 'Failed to open camera'}, status=500)

    # return JsonResponse({'success': 'Camera opened successfully'})


# def capture_image(request):
#     cam = cv2.VideoCapture(0)

#     if not cam.isOpened():
#         return JsonResponse({'error': 'Failed to open camera'}, status=500)

#     ret, frame = cam.read()
#     # cv2.imshow(frame)
#     cam.release()

#     if not ret:
#         return JsonResponse({'error': 'Failed to capture image'}, status=500)

#     _, buffer = cv2.imencode('.png', frame)
#     img_data = base64.b64encode(buffer).decode()

#     return JsonResponse({'img_data': img_data})


# new def


@csrf_exempt
def capture_image(request):
    cam = cv2.VideoCapture(0)

    if not cam.isOpened():
        return JsonResponse({'error': 'Failed to open camera'}, status=500)

    ret, frame = cam.read()
    cam.release()

    if not ret:
        return JsonResponse({'error': 'Failed to capture image'}, status=500)

    _, buffer = cv2.imencode('.png', frame)
    img_data = base64.b64encode(buffer).decode()

    return JsonResponse({'img_data': img_data})

def read_file(request):
    try:
        img_path = os.path.join(os.getcwd(), 'Screen_shot.png')
        if not os.path.exists(img_path):
            return JsonResponse({'error': 'Image file not found'}, status=404)

        with open(img_path, 'rb') as file:
            img_data = file.read()
            img = Image.open(io.BytesIO(img_data))
            text = tess.image_to_string(img)
            return JsonResponse({'text': text})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

@csrf_exempt
def opencam(request):
    cam = cv2.VideoCapture(0)

    if not cam.isOpened():
        return JsonResponse({'error': 'Failed to open camera'}, status=500)

    cv2.namedWindow("Lun")

    while True:
        ret, frame = cam.read()

        if not ret:
            return JsonResponse({'error': 'Failed to capture frame'}, status=500)

        cv2.imshow("testing", frame)
        k = cv2.waitKey(1)

        if k & 0xFF == 27:
            print("Closed")
            break

        elif k & 0xFF == 32:
            img_name = "Screen_shot.png"
            cv2.imwrite(img_name, frame)
            cv2.imshow(img_name, frame)

    cam.release()
    cv2.destroyAllWindows()