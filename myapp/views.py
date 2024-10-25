from django.shortcuts import render
from django.db import connection


def myapp_search(request):
    query = request.POST.get('search', '')
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

