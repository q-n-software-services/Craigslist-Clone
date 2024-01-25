def search_result(request):
    query = request.GET.get('q')
    qs = Content.objects.distinct().search(query=query)

    page = request.GET.get('page', 1)
    pagination = Paginator(qs, CONTENTS_PER_PAGE)

    try:
        qs = pagination.page(page)
    except PageNotAnInteger:
        qs = pagination.page(CONTENTS_PER_PAGE)
    except EmptyPage:
        qs = pagination.page(pagination.num_pages)

    context = {
    'SearchResults': qs,
    'query': str(query),
    }

    return render(request, 'home/search_result.html', context)

