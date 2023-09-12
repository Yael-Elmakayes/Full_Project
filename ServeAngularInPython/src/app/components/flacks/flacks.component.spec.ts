import { ComponentFixture, TestBed } from '@angular/core/testing';

import { FlacksComponent } from './flacks.component';

describe('FlacksComponent', () => {
  let component: FlacksComponent;
  let fixture: ComponentFixture<FlacksComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ FlacksComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(FlacksComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
