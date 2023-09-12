from Example_holistic_model import *
from Example_drawing_landmarks import *
from Example_key_points import *

def main():
    while True:
        print("תפריט דוגמאות")
        print('תקיש 1 כדי לראות דוגמא של המודל ההוליסטי')
        print('תקיש 2 כדי לראות ציור חיבורים')
        print('תקיש 3 כדי לראות את מערך ציוני הדרך')
        print('תקיש 4 כדי לצאת מהתפריט')

        try:  # במקרה והמשתמש הזין קלט לא חוקי כמו רווח
            choice = int(input())
        except ValueError:
            print("Invalid input. Please enter an integer.")
            continue  # ask for input again
        if choice > 3 or choice < 1:
            print('Please select a valid choice')
        if choice == 1:
            res = holistic_model()
            print(res, "כך נראה מודל הוליסטי")
            if res.right_hand_landmarks is not None:
                print("רשימה של", len(res.right_hand_landmarks.landmark), "ציוני דרך ביד ימין")
            else:
                print("יד ימין לא נמצאה בחלון המצלמה")
            if res.left_hand_landmarks is not None:
                print("רשימה של", len(res.left_hand_landmarks.landmark), "ציוני דרך ביד שמאל")
            else:
                print("יד שמאל לא נמצאה בחלון המצלמה")
            if res.face_landmarks is not None:
                print("רשימה של", len(res.face_landmarks.landmark), "ציוני דרך בפנים")
            else:
                print("הפנים לא נמצאו בחלון המצלמה")
            if res.pose_landmarks is not None:
                print("רשימה של", len(res.pose_landmarks.landmark), "ציוני דרך תנוחות הגוף")
            else:
                print("תנוחות הגוף לא נמצאו בחלון המצלמה")
            print("********************************************")
        elif choice == 2:
            Drowing()
        elif choice == 3:
             Example_key_points(res)
        elif choice == 4:
            print('You opted to exit!')
            break
        cv2.destroyAllWindows()
main()