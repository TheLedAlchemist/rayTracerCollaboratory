import math
import vec3, color_utils, hittable, hittable_list
import ray
import argparse

# parser = argparse.ArgumentParser(
#   prog="raytrace.py",
#   description="This is a graphical raytracer written collaboratively by Matthew Gill and Jacob Shavel.\nAll code is interpreted from\
#   the guide \"Ray Tracing in One Weekend\" by Peter Shirley, Trevor David Black, and Steve Hollasch."
# )

# parser.add_argument('--outputfname', default="testImg.ppm", type=str)

# Constants
infinity = float('inf')
pi = 3.1415926535897932385

# Utility
degrees_to_radians = lambda degrees : degrees * pi / 180.0


def ray_color(r: ray.ray, world: hittable.hittable):
  rec = hittable.hit_record()

  if(world.hit(r, 0, infinity, rec)):
    return 0.5* (rec.normal + vec3.vec3(1, 1, 1))

  # Otherwise, Generate a cool color map background
  # unitdir = r.dir().unit_vector()
  # color = vec3.vec3( (unitdir.x() + unitdir.y())/2, math.sin(abs(unitdir.x())*abs(unitdir.y())*img_width)**2, .75)
  color = vec3.vec3(0.66, 0.66, 0.66)
  return color

if __name__ == "__main__":

  ## Image properties
  aspect_ratio = 16.0 / 9.0
  img_width = 256

  # Calculate the image height and ensure it's at least one
  img_height = int(img_width / aspect_ratio)
  img_height = img_height if img_height >= 1 else 1

  ## World
  world = hittable_list.hittable_list()

  world.add(hittable.sphere(vec3.vec3(0, 0, -1), 0.5))
  world.add(hittable.sphere(vec3.vec3(0, -100.5, -1), 100))

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

        r = ray.ray(origin=camera_center, direction=ray_direction)

        pixel_color = ray_color(r, world)
        color_utils.write_color(f, pixel_color)

    f.close()

  print("[ Render ] Done!")