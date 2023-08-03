import { ComponentFixture, TestBed } from '@angular/core/testing';

import { TradedcouponsComponent } from './tradedcoupons.component';

describe('TradedcouponsComponent', () => {
  let component: TradedcouponsComponent;
  let fixture: ComponentFixture<TradedcouponsComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [TradedcouponsComponent]
    });
    fixture = TestBed.createComponent(TradedcouponsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
