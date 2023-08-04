import { Component } from '@angular/core';
import { TaskService } from '../task.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss'],
})
export class HomeComponent {
  title = 'AllCouponz';
  SelectedData: any = {};
  CouponsGrid: any = [];

  constructor(private taskservice: TaskService) {}

  ngOnInit() {
    this.getcoupon();
  }

  getcoupon() {
    this.taskservice.getAllCoupons().subscribe((resp) => {
      if (resp && resp.length) {
        this.CouponsGrid = resp;
        console.log("------",this.CouponsGrid)
      } else {
        console.log("No Data Found");
      }
    });
  }
}
