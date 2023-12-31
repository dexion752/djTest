# Generated by Django 4.2.2 on 2023-07-04 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Testdata',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('entry', models.TextField(blank=True, null=True)),
                ('hanja', models.TextField(blank=True, db_column='hanJa', null=True)),
                ('metaterm', models.TextField(blank=True, db_column='metaTerm', null=True)),
                ('field', models.TextField(blank=True, null=True)),
                ('pageno', models.IntegerField(blank=True, db_column='pageNo', null=True)),
                ('simpleex', models.TextField(blank=True, db_column='simpleEx', null=True)),
            ],
            options={
                'db_table': 'testdata',
                'managed': False,
            },
        ),
    ]
