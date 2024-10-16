# from django.views.generic import ListView
# from .models import py5test
# # Create your views here.
# class py5test(ListView):
#     model = py5test
#     template_name = 'index.html'


from django.shortcuts import render
from django.db import connection


def vulnerable_search(request):
    query = request.GET.get('q', '')
    raw_query = f"SELECT * FROM myapp_py5test WHERE name = '{query}'"

    with connection.cursor() as cursor:
        cursor.execute(raw_query)
        rows = cursor.fetchall()

    # 템플릿에 결과 전달
    context = {
        'rows': rows,
        'query': query,
    }
    return render(request, 'index.html', context)