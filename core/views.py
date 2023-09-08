from django.shortcuts import render
from django_htmx.middleware import HtmxDetails
from django.http import HttpRequest, HttpResponse
from django.core.paginator import Paginator
from dataclasses import dataclass
from faker import Faker
from django.views.decorators.http import require_http_methods, require_GET, require_POST
# Create your views here.

@dataclass
class Person:
    id: int
    name: str


faker = Faker()
people = [Person(id=i, name=faker.name()) for i in range(1, 235)]

class HtmxHttpRequest(HttpRequest):
    htmx: HtmxDetails


@require_GET
def home(request: HtmxHttpRequest) -> HttpResponse:
    page_num = request.GET.get("page", "1")
    page = Paginator(object_list=people, per_page=10).get_page(page_num)
    return render(request, "home.html", {"persons": page})