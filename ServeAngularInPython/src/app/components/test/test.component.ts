import { HttpClient } from '@angular/common/http';
import { Component  } from '@angular/core';


interface ImageResponse {
  processedImage: string;
}
@Component({
  selector: 'app-test',
  templateUrl: './test.component.html',
})
export class TestComponent {
  imageUrl: string | undefined;
  fileToUpload: File = new File([], '');

  constructor(private http: HttpClient) { }

  onFileSelected(event: any) {
    this.fileToUpload = event.target.files[0];

  }

  onUpload() {
    const formData = new FormData();
    formData.append('image', this.fileToUpload, this.fileToUpload.name);

    this.http.post<any>('http://localhost:5000/process_image', formData).subscribe(
      (res) => {
        this.imageUrl = 'data:image/jpeg;base64,' + res.image;
      },
      (err) => {
        console.log(err);
      }
    );
  }
}


