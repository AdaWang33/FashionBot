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
    # returns:
    # first image path with attribute of given keyword or None
    
    # find index of the given keyword
    fashion_attributes = getAttributes()
    # print(len(fashion_attributes))
    # print(fashion_attributes[0])
    # print(fashion_attributes[-1])
    index = fashion_attributes.index(keyword)
    
    # get image with its attributes info
    path = list_attr_img_path
    attributes_img = []
    img_path = []
    
    file = open(path, "r")
    lines = file.read().split('\n')
    for line in lines[2:]:
        attr = line.split(' ')
        attr = attr[1:] # remove image path
        attr = list(filter(None, attr)) # get rid of empty elements
        
        attributes_img.append(attr)
        img_path.append(attr[0])
        
    max_possibility = np.max(attributes_img[:][index])
    # return image or None
    if max_possibility == 1:
        img_index = np.argmax(attributes_img[:][index])
        return img_path[img_index]
    else:
        return None

def giveHint():
    print("Could you describe the style you're comfortable with?")
    
def noImage():
    print("Sorry, but i have no idea about this style.")
    
def display(image):
    # display image here
    
    if image != None:
        plt.figure()
        plt.imshow(image) 
        plt.show()  
    else:
        noImage()

if __name__ == '__main__':
    # getAttributes()
    generateImage('ankle')