from idlelib.debugobj import dispatch
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db.models import Avg
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DetailView, FormView
from .forms import ReviewCreateForm
from .models import Books, Reviews, Category


class BookListView(ListView):
    model = Books
    categories = Category.objects.all()
    queryset = Books.objects.all()
    context_object_name = 'books'
    last_books = Books.objects.filter(availability='On sale').order_by('-average_rating')[:10]
    featured_books = Books.objects.filter(average_rating__gte=4, average_rating__lte=5,
                                          availability='On sale').order_by('-average_rating')[:4]
    extra_context = {
        'last_books': last_books,
        'featured_books': featured_books,
        'categories': categories,
    }
    template_name = 'index.html'


@method_decorator(login_required, name='dispatch')
class BookDetailView(FormView, DetailView):
    model = Books
    template_name = 'book_detail.html'
    context_object_name = 'book'
    form_class = ReviewCreateForm
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book = self.object
        context['categories'] = book.category.all()
        context['reviews'] = Reviews.objects.filter(book=book).order_by('-created_at')
        return context
    def form_valid(self, form):
        book = self.get_object()
        review = form.save(commit=False)
        review.book = book
        review.user = self.request.user
        review.save()
        return HttpResponseRedirect(self.request.path_info)

    def get_success_url(self):
        return reverse('books-detail', kwargs={'pk': self.object.pk})


class AllBookListView(ListView):
    model = Books
    context_object_name = 'books'
    template_name = 'all_books.html'
    categories = Category.objects.all()
    extra_context = {
        'categories': categories,
    }
