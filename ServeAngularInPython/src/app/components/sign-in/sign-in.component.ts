import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormControl, FormGroup, Validators } from '@angular/forms';
import { SignIn } from 'src/app/model/SignIn';
import { Router } from '@angular/router';
import { HttpClient } from '@angular/common/http';


@Component({
  selector: 'app-sign-in',
  templateUrl: './sign-in.component.html',
  styleUrls: ['./sign-in.component.css']
})
export class SignInComponent implements OnInit {

  signInForm!: FormGroup;
  message!: string;
  showRegisterButton: boolean = false;

  constructor(private formBuilder: FormBuilder, private http: HttpClient,private router: Router) { }

  ngOnInit(): void {
    this.signInForm = this.formBuilder.group({
      mail: ['', [Validators.required, Validators.email]],
      pass: ['', [Validators.required]]
    });
  }

  onSubmit() {
    // Get form data
    const formData = this.signInForm.value;

    // Send request to server to check user credentials
    this.http.post<any>('http://localhost:5000/login', formData).subscribe(
      response => {
        // Display success message if login was successful
        this.message = response.message;
        // this.signInForm.reset();
   
      },
      error => {
        // Display error message if login was unsuccessful
        this.message = error.error.message;
        
    // Display button to register
        this.showRegisterButton = true;
      }
    );
    
  }



  img ="assets/p.png"
}
