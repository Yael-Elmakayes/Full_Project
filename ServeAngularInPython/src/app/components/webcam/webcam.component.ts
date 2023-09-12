import { HttpClient } from '@angular/common/http';
import { Component } from '@angular/core';
import { Observable } from 'rxjs';

// המבנה הזה בעצם יכיל לי את התוצאות שחוזרות מהמודל כלומר את המילה או  האות שחוזרת מהמודל
interface PredictionResponse {

  result: string;

}

@Component({
  selector: 'app-webcam',
  templateUrl: './webcam.component.html',
  styleUrls: ['./webcam.component.css']
})
export class WebcamComponent {
  video: any;
  canvas: any;
  context: any;
  frames: any[] = [];
  result!: string;

  constructor(private http: HttpClient) { }

  ngOnInit() {
    this.video = document.getElementById('video');
    this.canvas = document.getElementById('canvas');
    this.context = this.canvas.getContext('2d');
    this.startCamera();
    setInterval(() => {
      this.captureFrame();
    }, 500);
  }
//מפעיל את המצלמה 
  startCamera() {
    navigator.mediaDevices.getUserMedia({ video: true })
      .then(stream => {
        this.video.srcObject = stream;
        this.video.play();
      })
      .catch(error => console.log(error));
  }
//מכבה את המצלמה
  stopCamera() {
    this.video.pause();
    this.video.srcObject = null;
  }
//תפיסת הפריים ושליחתו  לעיבוד בשרת
  captureFrame() {
    this.context.drawImage(this.video, 0, 0, this.canvas.width, this.canvas.height);
    let dataUrl = this.canvas.toDataURL('image/jpeg');//הכנסת ניתוב של הפריים לתוך משתנה
    //פה נצטרך לשנות ולשלוח כל פריים לכמה עיבודים נוספים לפני דחיפתו למערך הגדול
    // this.frames.push(dataUrl);//מכניס את הפריים למערך הגדול שאותו נרצה בסוף לשלוח למודל
    // this.sendFramesOPENCV(dataUrl)//שליחת הפריים הבודד לעיבוד מקדים לפני ההכנסה למערך

    this.sendFramesOPENCV(dataUrl).subscribe(response => {
      this.frames = this.frames.concat(response); // Do something with the response
    });

    if (this.frames.length == 30) {
      // this.sendFrames();
      //הפונקציה שתשלח לשרת פיתון שיבצע הכנסה למודל
      this.result='tee'
    }
  }


  // captureFram(): void {
  //   this.context.drawImage(this.video, 0, 0, this.canvas.width, this.canvas.height);
  //   let dataUrl = this.canvas.toDataURL('image/jpeg');
  //   this.sendFramesOPENCV(dataUrl).subscribe(response => {
  //     this.frames = this.frames.concat(response); // Do something with the response
  //   });
  //   setTimeout(() => {
  //     this.captureFrame();
  //   }, 500);
  // }



//מהפונקציה הזו חוזר לי מערך שלם של כל ציוני הדרך של אותו הפרים ואת המערך הזה אני ישרשר למערך שיכיל את כל מערכי המערכים של 30 הפריימים
// פונקציה שהולכת לשלוח את הפריים לעיבוד ראשונה בשרת פיתון
//פונקציה זו הולכת לממש קריאה של מתודה post
sendFramesOPENCV(input: string): Observable<string[]>//הפונקציה מקבלת נתיב של הפריים כמחרוזת 'i.jpg'
{
  let url = 'http://localhost:5000/python_process';//השם של השרת שאליו אני שולחת את התמונה
  let data = input;//מכיל את הנתונים שישלחו לשרת
  // קריאה לשרת
  return this.http.post<string[]>(url, data);//  captureFrame()  מחזיר מערך לפונקציה   
  //אני רוצה שהשרת יחזיר תשובה שתחזור לפונקציה שקראה לה
}


  // sendFramesOPENCV(_data: any) {
  //   let url = 'http://localhost:5000/pre';
  //   this.http.post(url, _data).subscribe(response => {
  //     let predictionResponse = response as PredictionResponse;
  //     this.result = predictionResponse.result;
  //   });
    
  // }

  //שליחת  המערך הגדול לשרת   להכנסת אל המודל
  sendFrames() {
    let url = 'http://localhost:5000/predict';
    let data = { frames: this.frames };
    this.http.post(url, data).subscribe(response => {
      let predictionResponse = response as PredictionResponse;
      this.result = predictionResponse.result;
    });
    this.frames = [];
  }
}
