from django import forms

from .models import Offer, Topic


class CreateOfferForm(forms.Form):
    title = forms.CharField(max_length=255)
    description = forms.CharField(widget=forms.Textarea)
    price = forms.DecimalField(max_digits=10, decimal_places=2, min_value=0)
    image = forms.ImageField(required=False)
    start_date = forms.DateTimeField()
    end_date = forms.DateTimeField()
    topic = forms.UUIDField()
    location = forms.CharField(max_length=255)

    def create(self, user):
        title = self.cleaned_data['title']
        description = self.cleaned_data['description']
        price = self.cleaned_data['price']
        image = self.cleaned_data['image']
        start_date = self.cleaned_data['start_date']
        end_date = self.cleaned_data['end_date']

        topic = Topic.objects.get(identifier=self.cleaned_data['topic'])
        location = self.cleaned_data['location']

        Offer.objects.create(
            title=title, description=description, price=price,
            image=image, start_date=start_date, end_date=end_date,
            topic=topic, location=location, author=user
        )

    def validate_topic(self):
        try:
            Topic.objects.get(identifier=self.cleaned_data['topic'])
        except Topic.DoesNotExist:
            raise forms.ValidationError('Invalid topic.')

    def validate_dates(self):
        if self.cleaned_data['start_date'] > self.cleaned_data['end_date']:
            raise forms.ValidationError('End date must be after start date.')


class UpdateOfferForm(forms.Form):
    identifier = forms.UUIDField()
    title = forms.CharField(max_length=255, required=False)
    description = forms.CharField(widget=forms.Textarea, required=False)
    price = forms.DecimalField(max_digits=10, decimal_places=2, min_value=0, required=False)
    image = forms.ImageField(required=False)
    start_date = forms.DateTimeField(required=False)
    end_date = forms.DateTimeField(required=False)
    topic = forms.CharField(max_length=255, required=False)
    location = forms.CharField(max_length=255, required=False)

    def update(self, user):
        offer = Offer.objects.get(identifier=self.cleaned_data['identifier'])

        if offer.author != user:
            raise PermissionError('You are not the author of this offer.')

        if self.cleaned_data['title']:
            offer.title = self.cleaned_data['title']
        if self.cleaned_data['description']:
            offer.description = self.cleaned_data['description']
        if self.cleaned_data['price']:
            offer.price = self.cleaned_data['price']
        if self.cleaned_data['image']:
            offer.image = self.cleaned_data['image']
        if self.cleaned_data['start_date']:
            offer.start_date = self.cleaned_data['start_date']
        if self.cleaned_data['end_date']:
            offer.end_date = self.cleaned_data['end_date']
        if self.cleaned_data['topic']:
            offer.topic = self.cleaned_data['topic']
        if self.cleaned_data['location']:
            offer.location = self.cleaned_data['location']
        offer.save()

class SearchOfferForm(forms.Form):
    text = forms.CharField(max_length=255)

    def search(self):
        return Offer.get_offer_containing_title(self.cleaned_data['text'])

class UUIDOfferForm(forms.Form):
    identifier = forms.UUIDField()

    def get_offer(self):
        return Offer.get_offer_with_id(self.cleaned_data['identifier'])

    def react(self):
        return Offer.add_reaction(self.cleaned_data['identifier'])

    def deactivate(self):
        return Offer.deactivate_offer(self.cleaned_data['identifier'])

    def activate(self):
        return Offer.activate_offer(self.cleaned_data['identifier'])