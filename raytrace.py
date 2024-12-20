import math
import vec3, color_utils
import argparse

parser = argparse.ArgumentParser(
  prog="raytrace.py",
  description="This is a graphical raytracer written collaboratively by Matthew Gill and Jacob Shavel.\nAll code is interpreted from\
  the guide \"Ray Tracing in One Weekend\" by Peter Shirley, Trevor David Black, and Steve Hollasch."
)

parser.add_argument('--outputfname', default="testImg.ppm", type=str)

# Image properties
img_width = 256
img_height = 256

# TODO: Consider adding a progress bar
with open(parser.parse_args(["--outputfname"]), "w") as f:
  f.write(f"P3\n{img_width} {img_height}\n255\n")

  for i in range(img_height):
    for j in range(img_width):
      # Generate a cool color map
      color = vec3.vec3((i + j)/(2* (img_width - 1)), math.sin(i*j + 3)**2, .5)
      color_utils.write_color(f, color)

  f.close()
