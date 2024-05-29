from django.shortcuts import render
from django.db import connection
from django.views.decorators.csrf import csrf_protect
# from django_ratelimit.decorators import ratelimit  # type: ignore


def add_code_snippet(request):
    if request.method == "POST":
        code = request.POST.get('code')
        address = request.POST.get('address')
        link = request.POST.get('link')
        CodeSnippet.objects.create(code=code, address=address, link=link) 
    return render(request, 'add_code_snippet.html')


# @ratelimit(key='ip', rate='10/m', method='GET')
@csrf_protect
def view_code_snippets(request):
    search_query = request.GET.get('query', '')
    rows = []
    if search_query:
        with connection.cursor() as cursor:
            query = "SELECT id, code, created_at, address, link FROM myapp_codesnippet WHERE code = %s"
            cursor.execute(query, [search_query])
            rows = cursor.fetchall()
    return render(request, 'view_code_snippets.html', {'rows': rows, 'search_query': search_query})

