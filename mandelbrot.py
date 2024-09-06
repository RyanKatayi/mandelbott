# Mandelbrot set ASCII art generator

def mandelbrot(c, max_iter):
    z = 0
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z*z + c
    return max_iter

def generate_ascii(width, height, max_iter):
    ascii_chars = "@%#*+=-:. "  # Characters for different depths
    for y in range(height):
        for x in range(width):
            # Scale the coordinates to the Mandelbrot set range (-2.5 to 1 for x, -1 to 1 for y)
            re = (x / width) * 3.5 - 2.5
            im = (y / height) * 2.0 - 1.0
            c = complex(re, im)
            m = mandelbrot(c, max_iter)
            # Map the iteration count to the ASCII characters, ensuring it's within bounds
            ascii_index = min(m * len(ascii_chars) // max_iter, len(ascii_chars) - 1)
            print(ascii_chars[ascii_index], end="")
        print()

# Generate the ASCII Mandelbrot set with specified dimensions and iterations
generate_ascii(80, 40, 100)
