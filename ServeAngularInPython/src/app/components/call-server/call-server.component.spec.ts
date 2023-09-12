import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CallServerComponent } from './call-server.component';

describe('CallServerComponent', () => {
  let component: CallServerComponent;
  let fixture: ComponentFixture<CallServerComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ CallServerComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(CallServerComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
