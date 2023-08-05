import { Component } from '@angular/core';
import { TaskService } from '../task.service';

@Component({
  selector: 'app-contact',
  templateUrl: './contact.component.html',
  styleUrls: ['./contact.component.scss'],
})
export class ContactComponent {
  name!: string;
  email!: string;
  message!: string; // Marked as definitely assigned

  constructor(private taskservice: TaskService) {}

  onSubmit() {
    const formData = {
      name: this.name,
      email: this.email,
      message: this.message,
    };
    this.taskservice.sendEmail(formData).subscribe((res) => {
      console.log(res);
      if (res) {
        alert('Email sent successfully');
        this.resetForm();
      } else {
        console.error('Error:', res.error);
        alert('Failed to send email. Please try again later.');
      }
    });
  }

  resetForm() {
    this.name = '';
    this.email = '';
    this.message = '';
  }
}
