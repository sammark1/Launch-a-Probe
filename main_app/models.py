from django.db import models
from django.contrib.auth.models import User

SYSTEM_CHOICES = (
	("Solitary star", "Solitary star"),
	("Binary system", "Binary system"),
	("Trinary system", "Trinary system"),
    ("Star cluster", "Star cluster"),
    ("Stellar nebula", "Stellar nebula"),
)

class System(models.Model):

    designation = models.CharField(max_length = 60, unique=True)
    name = models.CharField(max_length = 128)
    system_type = models.CharField(max_length = 20, choices = SYSTEM_CHOICES)
    # discoverer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='visitors')
    discoverer = models.ForeignKey(User, on_delete=models.PROTECT, related_name='visitors')
    visitors = models.ManyToManyField(User, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['designation']

STELLAR_CHOICES = (
	("sg", "supergiant"),
	("g", "giant"),
	("o", "O-spectrum"),
    ("b", "B-spectrum"),
    ("a", "A-spectrum"),
    ("f", "F-spectrum"),
    ("g", "G-spectrum"),
    ("k", "K-spectrum"),
    ("m", "M-spectrum"),
    ("w", "White Dwarf"),
)

class Star_Object(models.Model):
    
    designation = models.CharField(max_length = 60, unique=True)
    name = models.CharField(max_length = 128)
    system = models.ForeignKey(System, on_delete=models.CASCADE)
    stellar_class = models.CharField(max_length = 50, choices = STELLAR_CHOICES)
    emission_color = models.IntegerField()
    mass = models.FloatField()
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['designation']

PLANETOID_TYPES = (
	("g", "gas giant"),
	("r", "rocky planet"),
	("d", "dwarf planet"),
)

class Planetoid (models.Model):
    
    designation = models.CharField(max_length = 60, unique=True)
    name = models.CharField(max_length = 128)
    system = models.ForeignKey(System, on_delete=models.CASCADE)
    body_type = models.CharField(max_length = 20, choices = PLANETOID_TYPES)
    mass = models.FloatField()
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['designation']