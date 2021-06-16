import os, math
from app import app
from unittest import TestCase
from converter import get_image_pixels, get_image_reduction_factors, reduce_image_size
from PIL import Image


def get_image_dimensions(image_path):
    """Gets the width and height of an image and
    returns them as a new dict"""

    img = Image.open(image_path)
    width, height = img.size
    img.close()

    return {"width": width, "height": height}


#################################################
# Tests
#################################################


class AuthTests(TestCase):
    def setUp(self):
        """Executed prior to each test."""
        app.config["TESTING"] = True
        app.config["DEBUG"] = False

    def test_get_image_pixels(self):
        """Tests the get_image_pixels method"""

        testImage = "./test_images/converter-test-2.jpg"
        image_dimensions = get_image_dimensions(testImage)

        pixels = get_image_pixels(testImage)

        # Test Width and Height
        self.assertEqual(len(pixels[0]), image_dimensions.get("width"))
        self.assertEqual(len(pixels), image_dimensions.get("height"))

    def test_get_image_reduction_factors(self):
        """Tests the get_image_reduction_factors method"""

        testImage = "./test_images/converter-test-4.jpg"
        image_dimensions = get_image_dimensions(testImage)

        maxwidth = 200
        maxheight = 100

        pixels = get_image_pixels(testImage)
        reduction_factors = get_image_reduction_factors(pixels, maxwidth, maxheight)

        actualWidth = image_dimensions.get("width") / reduction_factors[0]
        differenceFromWidthMax = abs(maxwidth - actualWidth)

        actualHeight = image_dimensions.get("height") / reduction_factors[1]
        differenceFromHeightMax = abs(maxheight - actualHeight)

        # Test width and height should not be more than
        # (reduction factor) different than max width/height
        self.assertLess(
            differenceFromWidthMax,
            reduction_factors[0],
        )

        self.assertLess(
            differenceFromHeightMax,
            reduction_factors[1],
        )

    def test_reduce_image_size(self):
        testImage = "./test_images/converter-test-4.jpg"
        image_dimensions = get_image_dimensions(testImage)

        maxwidth = 200
        maxheight = 100

        pixels = get_image_pixels(testImage)
        reduction_factors = get_image_reduction_factors(pixels, maxwidth, maxheight)

        reduced_pixels = reduce_image_size(
            pixels, reduction_factors[0], reduction_factors[1]
        )

        expectedWidth = image_dimensions.get("width") / reduction_factors[0]
        realWidth = len(reduced_pixels[0])
        widthdiff = abs(expectedWidth - realWidth)

        expectedHeight = image_dimensions.get("height") / reduction_factors[1]
        realHeight = len(reduced_pixels)
        heightdiff = abs(expectedHeight - realHeight)

        # difference between real and expected size should be less than 1
        self.assertLess(widthdiff, 1)
        self.assertLess(heightdiff, 1)