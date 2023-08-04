import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { TaskService } from '../task.service';
import { Router } from '@angular/router'; // Import the Router service

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss'],
})
export class LoginComponent {
  loginForm!: FormGroup; // Add the "!" to tell TypeScript it will be initialized in the constructor.
  loginInProgress = false;
  loginSuccess = false;

  constructor(
    private formBuilder: FormBuilder,
    private taskservice: TaskService,
    private router: Router
  ) {}

  ngOnInit() {
    this.initializeForm();
  }

  initializeForm() {
    this.loginForm = this.formBuilder.group({
      email: ['', [Validators.required, Validators.email]],
      password: ['', [Validators.required, Validators.minLength(8)]],
    });
  }

  onSubmit() {
    if (this.loginForm?.valid) {
      const email = this.loginForm.get('email')?.value;
      const password = this.loginForm.get('password')?.value;

      const loginobj = {
        email: email,
        password: password,
      };

      this.loginInProgress = true;
      this.taskservice.login(loginobj).subscribe(
        (res: any) => {
          console.log(res);

          // Simulate 2 seconds delay for the login process
          setTimeout(() => {
            if (res.message == 'Login successful') {
              // Login success
              this.loginSuccess = true;
              localStorage.setItem('uid',res.user_id)
              // Navigate to home page after successful login
              this.router.navigate(['/home']);
            } else {
              // Login failed
              this.loginSuccess = false;
            }
            this.loginInProgress = false;
          }, 2000);

          // alert(res.message);
        },
        (error: any) => {
          // Handle any errors that occurred during the login process
          console.error('Login failed:', error);
          this.loginInProgress = false;
          this.loginSuccess = false;
        }
      );

      console.log('Email:', email);
      console.log('Password:', password);
    }
  }
}
