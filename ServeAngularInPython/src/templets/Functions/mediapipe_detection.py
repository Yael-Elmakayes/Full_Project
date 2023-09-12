from Libraries import*



def Mp_detection(img, mp_holistic):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # המרת צבע BGR 2 RGB
    img.flags.writeable = False# תמונה כבר לא ניתנת לכתיבה
    res = mp_holistic.process(img)# בצע תחזית
    img.flags.writeable = True  # התמונה ניתנת לכתיבה
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)# כיסוי צבע RGB 2 BGR
    return img, res
