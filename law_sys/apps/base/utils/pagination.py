"""
Pagination utils
"""

__author__ = "Saish Naik"
__copyright__ = "Copyright 2024, SN"

from rest_framework.pagination import (
    PageNumberPagination,
)


class StandardPagination(PageNumberPagination):
    """Standard pagination"""

    page_size_query_param = "page_size"
    page_query_param = "page"
    page_size = 10
    max_page_size = 1000

    def __init__(self, request):
        self.request = request

    def get_paginated_response(self, data):
        """Get paginated response"""
        return {
            "next": self.get_next_link(),
            "previous": self.get_previous_link(),
            "count": self.page.paginator.count,
            "total_pages": self.page.paginator.num_pages,
            "current_page": self.page.number,
            "results": data,
        }

    def paginate(self, queryset, serializer_class, context=None):
        """Paginate"""
        page = self.paginate_queryset(queryset, self.request)
        if page is not None:
            serializer = serializer_class(
                page, many=True, context=context or {}
            )
            return self.get_paginated_response(serializer.data)
        serializer = serializer_class(
            queryset, many=True, context=context or {}
        )
        return self.get_paginated_response(serializer.data)
