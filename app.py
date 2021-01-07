from PIL import Image

im = Image.open('converter-test-2.jpg')

raw_pixels = list(im.getdata())
width, height = im.size

pixels = [raw_pixels[i * width:(i + 1) * width] for i in range(height)]
# print(pixels)


def make_image_ascii_string(pixels, width):
    """Given a list of pixels, returns the ascii representation of them"""

    # get a list of single digit grayscale colors for each pixel
    grayscale_pixel_list = make_grayscale_pixel_color_list(pixels)

    # reduce the images size to the given max width and height
    reduced_pixels = reduce_image_size(grayscale_pixel_list, width)

    # get the string representation of the image
    image_text = make_ascii_string_from_grayscale(reduced_pixels)

    for row in range(0, len(image_text)):
        row_string = ""
        for col in range(0, len(image_text[0])):
            row_string += image_text[row][col]
        print(row_string)


def reduce_image_size(pixels, maxwidth):

    image_width = len(pixels[0])
    image_height = len(pixels)

    print(image_width)
    print(image_height)

    height_ratio = width/height

    width_reduction_factor = int(image_width/maxwidth)
    height_reduction_factor = int(image_height/(height_ratio * maxwidth))

    reduced_list = []

    print(height_reduction_factor)

    row = 0
    while row < len(pixels) - height_reduction_factor:
        column = 0
        row_list = []
        while column < len(pixels[0]) - width_reduction_factor:

            group_avg = get_list_avg(
                pixels[row][column:column + width_reduction_factor])

            row_list.append(group_avg)

            column += width_reduction_factor

        reduced_list.append(row_list)
        row += height_reduction_factor
    return reduced_list


def make_ascii_string_from_grayscale(pixels):
    ascii_character_list = []

    for col in range(0, len(pixels[0])):
        ascii_character_row = []
        for row in range(0, len(pixels)):
            character = "X"

            if(pixels[row][col] > 127):
                character = "_"

            ascii_character_row.append(character)
        ascii_character_list.append(ascii_character_row)

    return ascii_character_list


def make_grayscale_pixel_color_list(pixels):

    pixel_color_list = []

    for col in range(0, len(pixels[0])):
        pixel_row = []
        for row in range(0, len(pixels)):

            # get the color data for each pixel
            pixel_color = pixels[row][col]

            # average the R, G, and B values together to get grayscale value
            color_avg = get_list_avg(pixel_color)

            # add the grayscale value to the row list
            pixel_row.append(color_avg)

        pixel_color_list.append(pixel_row)

    return pixel_color_list


def get_list_avg(values):
    """Returns the average of a given list rounded down"""
    avg = 0
    count = 0

    for val in values:
        count += 1
        avg += val

    avg = avg // count
    return avg


make_image_ascii_string(pixels, 120)
