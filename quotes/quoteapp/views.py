from django.shortcuts import render, redirect, get_object_or_404
from .forms import AuthorForm, QuoteForm
from .models import Author, Quote

# Create your views here.

def main(request):
    quotes = Quote.objects.all()
    return render(request, 'quoteapp/index.html', {'quotes': quotes})

def author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='quoteapp:main')
        else:
            return render(request, 'quoteapp/author.html', {'form': form})

    return render(request, 'quoteapp/author.html', {'form': AuthorForm()})

def quote(request):
    authors = Author.objects.all()

    if request.method == 'POST':
        form = QuoteForm(request.POST)

        # author_id = Author.objects.get(id=request.POST.get('authors'))
        # print(author_id)
        # form.author = author_id

        if form.is_valid():
            form.save()
            return redirect(to='quoteapp:main')
        else:
            # print(form)
            # print(form.errors)

            return render(request, 'quoteapp/quote.html', {'authors': authors, 'form': form})

    return render(request, 'quoteapp/quote.html', {'form': QuoteForm()})

def detail(request, quote_id):
    quote = get_object_or_404(Quote, pk=quote_id)
    return render(request, 'quoteapp/detail.html', {'quote': quote})
