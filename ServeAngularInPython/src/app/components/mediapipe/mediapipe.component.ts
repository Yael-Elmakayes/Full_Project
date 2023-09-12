import { HttpClient } from '@angular/common/http';
import { Component } from '@angular/core';

@Component({
  selector: 'app-mediapipe',
  templateUrl: './mediapipe.component.html',
  styleUrls: ['./mediapipe.component.css']
})
export class MediapipeComponent {
  processedImage: string | undefined;

  constructor(private http: HttpClient) { }

  onFileSelected(event:any): void {
    const file: File = event.target.files[0];
    const reader = new FileReader();
    reader.readAsDataURL(file);
    reader.onload = () => {
      const base64Image = reader.result!.toString().split(',')[1];
      this.sendImageToServer(base64Image);
    };
  }

  sendImageToServer(base64Image: string): void {
    this.http.post('http://localhost:5000/process_image', { image: base64Image })
      .subscribe((response: any) => {
        this.processedImage = response.processed_image;
      });
  }
}
