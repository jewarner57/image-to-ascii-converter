from PIL import Image
from pixel import Pixel

# previously written character keys
char_key_1 = [
    "#",
    "@",
    "X",
    "W",
    "B",
    "&",
    "M",
    "G",
    "F",
    "V",
    "C",
    "J",
    "?",
    "7",
    "I",
    "1",
    "=",
    "/",
    "*",
    "~",
    "-",
    "_",
]

char_key_apples = ["#", "", "~", "`"]
char_key_inverted = [".", ",", "*", "/", "(", "#", "%", "&", "@"]
char_key_classic = ["@", "&", "%", "#", "(", "/", "*", ",", "."]


def make_image_ascii_string(image_path, character_key, width=80, height=None):
    """Given a list of pixels, returns the ascii representation of them
    Takes the pixels of the image, the character length of the ascii result
    and the height in number of lines."""

    pixels = get_image_pixels(image_path)

    # reduce the images size to the given max width and height
    reduced_pixels = reduce_image_size(pixels, width, height)

    # get the string representation of the image
    image_text = make_ascii_string_from_pixels(reduced_pixels, character_key)

    return image_text


def get_image_pixels(image_path):
    # open the image
    im = Image.open(image_path)
    # convert the image to use rgb format
    im = im.convert("RGB")

    # get list of raw pixels
    raw_pixels = list(im.getdata())
    width, height = im.size

    # process pixel list into a matrix
    pixels = [raw_pixels[i * width : (i + 1) * width] for i in range(height)]

    return pixels


def reduce_image_size(pixels, maxwidth, maxheight=None):
    """reduces the size of an array of pixels so that it matches the given
    maximum width and height factor."""

    image_width = len(pixels[0])
    image_height = len(pixels)

    height_ratio = image_width / image_height

    width_reduction_factor = int(image_width / maxwidth)

    # if no maxheight is given, make the height proportional to width
    if maxheight is None:
        height_reduction_factor = int((image_height / (height_ratio * maxwidth)))
    else:
        height_reduction_factor = int(image_height / maxheight)

    if height_reduction_factor < 1:
        height_reduction_factor = 1
    if width_reduction_factor < 1:
        width_reduction_factor = 1

    reduced_list = []

    row = 0

    while row < len(pixels) - height_reduction_factor:
        column = 0
        row_list = []

        while column < len(pixels[0]):

            pixel = Pixel(pixels[row][column])

            row_list.append(pixel)

            column += width_reduction_factor

        reduced_list.append(row_list)
        row += height_reduction_factor

    return reduced_list


def make_ascii_string_from_pixels(pixels, ascii_key):
    """converts an array of rgb pixels into an ascii representation"""
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
