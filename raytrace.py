# Imports
import math

# Image properties
img_width = 256
img_height = 256

with open("testImg.ppm", "w") as f:
  f.write(f"P3\n{img_width} {img_height}\n255\n")

  for i in range(img_height):
    for j in range(img_width):
      r = (i + j)/(2* (img_width - 1))
      g = math.sin(i*j + 3)**2
      b = .5

      ir = int(255.999 * r)
      ig = int(255.999 * g)
      ib = int(255.999 * b)

      f.write(f"{ir} {ig} {ib}\n")
  
  f.close()
