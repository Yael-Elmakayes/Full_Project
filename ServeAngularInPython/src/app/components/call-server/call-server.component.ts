import { Component } from '@angular/core';
import { CallToServerService } from 'src/app/services/call-to-server.service';

@Component({
  selector: 'app-call-server',
  templateUrl: './call-server.component.html',
  styleUrls: ['./call-server.component.css']
})
export class CallServerComponent  {
userName=''
msg='';


constructor(private callToServer:CallToServerService){}

checkUser(){//הפונקציה בעת הלחיצה על הכפתור

  // subscribe (res=>{מה לעשות עם מה שחזר})- כשחוזר הערך- תעשה איתו משהו
 this.callToServer.checkUser(this.userName).subscribe(res=>{this.msg=res.message});//לפה חוזר הערך והוא מכניס אותו למשתנה ואז שולח בחזרה ומציג על המסך
}
}
