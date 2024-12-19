import math
import vec3, color_utils

# Image properties
img_width = 256
img_height = 256

# TODO: Consider adding a progress bar
with open("testImg.ppm", "w") as f:
  f.write(f"P3\n{img_width} {img_height}\n255\n")

  for i in range(img_height):
    for j in range(img_width):
      # Generate a cool color map
      color = vec3.vec3((i + j)/(2* (img_width - 1)), math.sin(i*j + 3)**2, .5)
      color_utils.write_color(f, color)

  f.close()
