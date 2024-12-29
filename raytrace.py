import math, vec3, color_utils, hittable, hittable_list, camera, ray, interval, random

# Constants
infinity = float('inf')
pi = 3.1415926535897932385

# Utility
degrees_to_radians = lambda degrees : degrees * pi / 180.0

random_double = lambda  min = 0, max = 1: min + (max - min)*random.random()

if __name__ == "__main__":

  ## World
  world = hittable_list.hittable_list()

  world.add(hittable.sphere(vec3.vec3(0, 0, -1), 0.5))
  world.add(hittable.sphere(vec3.vec3(0, -100.5, -1), 100))

  cam = camera.camera()

  cam.aspect_ratio = 16.0/9.0
  cam.image_width = 400
  cam.samples_per_pixel = 100

  print("[ Render ] Beginning image render")
  cam.render(world)
  print("[ Render ] Done!")