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

# ImagePreprocessor.py
# 2023/01/21 to-arai


import os
from PIL import Image, ImageEnhance, ImageFilter

class ImagePreprocessor:
  def __init__(self, image_scaling=3.0, contrast=1.5, sharpness=4.0, gray_image=True, preprocessing=True):
    self.image_scaling = image_scaling
    self.contrast      = contrast
    self.gray_image    = gray_image
    self.sharpness     = sharpness #4.0 # 2.5
    self.preprocessing = preprocessing

  def read(self, image_file, image_scaling=3.0, contrast=2.5, sharpness=4.0):
    img = None

    self.image_scaling = image_scaling

    self.contrast      = contrast
    self.sharpness     = sharpness
    
    if os.path.exists(image_file):

      img = Image.open(image_file)
      img = img.convert("RGB")
      if self.preprocessing ==False:
        print("---No preprossing")
        return img

      #enhancer = ImageEnhance.Contrast(img)
      #img =  enhancer.enhance(self.contrast) #1.5) #1.5)

      # 1 enhance image contrast
      #enhancer = ImageEnhance.Sharpness(img)
      #img =  enhancer.enhance(1.5) #1.5) #1.5)
      #print("--- Image sharpened image")
      #enhancer = ImageEnhance.Contrast(img)
      #img =  enhancer.enhance(self.contrast) #1.5) #1.5)
      #print("--- Image enhances contrast up ")
      # 2 convert to gray_image
      if self.gray_image:
        print("--- Converted to gray image")
        img = img.convert("LA")
        img = img.convert("RGB")
 
      print("--- edge enhance more")
      w, h = img.size
      # 3 resize image 
      #print("--- image size w:{} h:{}".format(w, h))

      rw = float(w) * float(self.image_scaling)
      rh = float(h) * float(self.image_scaling)
      rw = int(rw)
      rh = int(rh)
      img = img.resize( (rw, rh))
      print("--- Image scaling {} Resized to w:{} h:{} from w:{} h:{}".format(self.image_scaling, rw, rh, w, h))
      # 3 sharpness
      # 1 enhance image contrast
      enhancer = ImageEnhance.Contrast(img)
      img =  enhancer.enhance(self.contrast) #1.5) #1.5)
      print("--- Image enhancement contrast: {}".format(self.contrast))

      enhancer = ImageEnhance.Sharpness(img)
      img = enhancer.enhance(self.sharpness)
      print("--- Image enhancement sharp: {}".format(self.sharpness))

    return img
