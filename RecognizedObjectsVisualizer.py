# RecognizedObjectsVisualizer.py

# See also:
#
# keras𝑜𝑐𝑟𝐷𝑜𝑐𝑢𝑚𝑒𝑛𝑡𝑎𝑡𝑖𝑜 
#     Fausto Morales
# https://keras-ocr.readthedocs.io/_/downloads/en/latest/pdf/
# See also:
# https://github.com/faustomorales/keras-ocr/releases

import os
import sys
import glob
import matplotlib.pyplot as plt

import cv2
import keras_ocr
import traceback
from PIL import Image, ImageDraw, ImageFont

TEXT_HORIZONTAL = 0
TEXT_VERTICAL   = 1

class RecognizedObjectsVisualizer:

  def __init__(self, font_name= "BIZ-UDMinchoM.ttc"):
    self.font_name  = font_name
 

  def get_font(self, height, width):

    fsize = 14
    direction = TEXT_VERTICAL
    try:
      #if height % 2 == 1:
      #  height += 1
      fsize = width

      if height < width:
        fsize = height
        direction = TEXT_HORIZONTAL
      fsize = int(fsize)
      #print("----- font_name {}  fsize {}".format(self.font_name, fsize))
      font = ImageFont.truetype(self.font_name, fsize) 
    except IOError:
      print("Failed to font_name {} size {} ".format(self.font_name, fsize))
      try:
       font = ImageFont.truetype(self.font_name, 20)
      except IOError:
       font = ImageFont.truetype('arial.ttf', 20)
    
    return (font, direction)


  def visualize(self, recognized_objects, image_file, output_dir, 
                draw_boundingbox=True, expanding_ratio=1.0):
    org = Image.open(image_file)
    w, h = org.size
    #if recognized_objects.preprocessing == False:
    #  scaling_ratio = recognized_objects.scaling_on_nonpreprocessing
    #  w = int(w * scaling_ratio)
    #  h = int(h * scaling_ratio)
    
    #2023/01/05 
    w = int (w * expanding_ratio)
    h = int (h * expanding_ratio)
    self.draw_recognized_objects(w, h, recognized_objects, image_file, output_dir, draw_boundingbox)


  def draw_recognized_objects(self, width, height, recognized_objects, image_file, output_dir, draw_boundingbox):

    img = Image.new("RGB", (width,  height), (255, 255, 255))
    #texts      = recognized_objects.texts
    #rectangles = recognized_objects.rectangles

    draw = ImageDraw.Draw(img)
    #list_len =len(rectangles)
    for pred in recognized_objects:
      text, bbox = pred
      [min_x, min_y] = bbox[0]
      [max_x, max_y] = bbox[2]
      print("--- text {}".format(text))
      print("--- bbox {}".format(bbox))
      #print(" {}".format(texts[i]))
      #print(" ({}, {})  ({}, {})".format(min_x, min_y, max_x, max_y))
      # [(x0, y0), (x1, y1)]
      if draw_boundingbox:
        draw.rectangle([(min_x, min_y), (max_x, max_y)], fill=None, outline="red", width=1)
      h = max_y - min_y
      w = max_x - min_x
      (font, direction) = self.get_font(h, w)
      if direction == TEXT_HORIZONTAL:
        draw.text((min_x, min_y), text, fill='black', font=font)
      else:
        #print("VERT {}".format(texts[i]))
        y = min_y
        for ch in text:
          draw.text((min_x, y), ch, fill="black", font=font)
          #print(ch)
          y += w

    basename = os.path.basename(image_file)
    
    output_file = os.path.join(output_dir,basename)
    print("--- output_file {}".format(output_file))

    img.save(output_file) #, "PNG") 


