import { Component } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { TaskService } from '../task.service';
import { Router } from '@angular/router'; // Import the Router service

interface Coupon {
  uid:string;
  title: string;
  description: string;
  expiryDate: string;
  type: string;
}
@Component({
  selector: 'app-addcoupon',
  templateUrl: './addcoupon.component.html',
  styleUrls: ['./addcoupon.component.scss'],
})
export class AddcouponComponent {
  
  couponForm!: FormGroup; // Use 'undefined' initialization
  coupon: Coupon = {
    uid:'',
    title: '',
    description: '',
    expiryDate: '',
    type: 'discount',
  };
  constructor(private fb: FormBuilder, private taskservice: TaskService, private router: Router) {}

  ngOnInit() {
    this.createCouponForm();
  }

  createCouponForm() {
    this.couponForm = this.fb.group({
      title: ['', Validators.required],
      description: ['', Validators.required],
      expiryDate: ['', Validators.required],
      type: ['discount', Validators.required]
    });
  }

  get formControls() {
    return this.couponForm.controls;
  }

  addCoupon() {
    if (this.couponForm.invalid) {
      console.error('Please fill all the required fields.');
      return;
    }

    this.coupon = this.couponForm.value;

    var obj = {
      couponName: this.coupon.title,
      couponDescription: this.coupon.description,
      couponType: this.coupon.type,
      couponImage: '',
      couponExpiry: this.coupon.expiryDate,
      userId:localStorage.getItem('uid')
    };
    // You can further customize your validation logic here if needed.

    // Get the form values and assign them to the coupon object
   

    // Display the values in the console
    console.log('Title:');
    console.log('Description:', this.coupon.description);
    console.log('Expiry Date:', this.coupon.expiryDate);
    console.log('Coupon Type:', this.coupon.type);
    this.router.navigate(['/home']);
    this.taskservice.addCoupon(obj).subscribe((res) => {
      console.log(res);
    });
    // For sending data to the server using HTTP service, you can call a service method here to save the data to a database, for example:
    // this.couponService.saveCoupon(this.coupon).subscribe(response => {
    //   console.log('Coupon saved successfully:', response);
    // }, error => {
    //   console.error('Error while saving coupon:', error);
    // });
  }
}
