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

# CosineSimilarity.py
#
# 2022/10/17 toshiyuki.arai

import numpy as np

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

#########################################
#
class CosineSimilarity:
  ##
  # Constructor
  def __init__(self):
    self.tfidf_vect = TfidfVectorizer(token_pattern='(?u)\\b\\w+\\b')

  # Vetorize a pair of (string1, string2)
  def vectorize(self, string1, string2):
    corpus = [string1, string2]
    tfidf = self.tfidf_vect.fit_transform(corpus)
    return tfidf.toarray()

  # Evaluate cosine_similarity between string1 and string2
  
  def evaluate(self, string1, string2):
    tfidf_array = self.vectorize(string1, string2)
    similarity_matrix =cosine_similarity(tfidf_array, tfidf_array, 2)
    return similarity_matrix


  def compute(self, string1, string2):
    tfidf_array = self.vectorize(string1, string2)

    similarity_matrix = cosine_similarity(tfidf_array, tfidf_array, 2)
    similarity = similarity_matrix[0][1]
    similarity = round(similarity, 3)
    return similarity

