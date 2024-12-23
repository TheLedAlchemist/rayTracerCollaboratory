import hittable

class hittable_list(hittable.hittable):
  objects: list

  def __init__(self):
    self.objects = []

  def clear(self) -> None:
    self.objects.clear()

  def add(self, obj) -> None:
    self.objects.append(obj)

  def hit(self, r, ray_tmin: float, ray_tmax: float, rec: hittable.hit_record) -> bool:
    temp_rec = hittable.hit_record()
    hit_anything = False
    closest_so_far = ray_tmax

    for object in self.objects:
      if(object.hit(r, ray_tmin, closest_so_far, temp_rec)):
        hit_anything = True
        closest_so_far = temp_rec.t
        rec.t = temp_rec.t
        rec.normal = temp_rec.normal
        rec.front_face = temp_rec.front_face
        rec.p = temp_rec.front_face
    
    return hit_anything
    
# 6.5 and 6.6