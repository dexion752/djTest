from django.db import models

# Create your models here.
class Testdata(models.Model):
    id = models.IntegerField(primary_key=True)
    entry = models.TextField(blank=True, null=True)
    hanja = models.TextField(db_column='hanJa', blank=True, null=True)  # Field name made lowercase.
    metaterm = models.TextField(db_column='metaTerm', blank=True, null=True)  # Field name made lowercase.
    field = models.TextField(blank=True, null=True)
    pageno = models.IntegerField(db_column='pageNo', blank=True, null=True)  # Field name made lowercase.
    simpleex = models.TextField(db_column='simpleEx', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'testdata'
