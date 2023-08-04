import { Component } from '@angular/core';
import { TaskService } from '../task.service';

@Component({
  selector: 'app-tradedcoupons',
  templateUrl: './tradedcoupons.component.html',
  styleUrls: ['./tradedcoupons.component.scss']
})
export class TradedcouponsComponent {
  tradedCoupons: any = [];

  constructor(private taskservice: TaskService) {}

  ngOnInit() {
    this.gettradedcoupon();
  }

  gettradedcoupon() {
    var id=localStorage.getItem('uid')
    this.taskservice.getTradedCoupons(id).subscribe((resp) => {
      if (resp && resp.length) {
        this.tradedCoupons = resp;
        console.log("------",this.tradedCoupons)
      } else {
        console.log("No Data Found");
      }
    });
  }
}