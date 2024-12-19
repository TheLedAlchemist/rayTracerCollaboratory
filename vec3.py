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
  
  def __getitem__(self, index):
    return self.vector[index]  
  
  def __mul__(self, other):
    # Scalar multiplication
    if isinstance(self, (int, float)):
      return (other.x() * self, other.y() * self, other.z() * self)
    # Dot product
    if isinstance(other, vec3):
        return vec3(self.x() * other.x(), self.y() * other.y(), self.z() * other.z())
    # Scalar multiplication
    if isinstance(other, (int, float)):
      return vec3(other * self.x(), other * self.y(), other * self.z())
    else:
        raise TypeError("Unsupported operand type for multiplication")
     
    
    
vektor1 = vec3(1,2,3)
vektor2 = vec3(2,4,5)


print(-vektor1)
print(vektor1 + vektor2)
print(f"vektor1[0]={vektor1[0]}")
print(vektor1 * vektor2)
print(vektor1*6)
print(3*vektor1)
print(5.2*vektor1)
