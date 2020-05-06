from PIL import Image, ImageDraw
from mandelbrot import mandelbrot, MAX_ITER

# Image size (pixels)
WIDTH = 1080.0
HEIGHT = 720.0

# Plot window
RE_START = -2.0
RE_END = 1.0
IM_START = -1.0
IM_END = 1.0

palette = []

im = Image.new('RGB', (int(WIDTH), int(HEIGHT)), (0, 0, 0))
draw = ImageDraw.Draw(im)

for x in range(0, int(WIDTH)):
    for y in range(0, int(HEIGHT)):
        # Convert pixel coordinate to complex number
        c = complex(RE_START + (x / WIDTH) * (RE_END - RE_START),
                    IM_START + (y / HEIGHT) * (IM_END - IM_START))
        # Compute the number of iterations
        m = mandelbrot(c)
        # The color depends on the number of iterations
        color = int((m) * 255 / MAX_ITER)
        # Plot the point
        draw.point([x, y], (color, color, color))

im.save('output.png', 'PNG')
