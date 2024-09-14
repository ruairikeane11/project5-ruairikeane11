from django.db import models

# Create your models here.
class Faq(models.Model):
    """
    Model for frequently asked questions
    """
    question = models.CharField(max_length=255, help_text="Please ask us questions")
    answer = models.TextField(help_text="Answer here")

    class Meta:
        verbose_name = "FAQ"
        verbose_name_plural = "FAQs"

    def __str__(self):
        return self.question