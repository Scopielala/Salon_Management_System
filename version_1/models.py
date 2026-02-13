from django.db import models
from django.core.validators import MinValueValidator
from django.utils import timezone

class Customer(models.Model):
    # Stores customer identity (KYC).
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20, unique=True, help_text="Uniquee phone number used to identify returning customers")
    email = models.EmailField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["name"]
        indexes = [
            models.Index(fields=["phone"]),
        ]

    def __str__(self):
        return f"{self.name} ({self.phone})"
        
class Visit(models.Model):
    # Stores each salon visit and payment
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="visits")
    services = models.CharField(max_length=255, help_text="List of services rendered")
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    visit_date = models.DateField(default=timezone.now)
    notes = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ["-visit_date"]
        indexes = [models.Index(fields=["visit_date"]),]

    def __str__(self):
        return f"{self.customer.name} - {self.visit_date}"

    @property   
    def service_list(self):
        return [s.strip() for s in self.services.split(",") if s.strip()]