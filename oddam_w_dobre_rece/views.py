from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from oddam_w_dobre_rece.models import Donation, Institution
class LandingPage(View):
    def get(self, request):
        total_bags = Donation.objects.all().count()
        total_organizations = Institution.objects.all().count()
        return render(request, 'landing_page.html', {'total_bags': total_bags, 'total_organizations': total_organizations})

class AddDonation(View):
    def get(self, request):
        return render(request, 'add_donation.html')

    def post(self, request):
        # Przetwarzanie danych z formularza i zapis do bazy danych
        return HttpResponse("Dziękujemy za dodanie daru!")
class Login(View):
    def get(self, request):
        return render(request, 'login.html')

class Register(View):
    def get(self, request):
        return render(request, 'register.html')


# Create your views here.
class FormView(View):
    def get(self, request):
        # Tutaj możesz umieścić kod obsługujący żądanie GET dla widoku formularza
        return render(request, 'form.html')  # Zwracamy odpowiedni szablon dla formularza

    def post(self, request):
        # Tutaj możesz umieścić kod obsługujący żądanie POST dla widoku formularza
        # Np. pobranie danych przekazanych przez formularz i zapisanie ich w bazie danych
        return render(request, 'form.html')  # Zwracamy odpowiedni szablon dla formularza (np. ten sam, lub inny po potwierdzeniu przesłania danych)