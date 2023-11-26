import os
import fitz
from PIL import Image,ImageChops

def compare_pdf_files(path1, path2):
    if not path1.endswith("pdf") or not path2.endswith(".pdf"):
        return False
    # pdf转为图片
    pageNum = 0
    with fitz.open(path1) as pdf1:
        pageNum = pdf1.page_count
        for i in range(pdf1.page_count):
            page = pdf1.load_page(1)
            image_list = page.get_pixmap()
            pathname = path1.replace(".pdf","")
            image_list.save(f"{pathname}_page{i+1}.jpg","JPEG")
    with fitz.open(path2) as pdf2:
        page = pdf2.load_page(1)
        image_list = page.get_pixmap()
        pathname = path2.replace(".pdf", "")
        image_list.save(f"{pathname}_page{i + 1}.jpg", "JPEG")
    # 开始比较图片
    ifSame = True
    for i in range(0, pageNum):
        newpath1 = path1.replace(".pdf","")
        img1 = Image.open(f"{newpath1}_page{i + 1}.jpg")
        newpath2 = path2.replace(".pdf", "")
        img2 = Image.open(f"{newpath2}_page{i + 1}.jpg")
        diff = ImageChops.difference(img1, img2)
        if diff.getbbox():
            ifSame = False
            break
    return ifSame
