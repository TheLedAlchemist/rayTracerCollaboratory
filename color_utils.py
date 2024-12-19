import vec3
from contextlib import redirect_stdout

"""
Used to write a single pixel's color to stdout
"""
def write_color(f, color: vec3):
  r = color.x()
  g = color.y()
  b = color.z()

  rb = int(255.999 * r)
  gb = int(255.999 * g)
  bb = int(255.999 * b)

  # Redirect the standard output to the provided stream
  with redirect_stdout(f):
    print(f"{rb} {gb} {bb}")