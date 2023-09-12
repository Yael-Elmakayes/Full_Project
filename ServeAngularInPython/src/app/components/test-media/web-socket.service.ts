
import { Injectable } from '@angular/core';
import { webSocket, WebSocketSubject } from 'rxjs/webSocket';

@Injectable({
  providedIn: 'root'
})
export class WebSocketService {
  private socket$: WebSocketSubject<any>;//any - יכול לקבל כל סוג של נתונים

  constructor() {
    this.socket$ = webSocket('ws://localhost:8000'); // replace with your server URL
  }
// פה מוגדרת המחלקה ששולחת לשרת
//וכן מטפלת בחזרת המערך מהשרת
  public sendNumber(num: number) {
    this.socket$.next(num);//הערך המוחזר מוקצה למאפיין socket$.
    return this.socket$.asObservable();
  }
}