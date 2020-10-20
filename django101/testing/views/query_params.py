from django.shortcuts import render


def query_params_view(request):
    q = request.GET.get('q')
    pages = request.GET.get('filter', '')

    context = {
        'grid_params': {
            'current_page': 0,
            'pages_count': 15,
            'filter': '',
            'order_by': '',
        },
        'q': q,
        'pages': pages
    }

    return render(request, 'testing/query_params.html', context)
