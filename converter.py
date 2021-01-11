from PIL import Image
from pixel import Pixel

# print(pixels)

char_key_1 = ["#", "@", "X", "W", "B", "&", "M", "G",
              "F", "V", "C", "J", "?", "7", "I", "1",
              "=", "/", "*", "~", "-", "_"]

char_key_apples = ["#", "", "~", "`"]
char_key_inverted = [".", ",", "*", "/", "(", "#", "%", "&", "@"]
char_key_classic = ["@", "&", "%", "#", "(", "/", "*", ",", "."]


def make_image_ascii_string(image_path, character_key, width=80, height=None):
    """Given a list of pixels, returns the ascii representation of them
    Takes the pixels of the image, the character length of the ascii result
    and the height_reduction_factor which is a float from 0.1-1.0 ."""

    pixels = get_image_pixels(image_path)

    # get a list of single digit grayscale colors for each pixel
    pixel_object_list = make_pixel_object_list(pixels)

    # reduce the images size to the given max width and height
    reduced_pixels = reduce_image_size(
        pixel_object_list, width, height)

    # get the string representation of the image
    image_text = make_ascii_string_from_grayscale(
        reduced_pixels, character_key)

    return image_text

    # for row in range(0, len(image_text)):
    #     row_string = ""
    #     for col in range(0, len(image_text[0])):
    #         row_string += image_text[row][col]
    #     print(row_string)


def get_image_pixels(image_path):
    # open the image
    im = Image.open(image_path)
    # convert the image to use rgb format
    im = im.convert('RGB')

    # get list of raw pixels
    raw_pixels = list(im.getdata())
    width, height = im.size

    # process pixel list into a matrix
    pixels = [raw_pixels[i * width:(i + 1) * width] for i in range(height)]

    return pixels


def reduce_image_size(pixels, maxwidth, maxheight=None):
    """reduces the size of an array of pixels so that it matches the given
    maximum width and height factor."""

    image_width = len(pixels[0])
    image_height = len(pixels)

    height_ratio = image_width/image_height

    width_reduction_factor = int(image_width/maxwidth)

    # if no maxheight is given, make the height proportional to width
    if maxheight is None:
        height_reduction_factor = int(
            (image_height/(height_ratio * maxwidth)))
    else:
        height_reduction_factor = int(image_height/maxheight)

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

            group_avg = get_list_avg(
                pixels[row][column:(column + width_reduction_factor)])

            pixel = Pixel(group_avg)

            row_list.append(pixel)

            column += width_reduction_factor

        reduced_list.append(row_list)
        row += height_reduction_factor

    return reduced_list


def make_ascii_string_from_grayscale(pixels, ascii_key):
    """converts an array of grayscale rgb numbers (0-255) into ascii chars."""
    ascii_character_list = []

    for row in range(0, len(pixels)):
        ascii_character_row = []
        for col in range(0, len(pixels[0])):

            # get the grayscale value of the pixel from its color
            pixels[row][col].getGrayscaleFromColor()

            # set the pixel to the corresponding char from the key
            pixels[row][col].char = ascii_key[pixels[row][col].grayscale % len(
                ascii_key)-1]

            # add the pixel to the display array
            ascii_character_row.append(pixels[row][col])

        ascii_character_list.append(ascii_character_row)

    return ascii_character_list


def make_pixel_object_list(pixels):
    """Takes a list of rgb colors and converts them into a grayscale
    representation."""

    pixel_color_list = []

    for row in range(0, len(pixels)):
        pixel_row = []
        for col in range(0, len(pixels[0])):

            # get the color data for each pixel
            pixel_color = pixels[row][col]

            # average the R, G, and B values together to get grayscale value
            pixel = Pixel(pixel_color)

            # add the grayscale value to the row list
            pixel_row.append(pixel)

        pixel_color_list.append(pixel_row)

    return pixel_color_list


def get_list_avg(pixels):
    """Returns the average of a list of pixel's color"""

    avg = 0
    count = 0
    result = []

    for rgb in range(0, 3):
        for pixel in pixels:
            count += 1
            avg += pixel.color[rgb]

        avg = avg // count
        result.append(pixels[0].color[rgb])

    return tuple(result)

# make_image_ascii_string(pixels, char_key_apples, 90, 0.5)
