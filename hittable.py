import ray, vec3, interval
from abc import ABC, abstractmethod
import math

class hit_record:
  p = vec3.vec3()
  normal = vec3.vec3()
  t = 0.0
  front_face: bool

  def set_face_normal(self, r: ray.ray, outward_normal: vec3.vec3):
    """
    Sets the normal vector. Outward_normal is assumed to have unit length.
    """

    self.front_face = r.direc.dot(outward_normal) < 0.0
    self.normal = outward_normal if self.front_face else -outward_normal

class hittable(ABC):
  @abstractmethod
  def hit(self, r: ray.ray, ray_t: interval.interval, rec: hit_record) -> bool:
    pass

class sphere(hittable):
  def __init__(self, center: vec3.vec3, radius: float):
    self.center = center
    self.radius = 0.0 if radius < 0 else radius

  def hit(self, r: ray.ray, ray_t: interval.interval, rec: hit_record) -> bool:
    o_to_c = self.center - r.origin()
    a = r.dir().length_squared()
    h = vec3.vec3.dot(r.dir(), o_to_c)
    c = o_to_c.length_squared() - self.radius * self.radius
    discrim = h*h - a*c
    
    if(discrim < 0):
      return False
    
    root_discrim = math.sqrt(discrim)

    root = (h - root_discrim)/a
    if (not ray_t.surrounds(root)):
      root = (h + root_discrim) / a
      if (not ray_t.surrounds(root)):
        return False

    rec.t = root
    rec.p = r.at(rec.t)
    outward_normal = (rec.p - self.center) / self.radius
    rec.set_face_normal(r, outward_normal)

    return True