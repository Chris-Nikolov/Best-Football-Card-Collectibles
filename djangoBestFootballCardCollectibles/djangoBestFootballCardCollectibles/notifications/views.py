from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.views.generic import ListView, TemplateView

from .models import Notifications, Card
from .forms import NotificationForm

# Create your views here.


class PurchaseView(LoginRequiredMixin, View):
    def get(self, request, card_id):
        form = NotificationForm()
        card = Card.objects.get(id=card_id)
        return render(request, 'notifications/purchase-card.html', {'form': form, 'card': card})

    def post(self, request, card_id):
        form = NotificationForm(request.POST)
        if form.is_valid():
            user = request.user
            profile = user.profile
            card = Card.objects.get(id=card_id)

            if not profile.phone_number or not profile.address or not profile.first_name or not profile.last_name:
                messages.error(request, "Please add personal information to your profile to complete this request.")
                return redirect('index')

            if not card.is_approved:
                messages.error(request, "This card is not approved.")
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


class NegotiationView(LoginRequiredMixin, View):
    def get(self, request, card_id):
        form = NotificationForm()
        card = Card.objects.get(id=card_id)
        return render(request, 'notifications/negotiate-card.html', {'form': form, 'card': card})

    def post(self, request, card_id):
        form = NotificationForm(request.POST)
        if form.is_valid():
            user = request.user
            profile = user.profile
            card = Card.objects.get(id=card_id)

            if not profile.phone_number or not profile.first_name or not profile.last_name:
                messages.error(request, "Please add number and name to your profile to complete this request.")
                return redirect('index')

            if not card.is_approved:
                messages.error(request, "This card is not approved.")
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


class UserArchiveView(LoginRequiredMixin, ListView):
    model = Notifications
    template_name = 'notifications/my-archive.html'
    context_object_name = 'notifications'
    paginate_by = 5

    def get_queryset(self):
        return Notifications.objects.filter(receiver=self.request.user, is_archived=True)


class ArchiveNotificationView(LoginRequiredMixin, View):
    def post(self, request, n_id):
        notification = Notifications.objects.get(id=n_id, receiver=request.user)
        notification.is_archived = True
        notification.save()
        return redirect('my_notifications')


class ReturnNotificationView(LoginRequiredMixin, View):
    def post(self, request, n_id):
        notification = Notifications.objects.get(id=n_id, receiver=request.user)
        notification.is_archived = False
        notification.save()
        return redirect('my_archive')


@login_required
def get_unread_notifications(request):
    unread_notifications = Notifications.objects.filter(receiver=request.user, is_archived=False).count()
    return JsonResponse({'unread_notifications': unread_notifications})
