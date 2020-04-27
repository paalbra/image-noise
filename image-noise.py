import argparse

from PIL import Image
import numpy

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Produce a noisy image.")
    parser.add_argument("output", help="Path to output image")
    parser.add_argument("--width", type=int, default=1080, help="Image width in pixels")
    parser.add_argument("--height", type=int, default=720, help="Image height in pixels")
    args = parser.parse_args()

    data = numpy.random.randint(0, 20, (args.height, args.width))
    data += 50
    img = Image.fromarray(numpy.uint8(data))

    img.save(args.output)