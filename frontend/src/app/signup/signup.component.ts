import { Component } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { TaskService } from '../task.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-signup',
  templateUrl: './signup.component.html',
  styleUrls: ['./signup.component.scss']
})
export class SignupComponent {
  signUpForm!: FormGroup;

  constructor(private formBuilder: FormBuilder,private taskservice:TaskService,private router: Router) { }

  ngOnInit() {
    this.initializeForm();
  }

  initializeForm() {
    this.signUpForm = this.formBuilder.group({
      first_name: ['', [Validators.required, Validators.maxLength(50)]],
      last_name: ['', [Validators.required, Validators.maxLength(50)]],
      email: ['', [Validators.required, Validators.email]],
      password: ['', [Validators.required, Validators.minLength(8)]],
      confirm_password: ['', Validators.required],
      phone: ['', [Validators.required, Validators.pattern(/^\d{10}$/)]]
    }, { validators: this.passwordMatchValidator });
  }

  passwordMatchValidator(formGroup: FormGroup) {
    const passwordControl = formGroup.get('password');
    const confirmPasswordControl = formGroup.get('confirm_password');

    if (passwordControl && confirmPasswordControl) {
      const password = passwordControl.value;
      const confirmPassword = confirmPasswordControl.value;
      return password === confirmPassword ? null : { passwordsMismatch: true };
    }

    return null; // Default return for null form controls
  }

  onSubmit() {
    console.log("onSubmit is working----------")
    if (this.signUpForm.valid) {
      var userobj = {
        "firstname": this.signUpForm.get('first_name')?.value,
        "lastname": this.signUpForm.get('last_name')?.value,
        "phonenumber": this.signUpForm.get('phone')?.value,
        "email": this.signUpForm.get('email')?.value,
        "password": this.signUpForm.get('password')?.value,
        "confirmpassword": this.signUpForm.get('confirm_password')?.value
      };
      
      this.taskservice.signUp(userobj).subscribe((res) => {
        console.log(res)
        // alert(res);
        this.router.navigate(['/login']);
      });
      console.log(this.signUpForm.value);
    }
  }
}