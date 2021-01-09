class Pixel:
    def __init__(self, color, grayscale=0):
        self.grayscale = grayscale,
        self.color = color
        self.char = ""

    def getGrayscaleFromColor(self):
        """Returns the average of a given list rounded down."""
        avg = 0
        count = 0

        for val in self.color:
            count += 1
            avg += val

        avg = avg // count
        self.grayscale = avg
