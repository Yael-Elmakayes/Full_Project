import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { FlacksComponent } from './components/flacks/flacks.component';
import { SignInComponent } from './components/sign-in/sign-in.component';
import { SignUpComponent } from './components/sign-up/sign-up.component';
import { NavComponent } from './components/nav/nav.component';
import { HomeComponent } from './components/home/home.component';
import { ComponentComponent } from './components/component/component.component';
import { AboutComponent } from './components/about/about.component';
import { SpeechToTextComponent } from './components/speech-to-text/speech-to-text.component';

const routes: Routes =
 [
  {path: 'Flacks', component:FlacksComponent},
 {path: 'SignIn', component:SignInComponent},
 {path: 'SignUp', component:SignUpComponent},
 {path: 'Nav', component:NavComponent},
 {path: 'Home', component:HomeComponent},
 {path: 'Component', component:ComponentComponent},
 {path: 'About', component:AboutComponent},
 {path: 'speech-to-text', component:SpeechToTextComponent},


];//חיבור לקומפוננטה הראשית



@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
