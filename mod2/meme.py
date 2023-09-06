from PIL import Image, ImageDraw, ImageFont

print("Генератор мемов запущен!")

# 1 часть
# top_text = input("Введите верхний текст: ")
# bottom_text = input("Введите нижний текст: ")
# stop_words = ['111', '222', '333']
# for word in stop_words:
#     top_text = top_text.replace(word, 'очень жаль!')

# 2 часть
text_type = int(input("Введите 1, если нужен только нижний текст, и 2, если и верхний, и нижний: "))

top_text = ""
bottom_text = ""

if text_type == 1:
    top_text = input("Введите нижний текст: ")
elif text_type == 2:
    top_text = input("Введите верхний текст: ")
    bottom_text = input("Введите нижний текст: ")
else:
    print('не верный режим')
    quit()


#image = Image.open('scary.jpg')
#часть 3
memes = ['scary.jpg', 'shark_falls.jpg', 'terrible_story.jpg', 'where_to_sit.jpg']

print('Дан список картинок. Выбери нужную!')
for id_img, img in enumerate(memes):
    print(id_img + 1, img)
choice_img = int(input('№ картинки  '))
image = Image.open(memes[choice_img - 1])
###########

draw = ImageDraw.Draw(image)
font = ImageFont.truetype('arial.ttf', size=70)
width, heigth = image.size
text = draw.textbbox((0,0), top_text, font)


draw.text(((width-text[2])/2, 10), top_text, font=font, fill='yellow')

draw.text(((width-text[2])/2, (heigth-text[3]) - 10), bottom_text, font=font, fill='yellow')

image.save('new_meme.jpg')


print(top_text, bottom_text)
