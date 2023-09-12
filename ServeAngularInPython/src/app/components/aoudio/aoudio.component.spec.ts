import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AoudioComponent } from './aoudio.component';

describe('AoudioComponent', () => {
  let component: AoudioComponent;
  let fixture: ComponentFixture<AoudioComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ AoudioComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(AoudioComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
