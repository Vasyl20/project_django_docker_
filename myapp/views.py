from django.shortcuts import render
from django.db import connection

def add_code_snippet(request):
    if request.method == "POST":
        code = request.POST.get('code')
        address = request.POST.get('address')
        link = request.POST.get('link')
        CodeSnippet.objects.create(code=code, address=address, link=link)  # Виправлено посилання на модель CodeSnippet
    return render(request, 'add_code_snippet.html')


def view_code_snippets(request):
    search_query = request.GET.get('query', '')
    rows = []
    if search_query:
        with connection.cursor() as cursor:
            # Небезпечний SQL-запит, вразливий до SQL-ін'єкції
            query = f"SELECT id, code, created_at, address, link FROM myapp_codesnippet WHERE code = '{search_query}'"
            cursor.execute(query)
            rows = cursor.fetchall()
    return render(request, 'view_code_snippets.html', {'rows': rows, 'search_query': search_query})