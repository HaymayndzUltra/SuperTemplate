import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterLink } from '@angular/router';

@Component({
  selector: 'app-not-found',
  standalone: true,
  imports: [CommonModule, RouterLink],
  template: `
    <div class="min-h-screen bg-gray-50 flex flex-col justify-center py-12 sm:px-6 lg:px-8">
      <div class="text-center">
        <h1 class="text-9xl font-bold text-gray-200">404</h1>
        <h2 class="mt-2 text-2xl font-semibold text-gray-900">Page not found</h2>
        <p class="mt-2 text-gray-600">Sorry, we couldn't find the page you're looking for.</p>
        <div class="mt-6">
          <a
            routerLink="/"
            class="inline-flex items-center px-4 py-2 border border-transparent text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
          >
            Go back home
          </a>
        </div>
      </div>
    </div>
  `,
  styles: []
})
export class NotFoundComponent {}