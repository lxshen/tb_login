from  PIL import Image, ImageChops


def get_gap(self, img1, img2):
    """
    获取缺口偏移量
    :param img1: 不带缺口图片
    :param img2: 带缺口图片
    :return:
    """
    left = 43
    for i in range(left, img1.size[0]):
        for j in range(img1.size[1]):
            if not self.is_pixel_equal(img1, img2, i, j):
                left = i
                return left



img1 = Image.open('index.png') #from PIL import Image 引用

img2 = Image.open('ind.png')

a = get_gap('index.png', 'ind.png')

# img3 = ImageChops.difference (img1, img2) #from PIL import ImageChops

print(a)