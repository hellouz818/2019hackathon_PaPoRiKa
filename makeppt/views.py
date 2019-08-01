from django.shortcuts import render
import csv
from django.http import HttpResponse


def ppt(request):
    response = HttpResponse(content_type='text/ppt')
    response['Content-Disposition'] = 'attachment; filename="hello.ppt"'
    
    writer = csv.writer(response)
    writer.writerow(['First row','\n','\tFoo', 'Bar', 'Baz'])
    writer.writerow(['Second row', 'A', 'B', 'C', 'Testing', 'Here\'s a quote'])

    return response