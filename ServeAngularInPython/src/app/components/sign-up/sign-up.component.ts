import { Component, OnInit } from '@angular/core';
import { FormControl, FormGroup, Validators } from '@angular/forms';
import { SignUp } from 'src/app/model/SignUp';
import { Router } from '@angular/router';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-sign-up',
  templateUrl: './sign-up.component.html',
  styleUrls: ['./sign-up.component.css']
})
export class SignUpComponent implements OnInit {
  im ="assets/p.png"
  signUpForm!: FormGroup;

  constructor(private http: HttpClient, private router: Router) { }

  ngOnInit(): void {
    this.signUpForm = new FormGroup({
      firstName: new FormControl('', [Validators.required]),
      lastName: new FormControl('', [Validators.required]),
      email: new FormControl('', [Validators.required, Validators.email]),
      phone: new FormControl('', [Validators.required]),
      pass: new FormControl('', [Validators.required]),
    });
  }

  onSubmit() {
    const data = {
      firstName: this.signUpForm.value.firstName,
      lastName: this.signUpForm.value.lastName,
      email: this.signUpForm.value.email,
      phone: this.signUpForm.value.phone,
      pass: this.signUpForm.value.pass
    };
    
    this.http.post('http://localhost:5000/add-user', data).subscribe({
      next: () => {
        console.log('User added successfully');
        //לאחר שנשלחת בהצלחה לשרת תנקה את הטופס
        this.signUpForm.reset();
        
      },
      error: (error) => {
        console.error('Error adding user', error);
      }
    });
  }
}

