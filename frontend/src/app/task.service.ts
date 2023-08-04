import { Injectable } from '@angular/core';
import { HttpClient ,HttpHeaders} from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class TaskService {
  private backendUrl = 'http://127.0.0.1:5000/api/tasks'; // Update the backend URL
  private baseUrl = 'http://127.0.0.1:5000/api/'; // Update the backend URL
  private headers: HttpHeaders;
  constructor(private http: HttpClient) {

    this.headers = new HttpHeaders({
      'Content-Type': 'application/json',
      'Access-Control-Allow-Credentials':'*'
    });
  }

  getTasks(): Observable<any[]> {
    return this.http.get<any[]>(this.backendUrl, { headers: this.headers });
  }

  addTask(task: string): Observable<any> {
    return this.http.post<any>(this.backendUrl, { task }, { headers: this.headers });
  }

  login(loginobj: any): Observable<any> {
    return this.http.post<any>(this.baseUrl+'login',  loginobj , { headers: this.headers });
  }

  signUp(signupobj: any): Observable<any> {
    return this.http.post<any>(this.baseUrl+'signup',signupobj , { headers: this.headers });
  }
  addUser(user: any): Observable<any> {
    return this.http.post<any>(this.baseUrl, user , { headers: this.headers });
  }
  updateTask(taskId: number, task: string): Observable<any> {
    const url = `${this.backendUrl}/${taskId}`;
    return this.http.put<any>(url, { task }, { headers: this.headers });
  }

  deleteTask(taskId: number): Observable<any> {
    const url = `${this.backendUrl}/${taskId}`;
    return this.http.delete<any>(url);
  }
  getAllCoupons() {
    return this.http.get<any[]>(this.baseUrl + 'getCoupons');
  }
  getCouponsById(couponId: number) {
    const url = `${this.baseUrl}/getCouponsById/${couponId}`;
    return this.http.get<any>(url, { headers: this.headers });
  }
  addCoupon(coupon: any): Observable<any> {
    const options = { 
      headers: this.headers,
      withCredentials: true // Add the withCredentials option here
    };
    return this.http.post<any>(this.baseUrl + 'addCoupons', coupon, options);
  }
  getTradedCoupons(user_id: any): Observable<any> {
    const url = `${this.baseUrl}/getTradedCoupons/${user_id}`;
    return this.http.get<any>(url);
  }

  postTradedCoupons(tradedCoupon: any): Observable<any> {
    const options = { 
      headers: this.headers,
      withCredentials: true // Add the withCredentials option here
    };
    return this.http.post<any>(this.baseUrl + 'postTradedCoupons', tradedCoupon, options);
  }
 
  addTransaction(transaction: any): Observable<any> {
    return this.http.post<any>(this.baseUrl+'tradedCoupons',  transaction , { headers: this.headers });
  }
}
