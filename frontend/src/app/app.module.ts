import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';
import { FormsModule } from '@angular/forms'; // Import FormsModule




import { AppComponent } from './app.component';
import { TaskListComponent } from './task-list/task-list.component';
import { AppRoutingModule } from './app-routing.module';
import { AboutComponent } from './about/about.component';
import { ContactComponent } from './contact/contact.component';
import { AddcouponComponent } from './addcoupon/addcoupon.component';
import { CoupondetailsComponent } from './coupondetails/coupondetails.component';
import { MycouponsforexchangeComponent } from './mycouponsforexchange/mycouponsforexchange.component';
import { PaymentComponent } from './payment/payment.component';
import { TradedcouponsComponent } from './tradedcoupons/tradedcoupons.component';
import { LoginComponent } from './login/login.component';
import { SignupComponent } from './signup/signup.component';
import { HomeComponent } from './home/home.component';

@NgModule({
  declarations: [
    AppComponent,
    TaskListComponent,
    AboutComponent,
    ContactComponent,
    AddcouponComponent,
    CoupondetailsComponent,
    MycouponsforexchangeComponent,
    PaymentComponent,
    TradedcouponsComponent,
    LoginComponent,
    SignupComponent,
    HomeComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    AppRoutingModule,
    FormsModule // Add FormsModule here
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
