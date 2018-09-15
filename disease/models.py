from django.db import models

# Create your models here.

class MainSymptoms(models.Model):
    """Model definition for MainSymptoms."""

    class Meta:
        """Meta definition for MainSymptoms."""

        verbose_name = '主症'
        verbose_name_plural = '主症'

    def __str__(self):
        """Unicode representation of MainSymptoms."""
        return self.symptoms

    # TODO: check logs and refresh weight

    symptoms = models.CharField(verbose_name="症状", max_length=50, unique=False)

    
class MainPrescription(models.Model):
    """Model definition for MainPrescription."""

    class Meta:
        """Meta definition for MainPrescription."""

        verbose_name = '主方'
        verbose_name_plural = '主方'

    def __str__(self):
        """Unicode representation of MainPrescription."""
        return self.prescription

    # TODO: prescription satisfaction

    prescription = models.CharField(verbose_name='药方', max_length=50, unique=False)


class Disease(models.Model):
    """Model definition for Disease."""

    class Meta:
        """Meta definition for Disease."""

        verbose_name = '疾病'
        verbose_name_plural = '疾病'

    def __str__(self):
        """Unicode representation of Disease."""
        return self.disease_name


    disease_name = models.CharField(verbose_name="疾病名称", max_length=50)
    main_symptoms  = models.ManyToManyField(MainSymptoms, verbose_name='主要症状')
    main_prescription  = models.ManyToManyField(MainPrescription, verbose_name='主药方', blank=True)


class DiseaseType(models.Model):
    """Model definition for DiseaseType."""

    class Meta:
        """Meta definition for DiseaseType."""

        verbose_name = '疾病分型'
        verbose_name_plural = '疾病分型'

    def __str__(self):
        """Unicode representation of DiseaseType."""
        return str(self.disease) + '/' + self.type_name
    
    disease = models.ForeignKey(Disease, on_delete=models.CASCADE, verbose_name='疾病')
    type_name = models.CharField(verbose_name='分型名称', max_length=50)
    type_symptoms = models.CharField(verbose_name='分型症状', max_length=200)
    add_prescription = models.ManyToManyField(MainPrescription, verbose_name='处方加减')
