from django.db import models
from django.template.loader import render_to_string

class Strategy(models.Model):
    template = 'composer/strategy.html'

    rendered = models.TextField(('Rendered strategy'), blank=True, default='')

    def save(self, *args, **kwargs):
        if not self.rendered:
            self.rendered = render_to_string(self.template, self.context)
        return super().save(*args, **kwargs) 






    