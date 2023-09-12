import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class CallToServerService {

  constructor(private http: HttpClient) { }


// הפונקציה שכשאני לוחצת עליה היא מדפיסה לי את הקלט ששלחתי לה
  checkUser(user: string): Observable<any> {//מקבלת את הuserName
    const url = 'http://localhost:5000/api/greeting';//  כל פעם נשנה אותו לפי הפונקציה החדשה ואני יגיד לו באיזה דף לפתוח אותה,הניתוב
    const data = { username: user };
    return this.http.post<any>(url, data);//מחזירה למי שקרא לה את הפלט
  }
 

}
