class ContentQuerySet(models.QuerySet):
    def search(self, query=None):
        if query is None or query == "":
            return self.none()
        params_list = query.split(',')
        lookups = Q(name__icontains=query) | Q(year__icontains=query) | Q(color__icontains=query) | Q(type__name__icontains=query)

        # for all queries in the query set repeat the following line to filter the results that fulfill the criteria

        q = query.objects.filter(color__icontains="Blue")
        q = q.filter(year__icontains='2003')
        return q


class ContentManager(models.Manager):
    def get_queryset(self):
        return ContentQuerySet(self.model, using=self._db)

    def search(self, query=None):
        return self.get_queryset().search(query=query)

