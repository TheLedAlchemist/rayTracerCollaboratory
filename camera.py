import vec3, ray, interval, hittable, color_utils, raytrace

class camera:
  def __init__(self):
    self.aspect_ratio = 1.0
    self.image_width = 100
    self.samples_per_pixel = 10
    self.max_depth = 10

  def render(self, world: hittable.hittable) -> None:
    self.initialize()

    with open("rayCastTest.ppm", "w") as f:
      # Write the file header
      f.write(f"P3\n{self.image_width} {self.image_height}\n255\n")

      # Begin casting rays into the scene
      for j in range(self.image_height):
        for i in range(self.image_width):

          pixel_color = vec3.vec3(0, 0, 0)

          for sample in range(self.samples_per_pixel):
            r = self.get_ray(i, j)
            pixel_color += self.ray_color(r, self.max_depth, world)

          color_utils.write_color(f, self.pixel_samples_scale * pixel_color)

        if ((float(j) / self.image_height) % 0.1) > 0.09:
          print(float(j)/self.image_height) 

      f.close()

  # Private
  def initialize(self) -> None:
    # Calculate the image height and ensure it's at least one
    self.image_height = int(self.image_width / self.aspect_ratio)
    self.image_height = self.image_height if self.image_height >= 1 else 1

    # Antialiasing number of samples
    self.pixel_samples_scale = 1.0 / self.samples_per_pixel

    # Initialize the camera's origin
    self.center = vec3.vec3(0, 0, 0)

    # Camera's view Properties
    focal_length = 1.0
    viewport_height = 2.0
    viewport_width = viewport_height * (float(self.image_width)/self.image_height)
    
    # Calculate the 'image coordinates' and set up the coordinate system
    viewport_u = vec3.vec3(viewport_width, 0, 0)
    viewport_v = vec3.vec3(0, -viewport_height, 0)

    # Establish conversion between viewport and image coordinates
    self.pixel_delta_u = viewport_u / self.image_width
    self.pixel_delta_v = viewport_v / self.image_height

    # Calculate location of upper-leftmost pixel
    port_upper_left = self.center - vec3.vec3(0, 0, focal_length) - viewport_u/2 - viewport_v/2
    self.pixel_00_loc = port_upper_left + 0.5 * (self.pixel_delta_u + self.pixel_delta_v)

  def get_ray(self, i: int, j: int) -> ray.ray:
    offset = self.sample_square()
    pixel_sample = self.pixel_00_loc + ((i + offset.x()) * self.pixel_delta_u) + ((j + offset.y()) * self.pixel_delta_v)

    ray_origin = self.center
    ray_direction = pixel_sample - ray_origin

    return ray.ray(origin=self.center, direction=ray_direction) 

  def sample_square(self) -> vec3.vec3:
    # The following returns a point within a unit square centered at (0, 0)
    return vec3.vec3(raytrace.random_double() - 0.5, raytrace.random_double() - 0.5, 0)

  def ray_color(self, r: ray.ray, depth: int, world: hittable.hittable):
    if depth <= 0:
      return vec3.vec3(0, 0, 0)
    
    rec = hittable.hit_record()

    # If an object was hit, continue scattering and decrement depth
    if(world.hit(r, interval.interval(0.001, float('inf')), rec)):
      direction = vec3.vec3().random_on_hemisphere(rec.normal)
      
      return 0.5 * self.ray_color(ray.ray(rec.p, direction), depth - 1, world)

    # Otherwise, Generate a cool color map background
    # unitdir = r.dir().unit_vector()
    # color = vec3.vec3( (unitdir.x() + unitdir.y())/2, math.sin(abs(unitdir.x())*abs(unitdir.y())*img_width)**2, .75)
    color = vec3.vec3(0.77, 0.77, 0.77)
    return color