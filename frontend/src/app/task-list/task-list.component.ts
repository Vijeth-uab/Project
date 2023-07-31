import { Component, OnInit } from '@angular/core';
import { TaskService } from '../task.service';

@Component({
  selector: 'app-task-list',
  templateUrl: './task-list.component.html',
  styleUrls: ['./task-list.component.scss']
})
export class TaskListComponent implements OnInit {
  tasks: any[] = [];
  newTask: string = '';

  constructor(private taskService: TaskService) { }

  ngOnInit(): void {
    this.fetchTasks();
  }

  fetchTasks(): void {
    this.taskService.getTasks().subscribe(tasks => {
      this.tasks = tasks;
    });
  }

  addTask(): void {
    if (this.newTask.trim()) {
      this.taskService.addTask(this.newTask).subscribe(() => {
        this.fetchTasks();
        this.newTask = ''; // Clear the input after adding the task
      });
    }
  }

  updateTask(task: any): void {
    const newTask = prompt('Edit task:', task.task);
    if (newTask !== null) {
      this.taskService.updateTask(task.id, newTask).subscribe(() => {
        this.fetchTasks();
      });
    }
  }

  deleteTask(task: any): void {
    if (confirm('Are you sure you want to delete this task?')) {
      this.taskService.deleteTask(task.id).subscribe(() => {
        this.fetchTasks();
      });
    }
  }
}
