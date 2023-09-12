import { HttpClient } from '@angular/common/http';
import { Component, ElementRef, ViewChild } from '@angular/core';


@Component({
  selector: 'app-frame-service',
  templateUrl: './frame-service.component.html',
  styleUrls: ['./frame-service.component.css']
})
export class FrameServiceComponent {

  @ViewChild('videoElement', { static: true }) videoElement!: ElementRef;
  @ViewChild('canvasElement', { static: true }) canvasElement!: ElementRef;
  @ViewChild('processedImageElement', { static: true }) processedImageElement!: ElementRef;

  private socket!: WebSocket;

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
        }, 1000);
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
    this.socket = new WebSocket('ws://localhost:8000');
    this.socket.addEventListener('open', event => {
      console.log('WebSocket connected');
    });
    this.socket.addEventListener('message', event => {
      const jsonData = JSON.parse(event.data);
      const imageSrc = 'data:image/jpeg;base64,' + jsonData.image;
      const image = new Image();
      image.src = imageSrc;
      image.onload = () => {
        // Display the image in the HTML of the component
        const imgContainer = document.getElementById('image-container');
        imgContainer!.appendChild(image);
      };
    });
    this.socket.addEventListener('close', event => {
      console.log('WebSocket disconnected');
    });
  }
}
