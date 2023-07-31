import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss'],
})
export class AppComponent {
  title = 'AllCouponz';
  SelectedData: any = {};
  CouponsGrid = [
    {
      name: 'Clothing Coupon 1',
      image_url: 'https://example.com/clothing_coupon1.jpg',
      discount: '20% off',
      description: 'Get 20% off on all clothing items',
      expiry_date: '2023-08-15',
    },
    {
      name: 'Food Coupon 1',
      image_url: 'https://example.com/food_coupon1.jpg',
      discount: '$5 off',
      description: 'Save $5 on your next food order',
      expiry_date: '2023-07-31',
    },
    {
      name: 'Footwear Coupon 1',
      image_url: 'https://example.com/footwear_coupon1.jpg',
      discount: '15% off',
      description: 'Enjoy 15% off on footwear collection',
      expiry_date: '2023-09-05',
    },
    {
      name: 'Clothing Coupon 2',
      image_url: 'https://example.com/clothing_coupon2.jpg',
      discount: 'Buy 1 Get 1 Free',
      description: 'Buy one clothing item and get another for free',
      expiry_date: '2023-08-20',
    },
    {
      name: 'Food Coupon 2',
      image_url: 'https://example.com/food_coupon2.jpg',
      discount: '50% off',
      description: 'Get 50% off on your favorite meal',
      expiry_date: '2023-07-15',
    },
    {
      name: 'Footwear Coupon 2',
      image_url: 'https://example.com/footwear_coupon2.jpg',
      discount: '$10 off',
      description: 'Save $10 on any footwear purchase',
      expiry_date: '2023-09-10',
    },
    {
      name: 'Clothing Coupon 3',
      image_url: 'https://example.com/clothing_coupon3.jpg',
      discount: '25% off',
      description: 'Get 25% off on all clothing items',
      expiry_date: '2023-08-25',
    },
    {
      name: 'Food Coupon 3',
      image_url: 'https://example.com/food_coupon3.jpg',
      discount: 'Free Delivery',
      description: 'Enjoy free delivery on your next food order',
      expiry_date: '2023-07-31',
    },
    {
      name: 'Footwear Coupon 3',
      image_url: 'https://example.com/footwear_coupon3.jpg',
      discount: '20% off',
      description: 'Save 20% on any footwear purchase',
      expiry_date: '2023-09-15',
    },
    {
      name: 'Clothing Coupon 4',
      image_url: 'https://example.com/clothing_coupon4.jpg',
      discount: '$15 off',
      description: 'Save $15 on your next clothing purchase',
      expiry_date: '2023-08-31',
    },
    {
      name: 'Food Coupon 4',
      image_url: 'https://example.com/food_coupon4.jpg',
      discount: '10% off',
      description: 'Get 10% off on your favorite meal',
      expiry_date: '2023-07-25',
    },
    {
      name: 'Footwear Coupon 4',
      image_url: 'https://example.com/footwear_coupon4.jpg',
      discount: 'Buy 2 Get 1 Free',
      description: 'Buy two footwear items and get another for free',
      expiry_date: '2023-09-20',
    },
    {
      name: 'Clothing Coupon 5',
      image_url: 'https://example.com/clothing_coupon5.jpg',
      discount: '30% off',
      description: 'Get 30% off on all clothing items',
      expiry_date: '2023-08-15',
    },
    {
      name: 'Food Coupon 5',
      image_url: 'https://example.com/food_coupon5.jpg',
      discount: '$7 off',
      description: 'Save $7 on your next food order',
      expiry_date: '2023-07-31',
    },
    {
      name: 'Footwear Coupon 5',
      image_url: 'https://example.com/footwear_coupon5.jpg',
      discount: '10% off',
      description: 'Enjoy 10% off on footwear collection',
      expiry_date: '2023-09-05',
    },
    {
      name: 'Clothing Coupon 6',
      image_url: 'https://example.com/clothing_coupon6.jpg',
      discount: 'Buy 2 Get 1 Free',
      description: 'Buy two clothing items and get another for free',
      expiry_date: '2023-08-20',
    },
  ];
}
