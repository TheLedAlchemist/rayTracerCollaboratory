import vec3, interval
from contextlib import redirect_stdout

"""
Used to write a single pixel's color to stdout
"""
def write_color(f, color: vec3):
  r = color.x()
  g = color.y()
  b = color.z()

  intensity = interval.interval(0.000, 0.999)
  rb = int(256 * intensity.clamp(r))
  gb = int(256 * intensity.clamp(g))
  bb = int(256 * intensity.clamp(b))

  # Redirect the standard output to the provided stream
  with redirect_stdout(f):
    print(f"{rb} {gb} {bb}")