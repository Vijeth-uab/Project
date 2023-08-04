import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AppComponent } from './app.component';
import { TaskListComponent } from './task-list/task-list.component';
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




const routes: Routes = [
  { path: "",pathMatch: 'full', redirectTo: "/login"},
  {path: "home", component: HomeComponent},
  { path: "tasks", component: TaskListComponent },
 // { path: '**', redirectTo: 'tasks' }, // Redirect any unknown route to the tasks component
 { path: "about", component: AboutComponent },
 { path: "contact", component: ContactComponent },
 { path: "addcoupon", component: AddcouponComponent },
 { path: "coupondetails", component: CoupondetailsComponent },
 { path: "mycoupons", component: MycouponsforexchangeComponent },
 { path: "payment", component: PaymentComponent  },
 { path: "tradedcoupons", component: TradedcouponsComponent },
 { path: "login", component: LoginComponent },
 { path: "signup", component: SignupComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
