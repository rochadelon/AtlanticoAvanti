"""
Módulo centralizado para importações comuns usadas no projeto.
Este arquivo facilita a consistência de importações em todo o código.
"""

# Importações do sistema e manipulação de arquivos
import os
import time
from pathlib import Path
from tqdm import tqdm

# Processamento de imagens e visualização
import cv2
from PIL import Image
from scipy.ndimage import rotate, zoom

# Bibliotecas de análise de dados
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from IPython.display import display, Markdown as md

# Utilidades de segurança e hashing
import hashlib

# TensorFlow e suas utilidades
import tensorflow as tf
from tensorflow.keras import layers, models, utils, Sequential
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.utils import Sequence
from tensorflow.keras.applications import MobileNetV2

# Métricas e avaliação
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
