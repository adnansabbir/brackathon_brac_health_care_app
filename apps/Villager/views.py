from django.http import HttpResponseRedirect
from django.shortcuts import render
from apps.Villager.forms import VillagerForm, RemarkForm, VillagerNextFollowUpForm
import django.contrib.messages as messages
from django.urls import reverse
from apps.Villager.models import Villager, Remark
from django.db.models import Q
from datetime import datetime


def villager_create(request):
    # Create Villager
    if request.method == 'GET':
        data = {
            'villager_form': VillagerForm()
        }
        return render(request, 'Villager/create.html', data)

    # Create Villager
    if request.method == 'POST':
        villager_form = VillagerForm(request.POST, request.FILES)
        if villager_form.is_valid():
            villager_form.save()

            messages.success(request, 'Form submission successful')
            return HttpResponseRedirect(reverse('villager:villager_create'))

        else:
            data = {
                'villager_form': villager_form
            }
            return render(request, 'Villager/create.html', data)


def villager_search(request):
    # Villager Search Menu

    # If any search input, search vbillager with that id
    search_query = request.GET.get('search_query') or ''

    if search_query:
        try:
            villager = Villager.objects.get(
                Q(reg_no__icontains=search_query)
            )
            return HttpResponseRedirect(reverse('villager:villager_profile', kwargs={'reg_no': villager.reg_no}))
            # go to villagers profile
        except Villager.DoesNotExist:
            messages.warning(request, "No Villager with this Reg No found")

    data = {
        'search_query': search_query
    }
    return render(request, 'Villager/search.html', data)


def villager_profile(request, reg_no):
    if request.method == "GET":
        villager = Villager.objects.get(reg_no=reg_no)
        villager_form = VillagerNextFollowUpForm(instance=villager)
        remark_form = RemarkForm()

        data = {
            'villager': villager,
            'villager_form': villager_form,
            'remark_form': remark_form,
            'last_remark': Remark.objects.filter(villager=villager).first()
        }
        return render(request, 'Villager/profile.html', data)

    if request.method == "POST":
        villager = Villager.objects.get(reg_no=reg_no)
        villager_form = VillagerNextFollowUpForm(request.POST, instance=villager)
        remark_form = RemarkForm(request.POST)

        if villager_form.is_valid() and remark_form.is_valid():
            villager_form.save()
            villager.follow_up_date = datetime.today()
            villager.save()

            remark = remark_form.save(commit=False)
            remark.villager = villager
            remark.save()

            messages.success(request, "Update Successful")

            return HttpResponseRedirect(reverse('villager:villager_profile', kwargs={'reg_no': villager.reg_no}))
