def gas(a, z):
  if a <= 0 or z <= 0:
    print("gak bisa 0 mah")
  else:
    return a*z
  p = gas(90, 5) + 7
  print(p)