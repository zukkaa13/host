import csv
import os
from django.conf import settings
from django.shortcuts import render
from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt

def search_csv(request):
    query = request.GET.get('q', '').lower()
    results = []

    csv_file = os.path.join(settings.BASE_DIR, 'csvapp/static/csv/words.csv')

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


@csrf_exempt
def add_word(request):
    if request.method == 'POST':
        word = request.POST.get('word')
        level = request.POST.get('level')

        if not word or not level:
            return JsonResponse({'error': 'სიტყვა და დონე აუცილებელია'}, status=400)

        csv_file = os.path.join(settings.BASE_DIR, 'csvapp/static/csv/words.csv')

        file_exists = os.path.isfile(csv_file)

        with open(csv_file, 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            if not file_exists or os.stat(csv_file).st_size == 0:
                # თუ ფაილი ახალია ან ცარიელია, ჰედერი ჩასვით
                writer.writerow(['bone', 'level'])
            writer.writerow([word, level])

        return JsonResponse({'success': True, 'word': word, 'level': level})

    return HttpResponseBadRequest('POST მეთოდი აუცილებელია')
