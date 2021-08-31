from django.shortcuts import render
from book.forms import PostSearchForm
from book.models import Book
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank, SearchHeadline
from django.contrib.postgres.search import TrigramSimilarity, TrigramDistance
# from django.db.models.functions import Lower

# Create your views here.
# def post_search(request):
#     return render(request, 'index.html')


# CharField.register_lookup(Lower)


def post_search(request):
  form = PostSearchForm

  results = []

  if 'q' in request.GET:
    form = PostSearchForm(request.GET)
    if form.is_valid():
      q = form.cleaned_data['q']
      # search headlines
    query = SearchQuery(q)
    vector = SearchVector('authors')
    results = Book.objects.annotate(search=vector, headline=SearchHeadline('authors', query, start_sel='<span>', stop_sel='</span>', )).filter(search=query)  
      
      ### case sensitive seach
    #   results = Book.objects.filter(title__contains=q)
    #   print(Book.objects.filter(title__contains=q).explain(analyze=True))
      ### HERE we are using icontains which means that we can search the data this is case insensitive
    #   results = Book.objects.filter(title__icontains=q)
      
      ## full text search
    #   results = Book.objects.filter(title__search=q)

      # Search Vector
    #   vector = SearchVector('title')
    #   query = SearchQuery(q)
    #   results = Book.objects.annotate(rank=SearchRank(vector, query)).order_by('-rank')

    # search Ranking
    #   vector = SearchVector('title', weight='A') + SearchVector('authors', weight='B')
    #   query = SearchQuery(q)
    #   results = Book.objects.annotate(rank=SearchRank(vector, query, cover_density=True)).order_by('-rank')
    
    # trigram similarity
    # results = Book.objects.annotate(similarity=TrigramSimilarity('title', q),).filter(similarity__gte=0.1).order_by('-similarity')
    # results = Book.objects.annotate(similarity=TrigramSimilarity('title', q),).filter(similarity__gte=0.3).order_by('-similarity')
    # results = Book.objects.annotate(distance=TrigramDistance('title', q),).filter(distance__lte=0.8).order_by('distance')


    ## search headlines
    #   query = SearchQuery(q)
    #   vector = SearchVector('authors')
    #   results = Book.objects.annotate(search=vector, headline=SearchHeadline('authors', query, start_sel='<span>', stop_sel='</span>', )).filter(search=query)
  return render(request, 'index.html', {'form':form, 'results':results})
#    return render(request, 'index.html', {'form':form, 'results':results, 'q': q})