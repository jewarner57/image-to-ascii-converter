from PIL import Image

im = Image.open('converter-test.jpg')

raw_pixels = list(im.getdata())
width, height = im.size

pixels = [raw_pixels[i * width:(i + 1) * width] for i in range(height)]
# print(pixels[0])


def make_image_ascii_string(pixels, width):
    """Given a list of pixels, returns the ascii representation of them"""

    # reduce the images size to the given max width and height
    reduced_pixels = reduce_image_size(pixels, width)

    # get a list of single digit grayscale colors for each pixel
    grayscale_pixel_list = make_grayscale_pixel_color_list(reduced_pixels)

    # get the string representation of the image
    image_text = make_ascii_string_from_grayscale(grayscale_pixel_list)

    for row in image_text:
        row_string = ""
        for column in image_text[0]:
            row_string += column
        print(row_string)


def reduce_image_size(pixels, width):
    return pixels


def make_ascii_string_from_grayscale(pixels):
    ascii_character_list = []

    for i in range(0, len(pixels)):
        ascii_character_row = []
        for j in range(0, len(pixels[0])):
            character = "X"
            if(pixels[i][j] > 127):
                character = "_"

            ascii_character_row.append(character)
        ascii_character_list.append(ascii_character_row)

    return ascii_character_list


def make_grayscale_pixel_color_list(pixels):

    pixel_color_list = []

    for i in range(0, len(pixels[0])):
        pixel_row = []
        for j in range(0, len(pixels)):

            # get the color data for each pixel
            pixel_color = pixels[i][j]

            # average the R, G, and B values together to get grayscale value
            color_avg = get_pixel_color_avg(pixel_color)

            # add the grayscale value to the row list
            pixel_row.append(color_avg)

        pixel_color_list.append(pixel_row)

    return pixel_color_list


def get_pixel_color_avg(pixel_color):
    """Returns the color average of a given pixel's rbg tuple"""
    color_avg = 0
    color_count = 0

    for color_val in pixel_color:
        color_count += 1
        color_avg += color_val

    color_avg = int(color_avg / color_count)
    return color_avg


make_image_ascii_string(pixels, 80)
