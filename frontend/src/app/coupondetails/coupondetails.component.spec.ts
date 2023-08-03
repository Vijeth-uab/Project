import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CoupondetailsComponent } from './coupondetails.component';

describe('CoupondetailsComponent', () => {
  let component: CoupondetailsComponent;
  let fixture: ComponentFixture<CoupondetailsComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [CoupondetailsComponent]
    });
    fixture = TestBed.createComponent(CoupondetailsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
