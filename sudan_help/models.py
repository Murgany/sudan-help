from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator

TYPE_CHOICES = [
    ('help needed', _('Help needed')),
    ('available', _('Available')),
]

OFFER_CHOICES = [
    ('food', _('Food')),
    ('drinking Water', _('Drinking Water')),
    ('medicine', _('Medicine')),
    ('transport', _('Transport')),
    ('accommodation', _('Accommodation')),
]


class Request(models.Model):
    request_type = models.CharField(choices=TYPE_CHOICES, max_length=100, verbose_name=_('Request type'))
    item_name = models.CharField(choices=OFFER_CHOICES, max_length=100, verbose_name=_("Item name"))
    address = models.CharField(max_length=200, verbose_name=_("Address"), blank=True)
    phone_number = models.CharField(max_length=15, verbose_name=_("Phone number"))
    description = models.TextField(max_length=400, null=True, verbose_name=_("Description"))

    class Meta:
        verbose_name = _("Request")
        verbose_name_plural = _("Requests")

    def __str__(self):
        return f'{self.request_type}: {self.item_name}'


MEDICAL_CHOICES = [
    ('Hospital', _('Hospital')),
    ('Pharmacy', _('Pharmacy')),
]


class MedicalService(models.Model):
    service_name = models.CharField(choices=MEDICAL_CHOICES, max_length=100, verbose_name=_("Service name"))
    hospital_or_pharmacy_name = models.CharField(max_length=200, verbose_name=_('Hospital or pharmacy name'),
                                                 default='')
    address = models.CharField(max_length=200, verbose_name=_("Address"))
    phone_number = models.CharField(max_length=18, verbose_name=_("Phone number"))
    open_from = models.DateTimeField(verbose_name=_("Open from"), editable=True)
    closes_at = models.DateTimeField(verbose_name=_("Closes at"), editable=True, default=_('Open 24 hours'))
    description = models.TextField(max_length=400, null=True, verbose_name=_("Description"))

    class Meta:
        verbose_name = _("Medical Service")
        verbose_name_plural = _("Medical Services")

    def __str__(self):
        return f'{self.service_name}: {self.hospital_or_pharmacy_name}'


REPORT_TYPE = [
    ("missing", _("Missing")),
    ("found", _("Found")),
]

GENDER_CHOICES = [
    ("male", _("Male")),
    ("female", _("Female")),
    ("other", _("Other")),
]


class MissingPerson(models.Model):
    report_type = models.CharField(_("Report type"), max_length=30, choices=REPORT_TYPE)
    name = models.CharField(_("Name"), max_length=200)
    age = models.PositiveIntegerField(_("Age"))
    gender = models.CharField(_("Gender"), max_length=10, choices=GENDER_CHOICES)
    photo = models.ImageField(_("Photo"), upload_to='missing_persons')
    last_seen_location = models.CharField(_("Last seen location"), max_length=200, blank=True)
    last_seen_date = models.DateField(_("Last seen date"), blank=True, null=True)
    reported_at = models.DateTimeField(_("Reported at"), auto_now_add=True)
    reporters_phone_number = models.CharField(_("Reporter's phone number"), max_length=18)
    description = models.TextField(_("Description"), max_length=300, blank=True)

    class Meta:
        verbose_name = _("Missing Person")
        verbose_name_plural = _("Missing Persons")

    def __str__(self):
        return f'{self.report_type}: {self.name}'
