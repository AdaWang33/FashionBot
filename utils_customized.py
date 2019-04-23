## keywords extraction and synonyms processing methods
import re
import configparser
import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

config = configparser.ConfigParser()
config.read('config')
list_attr_cloth_path = config.get('fashion_data', 'LIST_ATTR_CLOTH_PATH')
list_attr_img_path = config.get('fashion_data', 'LIST_ATTR_IMG_PATH')

def getKeyWords(text):
    return(re.compile('\w+').findall(text))

def getAttributes(path = list_attr_cloth_path):
    # returns:
    # attributes: list of string consist of fashion attributes
    attributes_cloth = []
    file = open(path, "r")
    lines = file.read().split('\n')
    for line in lines[2:-1]:
        line = line[:-1]
        attr = line.rstrip()
        attributes_cloth.append(attr)
    return attributes_cloth

def generateImage(keyword):
   max_to_keep = 6
    fashion_attributes = getAttributes()
    index = fashion_attributes.index(keyword)

    # get image with its attributes info
    path = list_attr_img_path

    attributes_img = []

    file = open(path, "r")

    lines = file.read().split('\n')
    for line in lines[2:]:
        attr = line.strip().split()
        if (attr[index + 1] == '1'):
            attributes_img.append(attr[0])
        if (len(attributes_img) >= max_to_keep):
            break


def giveHint():
    print("Could you describe the style you're comfortable with?")
    
def noImage():
    print("Sorry, but i have no idea about this style.")
    
def display(image):
    # display image here
    img_path = 'fashion_data/'
    # display image here
    if len(image)!=0:
      for i in range(len(image)):
        path1 = img_path + image[i]
        img = cv2.imread(path1)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        title = 'predict img' + str(i + 1)
        plt.subplot(2, 3, i + 1)
        plt.imshow(img)
        plt.title(title)
        plt.xticks([])
        plt.yticks([])
      plt.show()
    else:
        noImage()

if __name__ == '__main__':
    # getAttributes()
    generateImage('ankle')
