import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AddcouponComponent } from './addcoupon.component';

describe('AddcouponComponent', () => {
  let component: AddcouponComponent;
  let fixture: ComponentFixture<AddcouponComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [AddcouponComponent]
    });
    fixture = TestBed.createComponent(AddcouponComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
