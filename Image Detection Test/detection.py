from PIL import Image
from io import BytesIO
import cv2
import numpy as np
import requests


def read_image(url: str) -> np.array:
    image = Image.open(BytesIO(requests.get(url, stream=True).content))
    image = image.resize((450, 250))
    image_np = np.array(image)

    return image_np


def scale_image(image_np: np.array):
    image_grayscale = cv2.cvtColor(image_np, cv2.COLOR_BGR2GRAY)
    image_blurred = cv2.GaussianBlur(image_grayscale, (5, 5), 0)
    image_dilated = cv2.dilate(image_blurred, np.ones((3, 3)))

    structuring_kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
    image_morph_close = cv2.morphologyEx(
        image_dilated, cv2.MORPH_CLOSE, structuring_kernel)

    return image_morph_close


def detect_cascade(image_array, image_normalized, source_xml: str, url=False):
    cascade_classifier = cv2.CascadeClassifier(source_xml)
    cars_found_array = cascade_classifier.detectMultiScale(
        image_normalized, 1.1, 1)

    for (x, y, width, height) in cars_found_array:
        cv2.rectangle(image_array, (x, y),
                      (x + width, y + height), (0, 0, 255), 2)

    image = Image.fromarray(image_array)
    image.save("Output Files/" + url[-10:] +
               "_processed.jpg" if url else 'Test.jpg')


def video_part():
    cascade_src = 'Required Files/cars.xml'
    video_src = 'Cars.mp4'

    cap = cv2.VideoCapture(video_src)
    car_cascade = cv2.CascadeClassifier(cascade_src)
    video = cv2.VideoWriter('Output Files/result.avi',
                            cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 20.0, (int(cap.get(3)), int(cap.get(4))))
# cant make d video output work :< using m1

    while True:
        ret, img = cap.read()

        if (type(img) == type(None)):
            break

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        cars = car_cascade.detectMultiScale(gray, 1.1, 2)

        for (x, y, w, h) in cars:
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 255), 2)

    video.write(img)
    video.release()


if __name__ == '__main__':
    # url = input('Enter Image URL: ')
    # image_array = read_image(url)
    # image_scaled = scale_image(image_array)
    # detect_cascade(image_array, image_scaled, 'Required Files/cars.xml', url)

    # video_part()
