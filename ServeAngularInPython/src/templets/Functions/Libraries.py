import mediapipe as mp # ספריה לראיה ממוחשבת  לצורך זיהוי פנים וידיים
import numpy as np # עבודה על מערכים קריטי ללמידת מכונה
import cv2 # ספריית קוד פתוח לזיהוי פנים ועיבוד תמונה
#מודל הולסטי      Mediapipe Holistic הוא אחד מהצינורות המכילים רכיבי פנים, ידיים ותנוחה
mp_holistic = mp.solutions.holistic
#כלי עזר לציור
mp_drawing = mp.solutions.drawing_utils
