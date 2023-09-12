import { Component, ViewChild, ElementRef } from '@angular/core';
import { HttpClient } from '@angular/common/http';
@Component({
  selector: 'app-python',
  templateUrl: './python.component.html',
  styleUrls: ['./python.component.css']
})
export class PythonComponent {
  @ViewChild('videoElement') videoElement: ElementRef | undefined;
  private video: HTMLVideoElement | undefined;
  private stream: MediaStream | undefined;
  private frames: ImageData[] = [];

  constructor(private http: HttpClient) {}
   //הפעלת הצלמה
  startCamera() {
    this.video = this.videoElement?.nativeElement;
    if (!this.video) {
      console.error('Video element not found');
      return;
    }
    navigator.mediaDevices.getUserMedia({ video: true })
      .then(stream => {
        this.stream = stream;
        this.video!.srcObject = stream;
        this.video!.play();
        setInterval(() => {
          this.captureFrame();
        }, 1000);
      })
      .catch(err => console.error(err));
  }

//סגירת המצלמה
  stopCamera() {
    if (this.stream) {
      this.stream.getTracks().forEach(track => track.stop());
      this.video!.srcObject = null;
      this.video = undefined;
      this.stream = undefined;
      this.frames = [];
    }
  }

//לכידת פריים בודד מהסירטון
  captureFrame() {
    if (!this.video) {
      console.error('Video element not found');
      return;
    }
    const canvas = document.createElement('canvas');
    // מגדירים את הרוחב והגובה של הקנבס כך שיתאימו לרוחב ולגובה של הזרם הווידאו.
    canvas.width = this.video.videoWidth;
    canvas.height = this.video.videoHeight;
    //לקבל את ההקשר לציור 2D של הקנבס באמצעות השיטה getContext().
    const ctx = canvas.getContext('2d');
    // מציירים את המסגרת הנוכחית של הזרם הווידאו על הקנבס באמצעות השיטה drawImage().
    ctx!.drawImage(this.video, 0, 0, canvas.width, canvas.height);
    // לקבל את התמונה מהקנבס באמצעות השיטה getImageData().
    const imageData = ctx!.getImageData(0, 0, canvas.width, canvas.height);
    //הכנסת התמונה למערך
    this.frames.push(imageData);
    if (this.frames.length === 30) {//ברגע שהמערך מלא והגענו ל30 פרימים   נרצה לשלוח אותם לשרת פיתון
      this.sendFrames();
    }
  }
//שליחת 30 הפרימים שנלכדו לשרת פיתון לצורך עיבוד
  sendFrames() {
    const url = 'http://localhost:5000/predict';
    const body = { frames: this.frames };
    this.http.post(url, body).subscribe(
      res => console.log(res),
      err => console.error(err)
    );
    this.frames = [];
  }






}
