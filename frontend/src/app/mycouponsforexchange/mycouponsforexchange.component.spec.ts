import { ComponentFixture, TestBed } from '@angular/core/testing';

import { MycouponsforexchangeComponent } from './mycouponsforexchange.component';

describe('MycouponsforexchangeComponent', () => {
  let component: MycouponsforexchangeComponent;
  let fixture: ComponentFixture<MycouponsforexchangeComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [MycouponsforexchangeComponent]
    });
    fixture = TestBed.createComponent(MycouponsforexchangeComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
