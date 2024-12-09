from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.views.generic import ListView

from .models import Notifications, Card
from .forms import NotificationForm

# Create your views here.


class PurchaseView(View):
    def get(self, request, card_id):
        form = NotificationForm()
        card = Card.objects.get(id=card_id)
        return render(request, 'notifications/purchase-card.html', {'form': form, 'card': card})

    def post(self, request, card_id):
        form = NotificationForm(request.POST)
        if form.is_valid():
            user = request.user
            profile = user.profile

            if not profile.phone_number or not profile.address or not profile.first_name or not profile.last_name:
                messages.error(request, "Please add personal information to your profile to complete this request.")
                return redirect('index')

            notification = form.save(commit=False)
            notification.sender = user
            notification.receiver = Card.objects.get(id=card_id).owner
            notification.card = Card.objects.get(id=card_id)
            notification.title = (f"A buyer has arrived! "
                                  f"{user.profile.first_name} {user.profile.last_name} wants to buy your card.")
            notification.content = (f"Contacts: Phone number: {user.profile.phone_number} "
                                    f"Address: {user.profile.address}")
            notification.save()
            messages.success(request, "Request is successfully sent.")
            return redirect('index')
        card = Card.objects.get(id=card_id)
        return render(request, 'notifications/purchase-card.html', {'form': form, 'card': card})

    class PurchaseView(View):
        def get(self, request, card_id):
            form = NotificationForm()
            card = Card.objects.get(id=card_id)
            return render(request, 'notifications/purchase-card.html', {'form': form, 'card': card})

        def post(self, request, card_id):
            form = NotificationForm(request.POST)
            if form.is_valid():
                user = request.user
                profile = user.profile

                if not profile.phone_number or not profile.address or not profile.first_name or not profile.last_name:
                    messages.error(request, "Please add personal information to your profile to complete this request.")
                    return redirect('index')
                card_title = Card.objects.get(id=card_id).title
                price = Card.objects.get(id=card_id).price
                notification = form.save(commit=False)
                notification.sender = user
                notification.receiver = Card.objects.get(id=card_id).owner
                notification.card = Card.objects.get(id=card_id)
                notification.title = (f"A buyer has arrived! "
                                      f"{user.profile.first_name} {user.profile.last_name} "
                                      f"wants to buy {card_title} for {price}$.")
                notification.content = (f"Contacts: Phone number: {user.profile.phone_number} "
                                        f"Address: {user.profile.address}")
                notification.save()
                messages.success(request, "Request is successfully sent.")
                return redirect('index')
            card = Card.objects.get(id=card_id)
            return render(request, 'notifications/purchase-card.html', {'form': form, 'card': card})


class NegotiationView(View):
    def get(self, request, card_id):
        form = NotificationForm()
        card = Card.objects.get(id=card_id)
        return render(request, 'notifications/negotiate-card.html', {'form': form, 'card': card})

    def post(self, request, card_id):
        form = NotificationForm(request.POST)
        if form.is_valid():
            user = request.user
            profile = user.profile

            if not profile.phone_number or not profile.first_name or not profile.last_name:
                messages.error(request, "Please add number and name to your profile to complete this request.")
                return redirect('index')
            card_title = Card.objects.get(id=card_id).title
            card_price = Card.objects.get(id=card_id).price
            notification = form.save(commit=False)
            notification.sender = user
            notification.receiver = Card.objects.get(id=card_id).owner
            notification.card = Card.objects.get(id=card_id)
            notification.title = f"{user.profile.first_name} {user.profile.last_name} wants to negotiate your card."
            notification.content = (f"Call {user.profile.phone_number} to negotiate "
                                    f"about {card_title} with price {card_price}$.")
            notification.save()
            messages.success(request, "Request is successfully sent.")
            return redirect('index')
        card = Card.objects.get(id=card_id)
        return render(request, 'notifications/negotiate-card.html', {'form': form, 'card': card})


class UserNotificationsView(LoginRequiredMixin, ListView):
    model = Notifications
    template_name = 'notifications/my-notifications.html'
    context_object_name = 'notifications'
    paginate_by = 5

    def get_queryset(self):
        return Notifications.objects.filter(receiver=self.request.user, is_archived=False).order_by('-date')
