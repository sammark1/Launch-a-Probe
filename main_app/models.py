from django.db import models

SYSTEM_CHOICES = (
	("s", "solitary star"),
	("b", "binary system"),
	("t", "trinary system"),
    ("cl", "star cluster"),
    ("sn", "stellar nebula"),
)

class System(models.Model):

    designation = models.CharField(max_length = 60)
    name = models.CharField(max_length = 128)
    system_type = models.CharField(max_length = 20, choices = SYSTEM_CHOICES)
    created_at = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['designation']