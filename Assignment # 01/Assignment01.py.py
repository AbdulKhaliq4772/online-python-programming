#!/usr/bin/env python
# coding: utf-8

# # Question # 01 - Print Poem

# In[12]:


print("Twinkle Twinkle Little Star,\n\tHow I wonder what you are\n\t\tUp above the world so high,\n\t\tLike a diamond in the sky, \nTwinkleTwinkle Little Star\n\tHow I wonder what you are");


# # Question # 02 - Print Date and Time

# In[13]:


import datetime
dateandtime=datetime.datetime.now();
print(dateandtime);


# # Question # 03 - Python Version

# In[18]:


import sys
print("Python version");
print(sys.version);


# # Question # 04 - Radius to Area of Circle

# In[25]:


radius=float(input("Enter radius (unit);"));
Area=((22/7)*(radius)*(radius));
print("Area of circle =", Area, "unit square");


# # Question # 05 - Reverse Order

# In[28]:


# input always takes values as an string
first_name=input("Enter First Name: ");
last_name=input("Enter Last Name: ");
full_name=first_name+" "+last_name;
print(full_name);
#Slicing method for reversing string
full_name=full_name[::-1]
print(full_name);


# # Question # 06 - addition

# In[30]:


# input always takes values as a string - must be converted into integer/float for sloving number
x=int(input("Enter first Number: "));
y=int(input("Enter second Number: "));
print("Result is",x+y);


# In[ ]:




