import cv2
import numpy as np
from PIL import Image
import os

def is_black_image(img_path, threshold=5):
    """검은 이미지(NSFW) 여부 판단"""
    img = Image.open(img_path).convert("L")
    return np.mean(np.array(img)) < threshold

def is_white_background(img_path, threshold=240):
    """흰 배경 여부 판단"""
    img = Image.open(img_path).convert("RGB")
    img_np = np.array(img)
    
    corners = [
        img_np[0, 0],
        img_np[0, -1],
        img_np[-1, 0],
        img_np[-1, -1],
    ]
    
    avg_color = np.mean(corners)
    return avg_color > threshold

def auto_crop_image(img_path, save_path=None, padding=20):
    """이미지 자동 크롭"""
    img = cv2.imread(img_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    _, thresh = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY_INV)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    if contours:
        x, y, w, h = cv2.boundingRect(max(contours, key=cv2.contourArea))
        x = max(x - padding, 0)
        y = max(y - padding, 0)
        cropped_img = img[y:y+h+padding, x:x+w+padding]
        if save_path:
            cv2.imwrite(save_path, cropped_img)
        return cropped_img
    else:
        print(f"❗ crop 대상 없음: {img_path}")
        return img

def fix_white_background(img_path, save_path=None):
    """흰 배경으로 수정"""
    img = cv2.imread(img_path)
    if img is None:
        print(f"❌ 이미지 불러오기 실패: {img_path}")
        return None

    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower_white = np.array([0, 0, 180])
    upper_white = np.array([180, 40, 255])
    mask = cv2.inRange(img_hsv, lower_white, upper_white)
    img[mask == 0] = [255, 255, 255]

    if save_path:
        cv2.imwrite(save_path, img)
    print("✅ 흰 배경으로 재 생성")
    return img

def get_unique_filename(filename):
    """고유한 파일명 생성"""
    base, ext = os.path.splitext(filename)
    counter = 1
    while os.path.exists(filename):
        filename = f"{base}_{counter}{ext}"
        counter += 1
    return filename 