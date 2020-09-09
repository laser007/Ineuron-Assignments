#!/usr/bin/env python
# coding: utf-8

# In[1]:


x =[]
for i in range(2000, 3201):
        if (i%7==0)and (i%5!=0):
            x.append(str(i))
print(','.join(x))
        


# In[2]:


First_name = input("Enter your First Name: ")
Last_name = input("Enter your Last Name: ")
print(Last_name, First_name)


# In[3]:


Diameter = int(input("Enter the diameter: "))
radius =int(Diameter / 2)
Volume_Sphere = (4*22)%(3*7)*radius**3
print ("Volume of Sphere is: ", Volume_Sphere)


# In[ ]:




