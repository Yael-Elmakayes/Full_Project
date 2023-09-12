import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Router } from '@angular/router';

@Injectable({
  providedIn: 'root'
})

export class SentenceDataService {
  finalResult: string = "";
  private apiUrl = 'https://localhost:44331/Sentence/';

  constructor(private http: HttpClient, private router: Router) { }
  sendSentence(sentence: string): void {

    let data=new FormData()
    data.append("text",sentence)
    this.http.post<string>(this.apiUrl + "GetSentence/",data ).subscribe(res => {
      this.finalResult = res;
      this.router.navigate(['/results'])
    });


    // getData(spokenSentence: string): Observable<any> {
    //   const url = `${this.apiUrl}?sentence=${encodeURIComponent(spokenSentence)}`;
    //   return this.http.get<any>(url);
  }
}
