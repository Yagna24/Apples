#!/usr/bin/env python
# coding: utf-8

# **Connect google drive**

# In[ ]:


pip install --upgrade gpustat


# In[2]:


# Check if NVIDIA GPU is enabled
get_ipython().system('nvidia-smi')


# In[3]:


from google.colab import drive
drive.mount('/content/gdrive')
get_ipython().system('ln -s /content/gdrive/My\\ Drive/ /mydrive')
get_ipython().system('ls /mydrive')


# **1) Clone, configure & compile Darknet**
# 
# 

# In[ ]:


# Clone
get_ipython().system('git clone https://github.com/AlexeyAB/darknet')


# In[ ]:


# Configure
get_ipython().run_line_magic('cd', 'darknet')
get_ipython().system("sed -i 's/OPENCV=0/OPENCV=1/' Makefile")
get_ipython().system("sed -i 's/GPU=0/GPU=1/' Makefile")
get_ipython().system("sed -i 's/CUDNN=0/CUDNN=1/' Makefile")


# In[ ]:


# Compile
get_ipython().system('make')


# **2) Configure yolov3.cfg file**

# In[ ]:


# Make a copy of yolov3.cfg
get_ipython().system('cp cfg/yolov3.cfg cfg/yolov3_training.cfg')


# In[ ]:


# Change lines in yolov3.cfg file
get_ipython().system("sed -i 's/batch=1/batch=64/' cfg/yolov3_training.cfg")
get_ipython().system("sed -i 's/subdivisions=1/subdivisions=16/' cfg/yolov3_training.cfg")
get_ipython().system("sed -i 's/max_batches = 500200/max_batches = 6000/' cfg/yolov3_training.cfg")
get_ipython().system("sed -i '610 s@classes=80@classes=3@' cfg/yolov3_training.cfg")
get_ipython().system("sed -i '696 s@classes=80@classes=3@' cfg/yolov3_training.cfg")
get_ipython().system("sed -i '783 s@classes=80@classes=3@' cfg/yolov3_training.cfg")
get_ipython().system("sed -i '603 s@filters=255@filters=24@' cfg/yolov3_training.cfg")
get_ipython().system("sed -i '689 s@filters=255@filters=24@' cfg/yolov3_training.cfg")
get_ipython().system("sed -i '776 s@filters=255@filters=24@' cfg/yolov3_training.cfg")


# **3) Create .names and .data files**

# In[ ]:


get_ipython().system("echo -e 'Wearing Mask\\n2nd item\\n3rd item' > data/obj.names")
get_ipython().system("echo -e 'classes= 3\\ntrain  = data/train.txt\\nvalid  = data/test.txt\\nnames = data/obj.names\\nbackup = /mydrive/yolov3' > data/obj.data")


# **4) Save yolov3_training.cfg and obj.names files in Google drive**

# In[ ]:


get_ipython().system('cp cfg/yolov3_training.cfg /mydrive/yolov3/yolov3_testing.cfg')
get_ipython().system('cp data/obj.names /mydrive/yolov3/classes.txt')


# **5) Create a folder and unzip image dataset**

# In[ ]:


get_ipython().system('mkdir data/obj')
get_ipython().system('unzip /mydrive/yolov3/images.zip -d data/obj')


# **6) Create train.txt file**

# In[ ]:


import glob
images_list = glob.glob("data/obj/*.jpg")
with open("data/train.txt", "w") as f:
    f.write("\n".join(images_list))


# **7) Download pre-trained weights for the convolutional layers file**

# In[ ]:


get_ipython().system('wget https://pjreddie.com/media/files/darknet53.conv.74')


# **8) Start training**

# In[ ]:


get_ipython().system('./darknet detector train data/obj.data cfg/yolov3_training.cfg darknet53.conv.74 -dont_show')
# Uncomment below and comment above to re-start your training from last saved weights
#!./darknet detector train data/obj.data cfg/yolov3_training.cfg /mydrive/yolov3/yolov3_training_last.weights -dont_show

