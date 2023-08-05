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
        this.CouponsGrid.forEach((element: any)=> {
        //  element['img']='assets/lorem.jpg'
          if(element.couponType=='food'){
            element['img']='assets/food.jpeg'
          } else if(element.couponType=='clothing'){
            element['img']='assets/clothing.png'
          }else if(element.couponType=='electronics'){
            element['img']='assets/lorem.jpg'
          }else if(element.couponType=='other'){
            element['img']='assets/macys.png'
          }

        });
        console.log("------",this.CouponsGrid)
      } else {
        console.log("No Data Found");
      }
    });
  }
}
