import { Component, EventEmitter, OnInit, Output } from '@angular/core';
import { SentenceDataService } from 'src/app/services/sentence-data.service';
import { VoiceRecognitionService } from 'src/app/services/voice-recognition.service';

@Component({
  selector: 'app-speech-to-text',
  templateUrl: './speech-to-text.component.html',
  styleUrls: ['./speech-to-text.component.css'],
  providers: [VoiceRecognitionService]
})


export class SpeechToTextComponent implements OnInit {
  @Output() spokenSentence = new EventEmitter<string>();
  txt = ""

  stopVoice: boolean = false;

  constructor(public service: VoiceRecognitionService, private sentenceDataService: SentenceDataService) {
    this.service.init()
  }

  ngOnInit(): void {
  }

  startService() {
    this.service.start()
    this.stopVoice=true;
    
  }

  stopService() {
    this.service.stop()
    this.txt=this.service.text;
    this.stopVoice=false;

  }

  sendSentence() {
    let text = document.querySelector('#txt')?.innerHTML;
    if (text === undefined)
      text = "";
    this.sentenceDataService.sendSentence(text);//.subscribe(response => {
    //  console.log(response);;
    //} );
  }
}
