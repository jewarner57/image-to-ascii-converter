from PIL import Image, ImageDraw, ImageFont
from pixel import Pixel


class SerializeablePixel(Pixel):
    def __init__(self, pixel):
        super().__init__(pixel)

    def __json__(self):
        return dict(
            {"color": self.color, "char": self.char, "grayscale": self.grayscale}
        )


def create_gif_from_images(images, backgroundColor, fontFamilyNumber, textColor):
    createdImages = []

    for image in images:
        createdImages.append(
            create_image_from_ascii_string(
                image, backgroundColor, fontFamilyNumber, textColor, 8
            )
        )

    filename = "./static/images/conversions/gifConversion.gif"
    createdImages[0].save(
        filename, save_all=True, append_images=createdImages, duration=100, loop=0
    )

    return filename


def make_gif_ascii_string(image_path, character_key, width=80, height=None):
    width = int(width)
    if height is not None:
        height = int(height)

    gifImage = Image.open(image_path)

    firstImage = make_image_ascii_string(gifImage, character_key, width, height)
    frames = []

    for frame in range(0, gifImage.n_frames, 2):
        gifImage.seek(frame)
        frames.append(make_image_ascii_string(gifImage, character_key, width, height))

    responseData = {"previewImage": firstImage, "frames": frames}

    return responseData


def create_image_from_ascii_string(
    image_text, background_color, font_family_number, text_color, font_size=15
):
    # Create the image with the correct background color
    # Set the size to be the character width * number of characters

    fonts = {
        1: "SourceCodePro-Black",
        2: "CourierPrime-Bold",
        3: "DMMono-Medium",
        4: "SpaceMono-Bold",
        5: "RobotoMono-Bold",
    }

    imageHeight = len(image_text)
    imageWidth = len(image_text[0])
    fontSize = font_size
    fontName = fonts.get(int(font_family_number))
    fontWidth = fontSize * 0.5

    img = Image.new(
        "RGB",
        (int(fontWidth * imageWidth * 1.5), int(imageHeight * fontSize)),
        color=background_color,
    )

    # Get the chosen font
    fnt = ImageFont.truetype(f"./static/fonts/{fontName}.ttf", fontSize)

    # Draw the image
    d_img = ImageDraw.Draw(img)

    # For each row
    #   For each character
    #     Place a colored character with the correct width and height offset
    for r in range(0, imageHeight - 1):
        for c in range(0, imageWidth - 1):

            if text_color == "Black":
                fontColor = (0, 0, 0)
            else:
                fontColor = tuple(image_text[r][c].get("color"))

            d_img.text(
                (int(fontWidth * c * 1.5), int(fontSize * r)),
                image_text[r][c].get("char"),
                font=fnt,
                fill=(fontColor),
            )

    return img


def make_image_ascii_string(image_path, character_key, width=80, height=None):
    """Given a list of pixels, returns the ascii representation of them
    Takes the pixels of the image, the character length of the ascii result
    and the height in number of lines."""

    width = int(width)
    if height is not None:
        height = int(height)

    # get a matrix of pixels from an image
    pixels = get_image_pixels(image_path)

    # get the size reduction factors for the image
    reduction_factors = get_image_reduction_factors(pixels, width, height)

    # reduce the images size using the reduction factors
    reduced_pixels = reduce_image_size(
        pixels, reduction_factors[0], reduction_factors[1]
    )

    # get the string representation of the image
    image_text = make_ascii_string_from_pixels(reduced_pixels, character_key)

    return image_text


def get_image_pixels(image):

    if type(image) is not str:
        # get the imageObject
        im = image
    else:
        # open the image
        im = Image.open(image)

    # convert the image to use rgb format
    im = im.convert("RGB")

    # get list of raw pixels
    raw_pixels = list(im.getdata())
    width, height = im.size

    # process pixel list into a matrix
    pixels = [raw_pixels[i * width : (i + 1) * width] for i in range(height)]

    return pixels


def get_image_reduction_factors(pixels, maxwidth, maxheight=None):
    """Calculates the factors for reducing the size of an image so
    that it stays proportional and fits within the maxwidth and maxheight
    returns a tuple (width_factor, height_factor)"""

    image_width = len(pixels[0])
    image_height = len(pixels)

    height_ratio = (image_height * 2.8) / (image_width * 4)

    width_reduction_factor = int(image_width / maxwidth)

    # if no maxheight is given, make the height proportional to width
    if maxheight is None:
        height_reduction_factor = int((image_height / ((height_ratio * maxwidth))))
    else:
        height_reduction_factor = int(image_height / maxheight)

    if height_reduction_factor < 1:
        height_reduction_factor = 1
    if width_reduction_factor < 1:
        width_reduction_factor = 1

    return (width_reduction_factor, height_reduction_factor)


def reduce_image_size(pixels, width_reduction_factor, height_reduction_factor):
    """reduces the size of an array of pixels by the given reduction factors for
    width and height"""

    reduced_list = []
    row = 0

    while row < len(pixels) - height_reduction_factor:
        column = 0
        row_list = []

        while column < len(pixels[0]):

            pixel = SerializeablePixel(pixels[row][column])

            row_list.append(pixel)

            column += width_reduction_factor

        reduced_list.append(row_list)
        row += height_reduction_factor

    return reduced_list


def make_ascii_string_from_pixels(pixels, ascii_key):
    """converts an array of rgb pixels into an array of ascii
    symbols based on the brightness of each pixel"""
    ascii_character_list = []

    for row in range(0, len(pixels)):
        ascii_character_row = []
        for col in range(0, len(pixels[0])):

            # get the grayscale value of the pixel from its color
            pixels[row][col].getGrayscaleFromColor()

            # set the pixel to the corresponding char from the key
            pixels[row][col].char = ascii_key[
                pixels[row][col].grayscale % len(ascii_key) - 1
            ]

            # add the pixel to the display array
            ascii_character_row.append(pixels[row][col])

        ascii_character_list.append(ascii_character_row)

    return ascii_character_list
