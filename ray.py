import vec3

class ray:

  def __init__(self, origin = vec3.vec3(0, 0, 0), direction = vec3.vec3(0, 0, 0)):
    self.orig = origin
    self.direction = direction

  def origin(self):
    return self.orig
  
  def dir(self):
    return self.direction
  
  def at(self, t: float):
    return self.orig + t*self.direction
