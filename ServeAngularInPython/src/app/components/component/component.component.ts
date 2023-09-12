import { Component } from '@angular/core';
import { Router } from '@angular/router';


@Component({
  selector: 'app-component',
  templateUrl: './component.component.html',
  styleUrls: ['./component.component.css']
})
export class ComponentComponent {

  constructor(private router: Router) { }
  onStart() {
    this.router.navigate(['/flacks']);
  }
  img ="assets/j.png"
  // sigin() {
  //   this.router.navigate(['/sign-in']);
  // }
}
