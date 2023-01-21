# Copyright 2023 antillia.com Toshiyuki Arai
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
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

import keras_ocr
import traceback
from RecognizedObjectsVisualizer import RecognizedObjectsVisualizer
from ConfigParser import ConfigParser
from ImagePreprocessor import ImagePreprocessor


class KerasOCRTexBoxRecognizer:

  def __init__(self, config_file):
    print("--- KerasOCRTexBoxRecognizer.constructor")
    self.config    = ConfigParser(config_file)
  
    PARAMETER           = "parameter"
    self.images_dir     = self.config.get(PARAMETER, "images_dir")
    self.output_dir     = self.config.get(PARAMETER, "output_dir")
    #self.language_hints = self.config.get(PARAMETER, "language_hints")
    self.image_format   = self.config.get(PARAMETER, "image_format")

    PREPROCESSOR        = "preprocessor"
    self.preprocessing  = self.config.get(PREPROCESSOR, "preprocessing") 
    self.image_scaling  = self.config.get(PREPROCESSOR, "image_scaling")
    self.contrast       = self.config.get(PREPROCESSOR, "contrast")
    self.gray_image     = self.config.get(PREPROCESSOR, "gray_image")
    self.sharpness      = self.config.get(PREPROCESSOR, "sharpness")
  
    VISUALIZER          = "visualizer"
    self.font_name      = self.config.get(VISUALIZER, "font_name")
    self.draw_boundingbox  = self.config.get(VISUALIZER, "draw_boundingbox")
    self.expanding_ratio   = self.config.get(VISUALIZER, "expanding_ratio")
    self.scaling_on_nonpreprocessing = self.config.get(VISUALIZER, "scaling_on_nonpreprocessing", 1.0)
    if not os.path.exists(self.output_dir):
      os.makedirs(self.output_dir)

    try:
      # In the following of a creating pipeline code, keras-ocr will automatically 
      # download pretrained weights for the detector and recognizer respectively.
      self.pipeline = keras_ocr.pipeline.Pipeline()

      # This pipleline object has 
      # a text-detection CRAFT model written by pytorch 
      # see: https://github.com/faustomorales/keras-ocr/blob/master/keras_ocr/detection.py   
      # and
      # a text-recognition CRNN model written by tensorflow.keras
      # see: https://github.com/faustomorales/keras-ocr/blob/master/keras_ocr/recognition.py

      #
      # detection pretrained_weight
      #   "url": "https://github.com/faustomorales/keras-ocr/releases/download/v0.8.4/craft_mlt_25k.h5",

      # recognition pretrained_weight
      #    "url": "https://github.com/faustomorales/keras-ocr/releases/download/v0.8.4/crnn_kurapan.h5",
      
      # The kurapan.h5 supports the alphabet characters.
      #
    except:
      traceback.print_exc()


  def recognize(self):
    print("--- KerasOCRTexBoxRecognizer.recognize")
    # Get a set of three example images
    image_files  = glob.glob(self.images_dir + "/*.png")
    image_files += glob.glob(self.images_dir + "/*.jpg")

    for image_file in image_files:

      self.recognize_one(image_file)

  def recognize_one(self, image_file):
    preprocessor = ImagePreprocessor(gray_image=self.gray_image, preprocessing=self.preprocessing)

    img = preprocessor.read(image_file, image_scaling=self.image_scaling, 
                              contrast=self.contrast, sharpness=self.sharpness)
    
    basename = os.path.basename(image_file)
    if self.preprocessing:
      save_image_name = "preprocessed_" + "scaling_" + str(self.image_scaling) + "_contrast_" + str(self.contrast) + "_sharpness_" + str(self.sharpness) + "_" +basename
    else:
      save_image_name = "non_preprocessed_" + basename

    enhanced_image_file = os.path.join(self.output_dir, save_image_name)
    img.save(enhanced_image_file) #, "PNG")
      
    
    # Each list of predictions in prediction_groups is a list of
    # (word, box) tuples.
    predictions = self.pipeline.recognize([enhanced_image_file])
    prediction = predictions[0]

    # Visualize the predictions
    visualizer = RecognizedObjectsVisualizer(font_name=self.font_name)

    visualizer.visualize(prediction, enhanced_image_file, self.output_dir)  


if __name__ == "__main__":
  config_file = "./recognition.conf"
  try:
    if len(sys.argv) == 2:
      config_file = sys.argv[1]
    if not os.path.exists(config_file):
      raise Exception("Not found " + config_file)
    recognizer = KerasOCRTexBoxRecognizer(config_file)
    recognizer.recognize()

  except:
    traceback.print_exc()