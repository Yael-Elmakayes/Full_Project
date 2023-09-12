import { HttpClient } from '@angular/common/http';
import { Component } from '@angular/core';

@Component({
  selector: 'app-update-name',
  templateUrl: './update-name.component.html',
  styleUrls: ['./update-name.component.css']
})
export class UpdateNameComponent {
  firstName!: string;
  lastName!: string;
  phone!: string;
  email!: string;
  password!: string;

  constructor(private http: HttpClient) {}

  addUser() {
    const user = {
      firstName: this.firstName,
      lastName: this.lastName,
      phone: this.phone,
      email: this.email,
      password: this.password
    };
    this.http.post('http://localhost:5000/users', user).subscribe(
      (response) => {
        console.log(response);
      },
      (error) => {
        console.log(error);
      }
    );
  }
}
