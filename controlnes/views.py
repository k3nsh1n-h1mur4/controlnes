from django.shortcuts import render, HttpResponseRedirect, redirect
from django.http import HttpRequest
from django.views.decorators.http import require_http_methods

from getConnection import getCnx 

from psycopg.rows import dict_row


def index(request):
    return render(request, 'index.html', {'title': 'Index'})


def list(request):
    title = 'Listado General'
    if request.method == 'GET':
        cnx = getCnx()
        cur = cnx.cursor(row_factory=dict_row)
        cur.execute('SELECT * FROM propuestastbl;')
        ctx = cur.fetchall()
        cnx.commit()
        cur.close()
        cnx.close()
    return render(request, 'list.html', {'ctx': ctx, 'title': title})
        

@require_http_methods(['GET', 'POST'])
def delete(request, id):
    title = 'Eliminar Registro'
    id = id
    print(request.body)
    print(type(id))
    print(id)
    if request.method == 'POST':
        cnx = getCnx()
        cur = cnx.cursor(row_factory=dict_row)
        cur.execute("DELETE FROM propuestastbl WHERE id = %s;", (id,))
        cnx.commit()
        cur.close()
        cnx.close()
    return redirect('list')
