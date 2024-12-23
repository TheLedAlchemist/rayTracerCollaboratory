import math

class vec3:
  vector = [0.0, 0.0, 0.0]

  def __init__(self, x = 0.0, y = 0.0, z = 0.0):
    self.vector = [x, y, z]
  
  def x(self):
    return self.vector[0] 
  
  def y(self):
    return self.vector[1]
  
  def z(self):
    return self.vector[2]
  
  def __str__(self):
    return f"{self.vector[0]} {self.vector[1]} {self.vector[2]}"
  
  def __neg__(self):
    return vec3(-self.x(), -self.y(), -self.z())
  
  def __add__(self, other):
    return vec3(self.x() + other.x(), self.y() + other.y(), self.z() + other.z())
  
  def __iadd__(self, other):
    return self.__add__(other)
  
  def __getitem__(self, index):
    return self.vector[index]
  
  def __setitem__(self, index, element):
    self.vector[index] = element
    return self.vector[index]
  
  def __mul__(self, other):
    # Scalar multiplication
    # Dot product
    if isinstance(other, vec3):
        return vec3(self.x() * other.x(), self.y() * other.y(), self.z() * other.z())
    # Scalar multiplication
    if isinstance(other, (int, float)):
      return vec3(other * self.x(), other * self.y(), other * self.z())
    else:
        raise TypeError("Unsupported operand type for multiplication")
  
  def __rmul__(self, scalar):
    if isinstance(scalar, (int, float)):
      return self.__mul__(scalar)  # Scalar multiplication is commutative
    else:
      raise TypeError("Unsupported operand type for multiplication")
    
  def __truediv__(self, other):
    if isinstance(other, (int, float)):
        return vec3(self[0]/float(other), self[1]/float(other), self[2]/float(other))
    
  def __itruediv__(self, other):
    if isinstance(other, (int, float)):
        return vec3(self[0]/float(other), self[1]/float(other), self[2]/float(other))

  def __sub__(self, other):
    if isinstance(other, vec3):
      return vec3(self.x() - other.x(), self.y() - other.y(), self.z() - other.z())
  
  def __isub__(self, other):
    return self.__sub__(other)

  def dot(a, b):
    return (float(a.x()) * b.x()
            + a.y() * b.y()
            + a.z() * b.z())
  
  def length_squared(self):
    return self.dot(self)

  def length(self):
    return math.sqrt(self.length_squared())

  def cross(self,other):
    return vec3(self[1] * other[2] - self[2] * other[1],
                self[2] * other[0] - self[0] * other[2],
                self[0] * other[1] - self[1] * other[0])
  
  def unit_vector(self):
    return self/self.length()