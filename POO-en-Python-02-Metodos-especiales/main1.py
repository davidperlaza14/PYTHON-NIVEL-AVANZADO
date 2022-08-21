class Fraccion:
  
  def __init__(self, num=0,den=1):
    if isinstance(num, int):
        self.num =num
    else:
        self.num = 0 
    if isinstance(den, int) and den != 0:
        self.den=den 
    else:
        self.den = 1 

#   def __del__(self):
#     print('Destruyendo el objeto: ',self.num,"/",self.den)

  def __str__(self):
        return "{"+ str(self.num) + "/" + str(self.den) + "}"

#   def imprime(self):
#     print("{",self.num,"/",self.den,"}")

#   def __mul__(self, b):
#     n = self.num * b.num
#     d = self.den * b.den
#     r = Fraccion(n,d)
#     return r
  def __add__(self, obj):
    n = self.num * obj.num + self.den * obj.num
    d = self.den * obj.den
    r = Fraccion(n,d)
    return r 

  def __eq__(self,b):
    pass

def main(): 

    a = Fraccion(4,5)
    b = Fraccion(2,3)
    r =  a + b
    print(r)

    # a = Fraccion(3,2)
    # b = Fraccion(2,5)
    # r =  a * b
    # print(r) 

#   a = Fraccion(2,7)
#   print(a)  
  
#   b = Fraccion(3,4)
#   b.imprime()  
  
if __name__ == "__main__":
    main() 