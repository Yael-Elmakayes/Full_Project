import { ComponentFixture, TestBed } from '@angular/core/testing';

import { FrameServiceComponent } from './frame-service.component';

describe('FrameServiceComponent', () => {
  let component: FrameServiceComponent;
  let fixture: ComponentFixture<FrameServiceComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ FrameServiceComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(FrameServiceComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
