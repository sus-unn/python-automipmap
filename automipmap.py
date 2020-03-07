from PIL import Image

src = Image.open("source\source.png")
result = []
resize = []
count = 4

for num in range(1, count):
    result.append("results\img" + str(num) + ".png")
    resize.append(src.resize((int(src.size[0]/(2*num)), int(src.size[1]/(2*num)))))

for num in range(0, count-1):
    resize[num].save(result[num])