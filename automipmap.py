from PIL import Image

src = Image.open("\source\source.png")
result = []
count = range(1,4)
resize = []

for num in range:
    result = "\results\img" + str(num) + ".png"
    resize.append(src.resize((src.size[0]/(2*num), src.size[1]/(2*num))))
    resize.save(result)




