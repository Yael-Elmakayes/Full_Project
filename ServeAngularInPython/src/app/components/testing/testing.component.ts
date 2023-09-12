import { HttpClient } from '@angular/common/http';
import { Component, ElementRef, ViewChild } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';

@Component({
  selector: 'app-testing',
  templateUrl: './testing.component.html',
  styleUrls: ['./testing.component.css']
})
export class TestingComponent {
  employee = {
    name: '',
    idCard: ''
  };
  showCamera = false;
  registrationSuccess = false;
  processedPhotoUrl!: string;

  constructor(private http: HttpClient) {}

  openCamera() {
    this.showCamera = true;
    const video = document.getElementById('video') as HTMLVideoElement;
    navigator.mediaDevices.getUserMedia({ video: true })
      .then(stream => {
        video.srcObject = stream;
        video.play();
      })
      .catch(error => {
        console.log(error);
      });
  }

  onSubmit() {
    const canvas = document.getElementById('canvas') as HTMLCanvasElement;
    const context = canvas.getContext('2d');
    const video = document.getElementById('video') as HTMLVideoElement;
    context!.drawImage(video, 0, 0, 320, 240);
    const photo = canvas.toDataURL();
    this.showCamera = false;
    const stream = video.srcObject as MediaStream; // get the MediaStream object from the video element
    const tracks = stream.getVideoTracks(); // get the video tracks from the MediaStream object
    tracks[0].stop(); // stop the video tracks and close the camera
  
    const formData = new FormData();
    formData.append('name', this.employee.name);
    formData.append('idCard', this.employee.idCard);
    formData.append('photo', photo);
  
    this.http.post<any>('http://localhost:5000/process-photo', formData).subscribe(response => {
      const bytes = atob(response.photo);
      const array = new Uint8Array(bytes.length);
      for (let i = 0; i < bytes.length; i++) {
        array[i] = bytes.charCodeAt(i);
      }
      const blob = new Blob([array], { type: 'image/jpeg' });
      this.processedPhotoUrl = URL.createObjectURL(blob);
      this.registrationSuccess = true;
      setTimeout(() => {
        this.registrationSuccess = false;
      }, 1000); // 5000 milliseconds = 5 seconds
    }, error  => {
      console.log(error);
    });
  }
}
