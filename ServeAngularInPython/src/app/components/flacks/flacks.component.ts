import { HttpClient } from '@angular/common/http';
import { Component, ElementRef, ViewChild } from '@angular/core';
@Component({
  selector: 'app-flacks',
  templateUrl: './flacks.component.html',
  styleUrls: ['./flacks.component.css']
})
export class FlacksComponent {

  @ViewChild('videoElement', { static: true }) videoElement!: ElementRef;
  @ViewChild('canvasElement', { static: true }) canvasElement!: ElementRef;
  @ViewChild('processedImageElement', { static: true }) processedImageElement!: ElementRef;
  frames: number[][] = [];
  
  count : number  = 0;
  private socket!: WebSocket;
  predictions: string[] = [];
  p : number[]=[]
  prediction!:'';


  ngOnInit() {
    this.startCamera();
    this.setupWebSocket();
  }

  startCamera() {
    if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
      navigator.mediaDevices.getUserMedia({ video: true }).then(stream => {
        this.videoElement.nativeElement.srcObject = stream;
        this.videoElement.nativeElement.play();
        setInterval(() => {
          this.captureFrame();
        }, 1000/30);
      });
    }
  }

  captureFrame() {
    const context = this.canvasElement.nativeElement.getContext('2d');
    context.drawImage(this.videoElement.nativeElement, 0, 0, this.canvasElement.nativeElement.width, this.canvasElement.nativeElement.height);
    const imageData = this.canvasElement.nativeElement.toDataURL('image/jpeg');
    
    this.sendFrame(imageData);
  }

  sendFrame(imageData: string) {//מחרוזת נתוני התמונה שיש לשלוח לשרת
    if (this.socket.readyState === WebSocket.OPEN) {//בדיקת החיבור לפני שליחת נתונים
      this.socket.send(JSON.stringify({ image: imageData }));
    }
    
  }

setupWebSocket() {

  const RECONNECT_INTERVAL = 5000;
  let reconnectTimeout:any;
  const connectWebSocket = () => {
    this.socket = new WebSocket('ws://localhost:8000');
    this.socket.addEventListener('open', event => {
      console.log('WebSocket connected');
    });
    this.socket.addEventListener('message', event => {
      const jsonData = JSON.parse(event.data);
      this.count++;
      if (this.count <= 30) {
        console.log("  מספר הפריים שנדחף כעת למערך  " + "  " + this.count);
        const numberArray = Array.from(jsonData);
        this.frames.push(numberArray as number[]);
        this.frames = this.frames.slice(-30)
        let rows = this.frames.length;
        let cols = this.frames[0].length;
        console.log("Dimensions: " + rows + " x " + cols);
      } else {
        this.count = 0;
        console.log("   המערך התמלא ב - 30 פריימים וכעת הוא עובד לשרת פיתון לצורך חיזוי ");
        const url = 'http://localhost:5000/process_frames';
        const data = { frames: this.frames };
        fetch(url, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(data)
        }).then(response => {
          if (response.ok) {
            return response.json();
          }
          throw new Error('Network response was not ok.');
        }).then(data => {
          console.log(data);
          if (this.predictions.length == 0)
           {
            this.predictions.push(data['prediction']);
           }
           else
            if (this.predictions[this.predictions.length - 1] != data['prediction']) 
            {
            this.predictions.push(data['prediction']);
            }

        }).catch(error => {
          console.error(error);
        });
      }
    });
    this.socket.addEventListener('close', event => {
      clearTimeout(reconnectTimeout);
      reconnectTimeout = setTimeout(connectWebSocket, RECONNECT_INTERVAL);
    });
  };

  connectWebSocket();
}
}