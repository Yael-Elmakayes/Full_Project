import { HttpClient } from '@angular/common/http';
import { Component } from '@angular/core';

@Component({
  selector: 'app-inbar',
  templateUrl: './inbar.component.html',
  styleUrls: ['./inbar.component.css']
})
export class InbarComponent {
  showForm = false;
  name!: string;
  id!: string;
  photos: string[] = [];
  showResult = false;
  resultMessage = '';
  constructor(private http: HttpClient) {}

  showMessage() {
    this.showForm = true;
  }

takePhoto() {
  const video = document.createElement('video');
  const canvas = document.createElement('canvas');
  const ctx = canvas.getContext('2d');
  let count = 0;
  let intervalId: any;

  navigator.mediaDevices.getUserMedia({ video: true }).then((stream) => {
    video.srcObject = stream;
    video.play();
  });

  video.addEventListener('canplay', () => {
    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;

    intervalId = setInterval(() => {
      ctx!.drawImage(video, 0, 0, canvas.width, canvas.height);
      const dataUrl = canvas.toDataURL('image/jpeg');
      console.log('המערך שנכנס עכשיו הוא : ' + count)
      this.photos.push(dataUrl);
      count++;
       if (count >= 10) {
        clearInterval(intervalId);
        video.pause();
        video.srcObject = null;
        this.sendData();
      }
    }, 1000);
  });
}

sendData() {
  const formData = new FormData();
  formData.append('name', this.name);
  formData.append('id', this.id);
  this.photos.forEach((photo, index) => {
    formData.append(`photo${index}`, photo);
  });
  
  // Append the frames array as a JSON string
  formData.append('frames', JSON.stringify(this.photos));
  
  const options = { responseType: 'text' as const };
  
  this.http.post('http://localhost:5000/register', formData, options).subscribe(
    (response: string) => {
      this.resultMessage = response;
      this.showResult = true;
    },
    (error) => {
      console.log(error);
    }
  );
}
}