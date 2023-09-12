import mediapipe as mp # ספריה לראיה ממוחשבת  לצורך זיהוי פנים וידיים
import numpy as np # עבודה על מערכים קריטי ללמידת מכונה
import cv2 # ספריית קוד פתוח לזיהוי פנים ועיבוד תמונה
import pandas as pd # עבודה על קבצים קריאה כתיבה וכו
import os# מאפשר ליצור אינטראקציה עם מספר פונקציות של מערכת ההפעלה
from sklearn.model_selection import train_test_split #   אלגורתמים + משמש לבניית מודלים של למידת מכונה
from keras.utils import to_categorical # משמש ללמידה עמוקה ולבניית השכבות במודלים
from scipy import stats # היא ספריית קוד פתוח המשמשת לפתרון בעיות מתמטיות, מדעיות, הנדסיות וטכניות
from matplotlib import pyplot as plt # היא ספרייה מקיפה ליצירת הדמיות סטטיות
from keras.models import Sequential
from keras.layers import LSTM, Dense
from keras.callbacks import TensorBoard
from keras.callbacks import ModelCheckpoint
from keras.models import model_from_json
#מודל הולסטי      Mediapipe Holistic הוא אחד מהצינורות המכילים רכיבי פנים, ידיים ותנוחה
Holistic = mp.solutions.holistic
#כלי עזר לציור
Drawing = mp.solutions.drawing_utils
