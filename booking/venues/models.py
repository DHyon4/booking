from django.db import models


class Venue(models.Model):
    title = models.CharField(max_length=256, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    address_city = models.CharField(max_length=256, null=True, blank=True)
    address_region_country = models.CharField(max_length=256, null=True, blank=True)
    address_region = models.CharField(max_length=256, null=True, blank=True)
    address_street = models.CharField(max_length=256, null=True, blank=True)
    address_string = models.CharField(max_length=256, null=True, blank=True)

    website = models.CharField(max_length=256, null=True, blank=True)
    featured = models.BooleanField(default=False)
    slug = models.CharField(max_length=32, null=True, blank=True)

    # Should we decide to populate a ton of profiles w/ out user consent,
    #   use this flag to indicate profiles that are owned
    claimed = models.BooleanField(default=True)


class BookingAgent(models.Model):
    first_name = models.CharField(max_length=256, null=True, blank=True)
    last_name = models.CharField(max_length=256, null=True, blank=True)




class Event(models.Model):

    OPPORTUNITY_TYPES = (
        (0, 'FESTIVAL')
        (1, 'CLUB')
        (2, 'MUSIC_SERIES')
        (3, 'PUBLICATION')
        (4, 'COFFEE_HOUSE')
        (5, 'BROADCAST')
        (6, 'MANAGEMENT')
        (7, 'SONGWRITING')
        (8, 'SPECIAL_EVENTS')
        (9, 'CONFERENCE')
        (10, 'RECORD LABEL')
        (11, 'COMPILATION')
        (12, 'INTERNET')
    )

    name = models.CharField(max_length=256, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    slug = models.CharField(max_length=32, null=True, blank=True)

    opportunity_type = models.SmallIntegerField(null=True, choices=OPPORTUNITY_TYPES)

    compensated = models.BooleanField(default=False)
    compensation_food_drink_tickets = models.BooleanField(default=False)
    compensation_general_compensation = models.BooleanField(default=False)
    compensation_max_flat_rate = models.DecimalField(max_digits=8, decimal_places=2)
    compensation_min_flat_rate = models.DecimalField(max_digits=8, decimal_places=2)
    compensation_percent_of_door = models.DecimalField(max_digits=2, decimal_places=2)
    compensation_percent_of_merchandise_sales = models.DecimalField(max_digits=2, decimal_places=2)

    review_by_datetime = models.DateTimeField()

    entry_start_datetime = models.DateTimeField()
    entry_end_datetime = models.DateTimeField()
    event_start_datetime = models.DateTimeField()
    event_end_datetime = models.DateTimeField()

    min_entry_price = models.DecimalField(max_digits=8, decimal_places=2)
    max_entry_price = models.DecimalField(max_digits=8, decimal_places=2)

class Application(models.Model):
    pass

