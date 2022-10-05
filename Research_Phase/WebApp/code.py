from tkinter import image_names


def flip_img(img):
    return img.transpose(Image.FLIP_LEFT_RIGHT)

def toggle_img(img):
    return img.transpose(Image.TRANSPOSE)


# generate a function that toggles between two images
def toggle_img(img1, img2):
    def toggle():
        toggle_img.img = img1 if toggle_img.img == img2 else img2
        return toggle_img.img
    toggle_img.img = img1
    return toggle


# if dir exists, delete it
if os.path.exists('images'):
    shutil.rmtree('images')

# if dir exists, delete it
# else create it
if os.path.exists('images'):
    shutil.rmtree('images')
else:
    os.mkdir('images')