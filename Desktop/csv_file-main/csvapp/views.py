import csv
import os
from django.conf import settings
from django.shortcuts import render

def search_csv(request):
    query = request.GET.get('q', '').lower()
    results = []

    # CSV ფაილის მდებარეობა
    csv_file = os.path.join(settings.BASE_DIR, 'csvapp/static/csv/words.csv')

    # თუ ველზე რამე შეიყვანეს
    if query:
        with open(csv_file, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                if query in row['bone'].lower():
                    results.append(row)

    return render(request, 'csv_template.html', {'results': results, 'query': query})          
       


def csv_view(request):
    data = []
    file_path = os.path.join(settings.BASE_DIR, 'csvapp/static/csv/words.csv')
    
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data.append(row)

    return render(request, 'csv_template.html', {'data': data})         