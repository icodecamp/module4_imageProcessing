'''This Example opens an Image and transform the image into grayscale, halftone, dithering, and primary colors.
You need PILLOW (Python Imaging Library fork) and Python 3.5
-Isai B. Cicourel'''

from PIL import Image

# Open an Image
def open_image(path):
  newImage = Image.open(path)
  return newImage

# Save Image
def save_image(image, path):
  image.save(path, 'png')


# Create a new image with the given size
def create_image(i, j):
  image = Image.new("RGB", (i, j), "white")
  return image


# Get the pixel from the given image
def get_pixel(image, i, j):
  # Inside image bounds?
  width, height = image.size
  if i > width or j > height:
    return None

  # Get Pixel
  pixel = image.getpixel((i, j))
  return pixel

# Create a Grayscale version of the image
def convert_grayscale(image):
  # Get size
  width, height = image.size

  # Create new Image and a Pixel Map
  new = create_image(width, height)
  pixels = new.load()

  # Transform to grayscale
  for i in range(???):
    for j in range(???):
      # Get Pixel
      pixel = get_pixel(image, i, j)

      # Get R, G, B values (This are int from 0 to 255)
      red =   pixel[0]
      green = pixel[1]
      blue =  pixel[2]

      # Transform to grayscale
      gray = ????
      gray = int(gray)
      # Set Pixel in new image
      pixels[i, j] = ????

  # Return new image
  return new

# Main
if __name__ == "__main__":
  # Load Image (JPEG/JPG needs libjpeg to load)
  input_path = raw_input("Please type the path of your image: ")
  original = open_image(input_path)

  # Convert to Grayscale and save
  new = convert_grayscale(original)

  output_path = raw_input("Please type the output path of the grayscale image: ")
  save_image(new, output_path)
