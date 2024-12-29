import vec3, ray, interval, hittable, color_utils

class camera:
  def __init__(self):
    self.aspect_ratio = 1.0
    self.image_width = 100

  def render(self, world: hittable.hittable) -> None:
    self.initialize()

    with open("rayCastTest.ppm", "w") as f:
      f.write(f"P3\n{self.image_width} {self.image_height}\n255\n")

      for j in range(self.image_height):
        for i in range(self.image_width):
          pixel_center = self.pixel_00_loc + (i * self.pixel_delta_u) + (j * self.pixel_delta_v)
          ray_direction = pixel_center - self.center

          r = ray.ray(origin=self.center, direction=ray_direction)

          pixel_color = self.ray_color(r, world)
          color_utils.write_color(f, pixel_color)

      f.close()

  # Private
  def initialize(self) -> None:
    # Calculate the image height and ensure it's at least one
    self.image_height = int(self.image_width / self.aspect_ratio)
    self.image_height = self.image_height if self.image_height >= 1 else 1

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

  def ray_color(self, r: ray.ray, world: hittable.hittable):
    rec = hittable.hit_record()

    if(world.hit(r, interval.interval(0, float('inf')), rec)):
      return 0.5* (rec.normal + vec3.vec3(1, 1, 1))

    # Otherwise, Generate a cool color map background
    # unitdir = r.dir().unit_vector()
    # color = vec3.vec3( (unitdir.x() + unitdir.y())/2, math.sin(abs(unitdir.x())*abs(unitdir.y())*img_width)**2, .75)
    color = vec3.vec3(0.66, 0.66, 0.66)
    return color