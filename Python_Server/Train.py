from Python_Libraries import *

# # נתיב עבור נתונים מיוצאים, מערכים numpy
DATA_PATH = os.path.join("Data")
# # פעולות שאנו מנסים לזהות
labels = np.array(['Help', 'Father', 'M','i'])
# # נתונים בשווי מאה סרטונים
num_video = 100
# # אורך הסרטונים יהיה 30 פריימים
frame_len = 30
label_map = {label:num for num, label in enumerate(labels)}
print(label_map)

sequences, words = [], []  # יוצרים שני מערכים רצפים ותווים
#X -- מייצג רצפים
#Y -- מייצג תוויות
for label in labels: # עובר על כל תווית == מילה או אות
    print("data to open" ,DATA_PATH, " " , label)
    for seq in np.array(os.listdir(os.path.join(DATA_PATH, label))).astype(int):# פותח את התקיה של המילה או האות שבתוכה נמאים 100 תקיות
        # print(label, seq)
        window = []
        for frame_num in range(frame_len):#אורך הסרטונים שהוא 30 פריימים במקביל עובר על כל פריים בתוך תקייה של תנועה
            res = np.load(os.path.join(DATA_PATH, label, str(seq), "{}.npy".format(frame_num)))# numpy  לתוך משתנה res וטוען את הקובץ
            window.append(res) # מכניס לתוך מערך החלונות את מערך הnumpy של אותו הפריים
        sequences.append(window)#  של רצפיםברגע שסיים להכניס אתכל הקבצים של הnumpy דוחף את כל המערך הגדול של אותו הסרטון למערך
        words.append(label_map[label])# ודוחף למערך המילים את המילה שסיימנו לעבוד איתה

X = np.array(sequences)# ממיר את המערך של הרצפים למערך numpy ומכניס אותו לX-
#One hot encoding and train-test split
y = to_categorical(words).astype(int)# מעביר פה למטריצה
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)#נאחסן את כל הנתונים במערך אחד X שיהיה יותר קל לעבוד איתו


model = Sequential()   # המודול
#activation='relu'-- זוהי הפונקציה שהולכת לעבוד על השכבות
# הוספת 3 שכבות של LSTM
model.add(LSTM(64, return_sequences=True, activation='tanh', input_shape=(30, 258)))#הקלט שמקבל המודל שלי
model.add(LSTM(128, return_sequences=True, activation='tanh'))
model.add(LSTM(64, return_sequences=False, activation='tanh'))
model.add(Dense(64, activation='tanh'))
model.add(Dense(32, activation='tanh'))
model.add(Dense(labels.shape[0], activation='softmax'))




model.compile(optimizer='Adam', loss='categorical_crossentropy', metrics=['categorical_accuracy'])
print(model.summary())


cp_best_val_loss = ModelCheckpoint(
      "SLD_val_loss", monitor='val_loss', mode = 'min', save_weights_only=True, save_best_only=True, verbose=1
)
cp_best_val_acc = ModelCheckpoint(
      "SLD_val_acc", monitor='val_categorical_accuracy', mode = 'max', save_weights_only=True, save_best_only=True, verbose=1
)



model.fit(X_train, y_train, epochs=170, validation_data = (X_test, y_test), callbacks = [cp_best_val_loss, cp_best_val_acc])
model_json = model.to_json()

with open("model.json", "w") as json_file:
    json_file.write(model_json)

model.save_weights('model.h5')

