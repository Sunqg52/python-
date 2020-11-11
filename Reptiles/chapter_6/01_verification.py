import tesserocr
from PIL import Image


# 直接使用图像处理库 tesserocr识别
# 对于难以识别的图片可将其转为灰度图像再指定二值化阈值进行调整



image = Image.open('code2.jpg')
image = image.convert('L')		# 传入参数L 将图片转化为灰度图像
# image = image.convert('1')	# 传入参数1 将图片进行二值化处理
threshold = 125					# 越低降噪越明显
table = []
for i in range(256):
	if i < threshold:
		table.append(0)
	else:
		table.append(1)
image = image.point(table, '1')
result = tesserocr.image_to_text(image)
print(result)

