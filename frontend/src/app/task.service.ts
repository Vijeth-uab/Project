import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class TaskService {
  private backendUrl = 'http://localhost:5000/api/tasks'; // Update the backend URL

  constructor(private http: HttpClient) { }

  getTasks(): Observable<any[]> {
    return this.http.get<any[]>(this.backendUrl);
  }

  addTask(task: string): Observable<any> {
    return this.http.post<any>(this.backendUrl, { task });
  }

  updateTask(taskId: number, task: string): Observable<any> {
    const url = `${this.backendUrl}/${taskId}`;
    return this.http.put<any>(url, { task });
  }

  deleteTask(taskId: number): Observable<any> {
    const url = `${this.backendUrl}/${taskId}`;
    return this.http.delete<any>(url);
  }
}
