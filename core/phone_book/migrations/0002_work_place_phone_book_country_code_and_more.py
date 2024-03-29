# Generated by Django 4.1 on 2022-08-18 18:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('phone_book', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Work_place',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=50)),
                ('company_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='phone_book',
            name='country_code',
            field=models.CharField(blank=True, choices=[('+380', 'Ukraine'), ('+44', 'Great Britain'), ('+49', 'Germany'), ('+48', 'Poland')], max_length=10, verbose_name='Country code'),
        ),
        migrations.AddField(
            model_name='phone_book',
            name='work_info',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='phone_book.work_place'),
        ),
    ]
