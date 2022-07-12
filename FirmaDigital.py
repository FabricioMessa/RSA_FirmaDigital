import random
import math
import hashlib
#import numpy as np 

s = 40

#funciones de los pdf
def euclides(a, b): #yala
    if b == 0 :
        return a
    else:
      return euclides(b, a % b)

def euclides_extendido(a, b):
    if a == 0 :
        return b, 0, 1
    mcd,x1,y1 = euclides_extendido(b % a, a)
    x = y1 - (b//a) * x1
    y = x1
    return mcd,x,y

def modulo(a,b): 
    r=a%b
    if r < 0:
        r=r+ b;
    return r

def inversa(a,b):
    m, a, y = euclides_extendido(a, b)
    if m == 1:
      a = modulo(a, b)
    return a

def exp_modular(a, x, n):
  c = a % n
  r = 1
  while(x > 0):
    if x % 2 != 0:
      r = (r * c) % n
    c = (c * c) % n
    x = x//2
  return r

def compuesto(a, n, t, u):
  x = exp_modular(a,u,n)
  if x == 1 or x == n - 1:
    return False
  for i in range(t):
    x = exp_modular(x,2,n)
    if x == n-1:
      return False
  return True

def Miller_Rabin(n,s):
  t = 0
  u = n - 1
  while (u % 2 == 0):
    u = u / 2
    t = t + 1
  for j in range(1, s):
    a = random.randint(2, n-1)
    if compuesto(a, n, t, u):
      return False
  return True

def phi(n):
    r = 0
    for i in range(n):
        d = euclides(i, n)
        if d == 1:
            r = r + 1
    return r

def gen_bits(b):
    n = random.randint(0, (2**b) - 1)
    m = (2**(b-1)) + 1
    n = n | m
    return n

def generar_primo(b):
    n = gen_bits(b)
    while Miller_Rabin(n, s) is False:
        n = n + 2
    return n

#-------------------------RSA----------------------------
def RSA(K):
  bool = True
  while bool:
    p = generar_primo(K)
    q = generar_primo(K)
    if p != q:
      bool = False
  print("valor de p: " + str(p))
  print("valor de q: " + str(q))
  n = p * q
  euler_p = p - 1
  euler_q = q - 1
  euler = euler_p * euler_q
  bool = True
  while bool:
    e = random.randint(3, n - 1)
    if (euclides(e, euler) == 1):
      bool = False
  d = inversa(e,euler)
  #RESPUESTAS
  print("n es : " + str(n))
  #print(n)
  print("e es : " + str(e))
  #print(e)
  print("d es : " + str(d))
  #print(d)
  public = [n,e]
  private = [n, d]
  print("Llave publica " + str(public))
  print("Llave privada " + str(private))
  print()
  print("Mensaje 1 = Hola Mundo")
  m1 = hashlib.sha1()
  m1.update(b"Hola Mundo")
  entero1 = m1.hexdigest()
  double1 = (int(entero1,16))
  print("Mensaje en hexadecimales utilizando sha - 1: " + str(entero1))
  print("Mensaje en decimales utilizando sha-1: " + str(double1))
  cifrar = (double1**d)%n
  print("Firma digital: " + str(cifrar))
  decifrar = (cifrar**e)%n
  print("Mensaje decifrado: " + str(decifrar))
  #comprobar si son iguales
  if double1 == decifrar:
      print("Son el mismo")
  else:
      print("Son diferentes")
  print()
  print("Mensaje 2 = Permanente C")
  m2 = hashlib.sha1()
  m2.update(b"Permanente C")
  entero2 = m2.hexdigest()
  double2 = (int(entero2,16))
  print("Mensaje en hexadecimales utilizando sha - 1: " + str(entero2))
  print("Mensaje en decimales utilizando sha-1: " + str(double2))
  cifrar2 = (double2**d)%n
  print("Firma digital: " + str(cifrar2))
  decifrar2 = (cifrar2**e)%n
  print("Mensaje decifrado: " + str(decifrar2))
  #comprobar si son iguales
  if double2 == decifrar2:
      print("Son el mismo")
  else:
      print("Son diferentes")
  print()
  print("Mensaje 3 = San Pablo")
  m3 = hashlib.sha1()
  m3.update(b"San Pablo")
  entero3 = m3.hexdigest()
  double3 = (int(entero3,16))
  print("Mensaje en hexadecimales utilizando sha - 1: " + str(entero3))
  print("Mensaje en decimales utilizando sha-1: " + str(double3))
  cifrar3 = (double3**d)%n
  print("Firma digital: " + str(cifrar3))
  decifrar3 = (cifrar3**e)%n
  print("Mensaje decifrado: " + str(decifrar3))
  #comprobar si son iguales
  if double3 == decifrar3:
      print("Son el mismo")
  else:
      print("Son diferentes")
  print()
  return print("Termino el programa")

print(RSA(32))
