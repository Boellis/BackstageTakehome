from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils.timezone import now
from .models import RequestStat
from .utils import calculate_difference
from .serializers import DifferenceSerializer
from typing import Any

class DifferenceView(APIView):
    def get(self, request: Any) -> Response:
        try:
            n: int = int(request.GET.get("number", ""))
            if not (1 <= n <= 100):
                raise ValueError()
        except (ValueError, TypeError):
            return Response(
                {"error": "Number must be an integer between 1 and 100."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        stat, _ = RequestStat.objects.get_or_create(number=n)
        stat.occurrences += 1
        stat.save()

        response_data = {
            "datetime": now(),
            "value": calculate_difference(n),
            "number": n,
            "occurrences": stat.occurrences,
            "last_datetime": stat.last_requested,
        }

        serializer = DifferenceSerializer(response_data)
        return Response(serializer.data)
