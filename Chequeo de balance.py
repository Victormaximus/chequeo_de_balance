#!/usr/bin/env python
# coding: utf-8

# In[10]:


lista1= ["[","{","("] 
lista2= ["]","}",")"] 
def check(contrasena):
    pila = []
    for i in contrasena:
        if i in lista1:
            pila.append(i)
        elif i in lista2:
            reserva = lista2.index(i)
            if((len(pila)>0)) and (lista1[reserva]==pila[len(pila)-1]):
                pila.pop()
            else:
                return ("No esta balanceado")
    if len(pila)==0:
        return ("Esta balanceado")
    else:
        return "No esta balanceado"


# In[12]:


string = "{[]{()}}"
print(check(string))
        


# In[ ]:




