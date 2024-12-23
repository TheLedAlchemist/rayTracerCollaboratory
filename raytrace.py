import math
import vec3, color_utils
import ray
import argparse

# parser = argparse.ArgumentParser(
#   prog="raytrace.py",
#   description="This is a graphical raytracer written collaboratively by Matthew Gill and Jacob Shavel.\nAll code is interpreted from\
#   the guide \"Ray Tracing in One Weekend\" by Peter Shirley, Trevor David Black, and Steve Hollasch."
# )

# parser.add_argument('--outputfname', default="testImg.ppm", type=str)

def did_hit_sphere(center: vec3.vec3, radius: float, r: ray.ray):
  o_to_c = center - r.origin()
  a = vec3.vec3.dot(r.dir(), r.dir())
  b = -2.0 * vec3.vec3.dot(r.dir(), o_to_c)
  c = vec3.vec3.dot(o_to_c, o_to_c) - radius * radius
  discrim = b*b - 4*a*c
  
  if(discrim < 0):
    return -1.0
  else:
    return (-1.0*b - math.sqrt(discrim))/(2.0*a)


def ray_color(r: ray.ray):
  t = did_hit_sphere(vec3.vec3(0,0, -1), 0.5, r)
  if(t > 0.0):
    normal = (r.at(t) - vec3.vec3(0, 0, -1)).unit_vector()
    return 0.5*vec3.vec3(normal.x() + 1, normal.y() + 1, normal.z() + 1)

  # Otherwise, Generate a cool color map
  unitdir = r.dir().unit_vector()
  
  color = vec3.vec3( (unitdir.x() + unitdir.y())/2, math.sin(abs(unitdir.x())*abs(unitdir.y())*img_width)**2, .75)
  return color

## Image properties
aspect_ratio = 16.0 / 9.0
img_width = 256

# Calculate the image height and ensure it's at least one
img_height = int(img_width / aspect_ratio)
img_height = img_height if img_height >= 1 else 1

## Camera Properties, set position to (0, 0, 0) and viewport distance (focal length)

focal_length = 1.0
port_height = 2.0
port_width = port_height * (float(img_width)/img_height)
camera_center = vec3.vec3(0, 0, 0)

## Calculate the 'image coordinates' and set up the coordinate system
viewport_u = vec3.vec3(port_width, 0, 0)
viewport_v = vec3.vec3(0, -port_height, 0)

# Find the 'delta vectors' for TODO: what??
pixel_delta_u = viewport_u / img_width
pixel_delta_v = viewport_v / img_height

# Calculate location of upper-leftmost pixel
port_upper_left = camera_center - vec3.vec3(0, 0, focal_length) - viewport_u/2 - viewport_v/2
pixel_00_loc = port_upper_left + 0.5 * (pixel_delta_u + pixel_delta_v)

#
# Perform the image rendering
# TODO: Consider adding a progress bar
# 

print("[ Render ] Beginning image render")

with open("rayCastTest.ppm", "w") as f:
  f.write(f"P3\n{img_width} {img_height}\n255\n")

  for j in range(img_height):
    for i in range(img_width):
      pixel_center = pixel_00_loc + (i * pixel_delta_u) + (j * pixel_delta_v)
      ray_direction = pixel_center - camera_center

      cast_ray = ray.ray(origin=camera_center, direction=ray_direction)

      pixel_color = ray_color(cast_ray)
      color_utils.write_color(f, pixel_color)

  f.close()

print("[ Render ] Done!")
