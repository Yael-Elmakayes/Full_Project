import { ComponentFixture, TestBed } from '@angular/core/testing';

import { InbarComponent } from './inbar.component';

describe('InbarComponent', () => {
  let component: InbarComponent;
  let fixture: ComponentFixture<InbarComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ InbarComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(InbarComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
