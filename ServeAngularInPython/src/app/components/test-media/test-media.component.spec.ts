import { ComponentFixture, TestBed } from '@angular/core/testing';

import { TestMediaComponent } from './test-media.component';

describe('TestMediaComponent', () => {
  let component: TestMediaComponent;
  let fixture: ComponentFixture<TestMediaComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ TestMediaComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(TestMediaComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
