import os
import easyocr  # pip install easyocr
import cv2

'''
def cv_imread(file_path):
    cv_img = cv2.imdecode(np.fromfile(file_path, dtype=np.uint8), cv2.IMREAD_COLOR)
    return cv_img
'''

image_path = '1.png'
print("当前工作目录:", os.getcwd())
print("文件绝对路径:", os.path.abspath(image_path))
print("文件是否存在:", os.path.exists(image_path))
if os.path.exists(image_path):
    print("文件大小:", os.path.getsize(image_path), "字节")

# 初始化 EasyOCR Reader
print("正在初始化 EasyOCR...")
reader = easyocr.Reader(['ch_sim', 'en'], gpu=False)
print("EasyOCR 初始化完成。")


# 方法一：直接用 cv2.imread 读取并传入数组
img = cv2.imread(image_path)
if img is not None:
    result = reader.readtext(img)
    print("OCR 结果:", result)
