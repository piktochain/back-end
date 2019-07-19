# pip install python-opencv==3.4.2.16
# pip install python-contrib-opencv==3.4.2.16
import cv2
import numpy as np


# 파일 경로
# 사진 리사이징 부분을 할시 변수 뒤에 _o 를 붙여주세요
def img_smil(original, image_to_compare):
    # 사진 리사이징 - 태스트 용

    original = np.array(original)
    image_to_compare = np.array(image_to_compare)
    # 1) Check if 2 images are equals

    if original.shape == image_to_compare.shape:
        print("The images have same size and channels")
        difference = cv2.subtract(original, image_to_compare)
        b, g, r = cv2.split(difference)

        if cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0:
            print("The images are completely Equal")
        else:
            print("The images are NOT equal")

    # 2) Check for similarities between the 2 images

    sift = cv2.xfeatures2d.SIFT_create()
    kp_1, desc_1 = sift.detectAndCompute(original, None)
    kp_2, desc_2 = sift.detectAndCompute(image_to_compare, None)

    index_params = dict(algorithm=0, trees=5)
    search_params = dict()
    flann = cv2.FlannBasedMatcher(index_params, search_params)

    matches = flann.knnMatch(desc_1, desc_2, k=2)

    good_points = []
    ratio = 0.65
    for m, n in matches:
        if m.distance < ratio * n.distance:
            good_points.append(m)

    # 일치하는 정도 출력
    print(len(good_points))
    if len(good_points) > 14:
        return True, len(good_points)
    else:
        return False, len(good_points)
