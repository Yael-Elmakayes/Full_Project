import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule } from '@angular/forms'; // import the FormsModule
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { CallToServerService } from './services/call-to-server.service';
import { CallServerComponent } from './components/call-server/call-server.component';
import { ReactiveFormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import { CameraComponent } from './components/camera/camera.component';
import { WebcamComponent } from './components/webcam/webcam.component';
import { PythonComponent } from './components/python/python.component';
import { TestComponent } from './components/test/test.component';
import { MediapipeComponent } from './components/mediapipe/mediapipe.component';
import { TestMediaComponent } from './components/test-media/test-media.component';
import { FrameServiceComponent } from './components/frame-service/frame-service.component';
import { FlacksComponent } from './components/flacks/flacks.component';
import { TestingComponent } from './components/testing/testing.component';
import { HomeComponent } from './components/home/home.component';
import { RouterModule, Routes } from '@angular/router';
import { SignInComponent } from './components/sign-in/sign-in.component';
import { SignUpComponent } from './components/sign-up/sign-up.component';
import { NavComponent } from './components/nav/nav.component';
import { NoopAnimationsModule } from '@angular/platform-browser/animations';
import { InbarComponent } from './components/inbar/inbar.component';
import { ComponentComponent } from './components/component/component.component';
import { AboutComponent } from './components/about/about.component';
import { AoudioComponent } from './components/aoudio/aoudio.component';
import { SpeechToTextComponent } from './components/speech-to-text/speech-to-text.component';
import { UpdateNameComponent } from './components/update-name/update-name.component';


const routes: Routes = [
  { path: 'flacks', component: FlacksComponent }
];
@NgModule({
  exports: [RouterModule],
  declarations: [
    AppComponent,
    CallServerComponent,
    PythonComponent,
    CameraComponent,
    WebcamComponent,
    TestComponent,
    MediapipeComponent,
    TestMediaComponent,
    FrameServiceComponent,
    FlacksComponent,
    TestingComponent,
    HomeComponent,
    SignInComponent,
    SignUpComponent,
    NavComponent,
    SpeechToTextComponent,
    InbarComponent,
    ComponentComponent,
    AboutComponent,
    AoudioComponent,
    UpdateNameComponent,
  ],
  imports: [
    RouterModule.forRoot(routes),
    BrowserModule,
    ReactiveFormsModule,
    AppRoutingModule,
    FormsModule,
    // להריץ קריאות ברשת
    HttpClientModule,
    NoopAnimationsModule,
  ],
  providers: [CallToServerService],
  bootstrap: [AppComponent]
})
export class AppModule { }
