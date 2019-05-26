#!/usr/bin/env python
# coding: utf-8

# ## Примените всевозможные операции к данным множествам, выделяя различные подмножества
# накинем 2 балла
# 
# <img src="set_food.png" width="700" height="700">

# In[1]:


pizza = {"dough", "tomatoes", "pepperoni", "ground pepper", "sweet basil",
         "a lot of cheeeese", "onion", "garlic", "salt", "oregano"}
shaverma = {"lavash", "cucumbers", "tomatoes", "sauce", "fried chicken", "onion", "cabbage"}


# # Объединение множеств
# Объединение множеств включает в себя каждый элемент множества *pizza* **или** *shaverma*

# In[2]:


pizza | shaverma


# # Пересечение множеств
# Пересечение множеств включает в себя каждый элемент множества *pizza* **и** *shaverma*

# In[3]:


pizza & shaverma


# # Разность множеств
# Разность множеств *pizza* \ *shaverma* включает в себя каждый элемент множества *pizza* **и не принадлежащий** *shaverma*

# In[4]:


pizza - shaverma


# Разность множеств *shaverma* \ *pizza* включает в себя каждый элемент множества *shaverma* **и не принадлежащий** *pizza*

# In[5]:


shaverma - pizza


# # Симметрическая разность множеств
# Симетрическая разность множеств включает в себя каждый элемент **либо** множества *shaverma*, **либо** множества *pizza*, но не включает в себя элементы принадлежащие одновременно двум этим множествам

# In[6]:


pizza ^ shaverma


# Логично предположить что данное выражение окажется верным:

# In[7]:


(pizza ^ shaverma) == ((pizza - shaverma) | (shaverma - pizza)) == ((pizza | shaverma) - (shaverma & pizza))

