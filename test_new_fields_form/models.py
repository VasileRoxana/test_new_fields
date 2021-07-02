from django.conf import settings
from django.db import models

# Backwards compatible settings.AUTH_USER_MODEL
USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')


class ExtraInfo(models.Model):
    """
    This model contains two extra fields that will be saved when a user registers.
    The form that wraps this model is in the forms.py file.
    """
    user = models.OneToOneField(USER_MODEL, null=True,  related_name='user+', on_delete=models.CASCADE)
    
    AGE_CHOICES = [
        ('Sub 20 ani', '< 20'),
        ('Intre 20 si 25 ani', '20 - 25'),
        ('Intre 25 si 30 ani', '25 - 30'),
        ('Intre 30 si 40 ani', '30 - 40'),
        ('Peste 40 ani', '> 40'),
    ]

    age = models.CharField(
        verbose_name="Varsta",
        max_length=255,
        choices=AGE_CHOICES,
    )
    
    MONTH_CHOICES = [
        ('Iauarie', 'Ianuarie'),
        ('Februarie', 'Februarie'),
        ('Martie', 'Martie'),
        ('Aprilie', 'Aprilie'),
        ('Mai', 'Mai'),
        ('Iunie', 'Iunie'),
        ('Iulie', 'Iulie'),
        ('August', 'August'),
        ('Septembrie', 'Septembrie'),
        ('Octombrie', 'Octombrie'),
        ('Noiembrie', 'Noiembrie'),
        ('Decembrie', 'Decembrie'),
    ]

    birth_month = models.CharField(
        verbose_name="Luna nasterii",
        max_length= 255,
        choices=MONTH_CHOICES
    )

    SEX_CHOICES = [
        ('Feminin', 'F'),
        ('Masculin', 'M'),
    ]

    sex = models.CharField(
        verbose_name="Sex",
        max_length = 255,
        choices=SEX_CHOICES
    )

    STUDIES_CHOICES = [
        ('Liceale', 'Liceale'),
        ('Universitare', 'Universitare'),
        ('Post Universitare', 'Post universitare'),
        ('Altele', 'Altele'),
    ]

    studies = models.CharField(
        verbose_name="Studii",
        max_length=255,
        choices=STUDIES_CHOICES
    )

    job = models.CharField(
        verbose_name="Ce job ai in prezent?",
        max_length=255,
    )

    EXPECTATIONS_CHOICES = [
        ('Reconversie profesionala', 'Reconversie profesionala'),
        ('Salariu mai mare', 'Salariu mai mare'),
        ('Angajare in IT', 'Angajare in IT'),
        ('Specializare pe o anumita tehnologie', 'Specializare pe o anumita tehnologie'),
        ('Acumulare de experienta', 'Acumulare de experienta'),
        ('Altele', 'Altele'),
    ]

    expectations = models.CharField(
        verbose_name="Asteptari in urma absolvirii",
        max_length=255,
        choices=EXPECTATIONS_CHOICES
    )

    ENVIRONMENT_CHOICES = [
        ('Urban', 'Urban'),
        ('Rural', 'Rural'),
    ]

    user_environment = models.CharField(
        verbose_name="Mediu",
        max_length=255,
        choices=ENVIRONMENT_CHOICES
    )    
    
    def __str__(self):
        result = '{0.user} {0.age} {0.birth_month} {0.sex} {0.studies} {0.job} {0.expectations} {0.user_environment}'
        return result.format(self)
