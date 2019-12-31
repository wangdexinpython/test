
from wand.image import Image

class pdf2txt1():
    def __init__():
        pass
    def pdf_to_picture1(,pdf_filename,pdf_resolution,imageformat):
        image_pdf = Image(filename=pdf_filename, resolution=pdf_resolution)
        image_page = image_pdf.convert(imageformat)

        req_image = []
        for img in image_page.sequence:
            img_page = Image(image=img)
            req_image.append(img_page.make_blob(imageformat))

        # 遍历req_image,保存为图片文件
        i = 0
        for img in req_image:
            ff = open(str(i) + imageformat, 'wb')
            ff.write(img)
            ff.close()
            i += 1


if __name__ == '__main__':
    paf = pdf2txt1()

    paf.pdf_to_picture1('wwww',300,"jbk")