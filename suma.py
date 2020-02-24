def sumaminima(vector, suma):
  vector=vector
  suma=suma
  w_=0
  while True:
    pos=randint(0,vector.shape[0])
    if vector[pos]>suma:
      w_+=1
      pass
    else: 
      w_+=1
      suma=suma-vector[pos]
    if vector.min()>suma:
      w_+=1
      return w_, suma
      break
  return w_
