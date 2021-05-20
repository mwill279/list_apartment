from django.shortcuts import render
from django.http import HttpResponse
from selenium import webdriver
from .realtorPage import RealtorPage

features = ".//div[@id='load-more-features']/div/div/ul"

# Create your views here.

def search_bar(request):
    return render(request, "search.html")

def results(request):
    browser = webdriver.Chrome()
    apartment = request.POST["url"]
    page = RealtorPage(driver=browser, url=apartment)
    page.go()
    
    return render(request, "result.html", {
        "link": apartment,
        "name": page.name().text(),
        "studio": page.rentals(page.format_plan()),
        "1_plan": page.rentals(page.format_plan(plan='1')),
        "2_plan": page.rentals(page.format_plan(plan='2')),
        "3_plan": page.rentals(page.format_plan(plan ='3')),
        "address": page.format_address(),
        "result_comm": page.comm_features(features),
        "result_unit": page.unit_features(features),
        "desc": page.description().text(),
    })