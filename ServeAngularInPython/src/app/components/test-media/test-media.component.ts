import { Component } from '@angular/core';
import { WebSocketService } from './web-socket.service';

@Component({
  selector: 'app-test-media',
  templateUrl: './test-media.component.html',
  styleUrls: ['./test-media.component.css']
})
export class TestMediaComponent {

  public arrnum:number[] = [1,2,1,2];//מערך גלובלי של מספרים,
  
  public num!: number;//משתנה שיכנס לפה הקלט של המשתמש
  public array!: number[];//המערך הסופי

  constructor(private webSocketService: WebSocketService) {}
//שולחת למחלקה ששלוחת מה לשלוח לה
  public sendNumber() {
    //his.webSocketService.sendNumber(this.num): זה קורא לשיטת sendNumber של האובייקט webSocketService (שהוא מסוג WebSocketService) ומעביר את הערך של המאפיין num כארגומנט.

    this.webSocketService.sendNumber(this.num).subscribe((array: number[]) => {//המערך חוזר לפה
      this.array = this.arrnum.concat(array);
      // this.array.concat(this.arrnum)
      console.log('Received array:', array);
    });
  }





}
