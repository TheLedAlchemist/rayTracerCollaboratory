import ray, vec3, interval
from abc import ABC, abstractmethod
import math

class material(ABC):
  @abstractmethod
  def scatter(r_in: ray.ray, rec, attenuation, scattered) -> bool:
    return False

class hit_record:
  p = vec3.vec3()
  normal = vec3.vec3()
  mat: material
  t = 0.0
  front_face: bool

  def set_face_normal(self, r: ray.ray, outward_normal: vec3.vec3):
    """
    Sets the normal vector. Outward_normal is assumed to have unit length.
    """

    self.front_face = r.direction.dot(outward_normal) < 0.0
    self.normal = outward_normal if self.front_face else -outward_normal

class hittable(ABC):
  @abstractmethod
  def hit(self, r: ray.ray, ray_t: interval.interval, rec: hit_record) -> bool:
    pass

class lambertian(material):
  def __init__(self, albedo: vec3.vec3) -> None:
    self.albedo = albedo

  def scatter(self, r_in: ray.ray, rec: hit_record, attenuation: vec3.vec3, scattered: ray.ray) -> bool:
    scatter_direction = rec.normal + vec3.vec3().random_unit_vector()
    
    # If the sum (scatter_direction) has a magnitude almost equal to 0, reset the scatter direction for safety
    if(scatter_direction.near_zero()):
      scatter_direction = rec.normal

    scattered.orig = rec.p
    scattered.direction = scatter_direction

    attenuation.x = self.albedo.x
    attenuation.y = self.albedo.y
    attenuation.z = self.albedo.z

    return True
  
class metal(material):
  def __init__(self, albedo: vec3.vec3, fuzz: float) -> None:
    self.albedo = albedo
    self.fuzz = 1.0 if fuzz > 1.0 else fuzz

  def scatter(self, r_in: ray.ray, rec: hit_record, attenuation: vec3.vec3, scattered: ray.ray) -> bool:
    reflected = r_in.dir().reflect(rec.normal)
    reflected = reflected.unit_vector() + (self.fuzz * vec3.vec3().random_unit_vector())

    scattered.orig = rec.p
    scattered.direction = reflected

    attenuation.x = self.albedo.x
    attenuation.y = self.albedo.y
    attenuation.z = self.albedo.z

    return scattered.direction.dot(rec.normal) > 0

class sphere(hittable):
  def __init__(self, center: vec3.vec3, radius: float, mat: material):
    self.center = center
    self.radius = 0.0 if radius < 0 else radius
    self.mat = mat

  def hit(self, r: ray.ray, ray_t: interval.interval, rec: hit_record) -> bool:
    o_to_c = self.center - r.origin()    
    a = r.dir().length_squared()
    h = r.dir().dot(o_to_c)
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
    rec.mat = self.mat

    return True