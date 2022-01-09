#importar csv
import csv

base=[]
j=0
with open("synergy_logistics_database.csv","r") as archivo_csv:
  lector=csv.reader(archivo_csv)
  for linea in lector:
    if j==0:
      j=1
      continue
    base.append(linea)

#hacer tabla de todos los países
base_p1=[]
base_p2=[]
for linea in base:
  base_p1.append(linea[2])
  base_p2.append(linea[3])

cp1=set(base_p1)
cp2=set(base_p2)

#print(cp1)
#print(cp2)
#Hacer lista de rutas
cp3=cp1.union(cp2)
i=0
cp4=list(cp3)
no_rep=[]
p4=[]
for linea in cp4:
  p1=linea
  no_rep.append(p1)
  for linea2 in cp4:
    p2=linea2
    for linea3 in no_rep:
      if p2==linea3:
        i=1
  
    if p1==p2 or i==1:
      i=0
      continue
    p3=p1+"-"+p2
    p4.append(p3)

#print(p4)
#Hacer lista de tipo de exportaciones
base_t1=[]
for linea in base:
  base_t1.append(linea[7])

  

ct1=set(base_t1)
ct2=list(ct1)


key=[]
#Hacer lista de key

for linea1 in ct2:
  ruta=linea1
  for linea2 in p4:
    paises=linea2
    key1=paises+"-"+ruta
    key.append(key1)

#print(key)

#Ponerle dos keys a base general
tk1=[]
for linea1 in base:
  p1=linea1[2]
  p2=linea1[3]
  r1=linea1[7]
  imp=int(linea1[9])
  anio=int(linea1[4])
  key1=p1+"-"+p2+"-"+r1
  key2=p2+"-"+p1+"-"+r1
  if anio==2019 or anio==2020 or anio==2018:
    tk1.append([key1,key2,imp])

#for linea1 in tk1:
#  print(linea1)

final=[]
print("Hola, favor de esperar... cargando")
#print(len(tk1))
#print("hola")


j=0
i=0
for lin1 in key:
  key3=lin1
  #print(key3)
  acum=0
  acumimp=0
  j=j+1
  i=0

  #print("a")
  #print(j)


  for lin2 in tk1:
    key1=lin2[0]
    key2=lin2[1]
    #print(key1)
    imp=int(lin2[2])
    i=i+1
    #print("b")
    #print(i)
    if key3==key1 or key3==key2:
      acum=acum+1
      acumimp=acumimp+imp
  final.append([key3,acum,acumimp])

print("En un momento terminará de cargar...")
#for lin3 in final:
#  print(lin3)

#quitar lineas en 0
final2=[]

for linea1 in final:
  acum=int(linea1[1])
  acumimp=int(linea1[2])
  if acum>0 or acumimp>0:
    final2.append(linea1)

#print("Se acaba quitar 0")  
print("")
print("-------------------")
#Sacar 10 rutas más transitadas
print("Rutas con mayor tránsito")
tr=[]
auxw=0
while auxw==0:
  resto=[]
  aux1=0
  for prod1 in final2:
    aux1=0
    id=prod1[0]
    for prod2 in tr:
      id2=prod2[0]
      if id==id2:
        aux1=1
    if aux1==0:
      resto.append(prod1)

  if len(resto)==len(final2)-10:
    auxw=1
  else:
    maxvta=int(resto[0][1])
    maxid=resto[0][0]
    maximp=int(resto[0][2])
    
    for producto in resto:
      venta=int(producto[1])
      if venta>maxvta:
        maxvta=int(producto[1])
        maxid=producto[0]
        maximp=int(producto[2])
        
    tr.append([maxid,maxvta,maximp])

i=1
while i<=10:
  for lin1 in tr:
    print(lin1)
    i=i+1

#Sacar 10 rutas con mayor valor

tr=[]
auxw=0
while auxw==0:
  resto=[]
  aux1=0
  for prod1 in final2:
    aux1=0
    id=prod1[0]
    for prod2 in tr:
      id2=prod2[0]
      if id==id2:
        aux1=1
    if aux1==0:
      resto.append(prod1)

  if len(resto)==len(final2)-10:
    auxw=1
  else:
    maxvta=int(resto[0][1])
    maxid=resto[0][0]
    maximp=int(resto[0][2])
    
    for producto in resto:
      imp=int(producto[2])
      if imp>maximp:
        maxvta=int(producto[1])
        maxid=producto[0]
        maximp=int(producto[2])
        
    tr.append([maxid,maxvta,maximp])

print("")
print("-------------------")
print("Rutas con mayor valor acumulado")
i=1
while i<=10:
  for lin1 in tr:
    print(lin1)
    i=i+1

#Hacer lista de transporte
# ct2 es la lista de transportes
ct3=[]
for linea1 in ct2:
  tipo1=linea1
  acumcant=0
  acumval=0
  for linea2 in base:
    anio=int(linea2[4])
    tipo2=linea2[7]
    val=int(linea2[9])
    if (anio==2019 or anio==2020 or anio==2018) and (tipo1==tipo2):
      acumcant=acumcant+1
      acumval=acumval+val
  ct3.append([tipo1,acumcant,acumval])

#Acomodar de mayor a menor

tr=[]
auxw=0
acum=0
while auxw==0:
  resto=[]
  
  aux1=0
  for prod1 in ct3:
    aux1=0
    id=prod1[0]
    for prod2 in tr:
      id2=prod2[0]
      if id==id2:
        aux1=1
    if aux1==0:
      resto.append(prod1)
  

  if len(resto)==0:
    auxw=1
  else:
    maxvta=int(resto[0][1])
    maxid=resto[0][0]
    maximp=int(resto[0][2])
    
    for producto in resto:
      venta=int(producto[1])
      if venta>maxvta:
        maxvta=int(producto[1])
        maxid=producto[0]
        maximp=int(producto[2])
        
    tr.append([maxid,maxvta,maximp])
    acum=acum+maximp
    #print(acum)

print("")
print("-------------------")
print("Cantidad y valor por medio de transporte")

for lin1 in tr:
  print(lin1)





#cp4 es la lista de las rutas/países
#Ponerle dos keys a base general
tk1=[]
for linea1 in base:
  p1=linea1[2]
  p2=linea1[3]
  #r1=linea1[7]
  imp=int(linea1[9])
  anio=int(linea1[4])
  key1=p1+"-"+p2
  key2=p2+"-"+p1
  if anio==2019 or anio==2020 or anio==2018:
    tk1.append([p1,p2,imp])

#Sacar la suma de valores
tot_imp=[]
for linea1 in tk1:
  imp=int(linea1[2])
  tot_imp.append(imp)

tot_sum=sum(tot_imp)
tot_sum=tot_sum*0.8

#Agregar número de importaciones y valores
#print(cp4)

p5=[]
for linea1 in cp4:
  p1=linea1
  acum1=0
  acum2=0
  for linea2 in tk1:
    key1=linea2[0]
    key2=linea2[1]
    imp=int(linea2[2])
    if key1==linea1 or key2==linea1:
      acum1=acum1+1
      acum2=acum2+imp
  p5.append([p1,acum1,acum2])

#print(p5)

#Sacar rutas con el 80% del valor más transitadas
print("-------------")
print("Países con mayor valor")
tr=[]
auxw=0
acum=0
while auxw==0:
  resto=[]
  
  aux1=0
  for prod1 in p5:
    aux1=0
    id=prod1[0]
    for prod2 in tr:
      id2=prod2[0]
      if id==id2:
        aux1=1
    if aux1==0:
      resto.append(prod1)
  

  if acum>tot_sum:
    auxw=1
  else:
    maxvta=int(resto[0][1])
    maxid=resto[0][0]
    maximp=int(resto[0][2])
    
    for producto in resto:
      venta=int(producto[1])
      if venta>maxvta:
        maxvta=int(producto[1])
        maxid=producto[0]
        maximp=int(producto[2])
        
    tr.append([maxid,maxvta,maximp])
    acum=acum+maximp
    #print(acum)


for lin1 in tr:
  print(lin1)

    












  



  

  






