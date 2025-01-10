import vec3, interval
from contextlib import redirect_stdout
import math

"""
Used to write a single pixel's color to stdout in a gamma color space
"""
def write_color(f, color: vec3):
  r = math.sqrt(color.x()) if color.x() > 0.0 else 0.0
  g = math.sqrt(color.y()) if color.y() > 0.0 else 0.0
  b = math.sqrt(color.z()) if color.z() > 0.0 else 0.0

  intensity = interval.interval(0.000, 0.999)
  rb = int(256 * intensity.clamp(r))
  gb = int(256 * intensity.clamp(g))
  bb = int(256 * intensity.clamp(b))

  # Redirect the standard output to the provided stream
  with redirect_stdout(f):
    print(f"{rb} {gb} {bb}")