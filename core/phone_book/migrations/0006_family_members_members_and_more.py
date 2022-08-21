# Generated by Django 4.1 on 2022-08-21 08:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('phone_book', '0005_family_members_phone_book_family_members'),
    ]

    operations = [
        migrations.AddField(
            model_name='family_members',
            name='members',
            field=models.CharField(default='No members', help_text='Do you have wife and\\or husband, son and\\or daughter', max_length=200, verbose_name='Family_members'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='phone_book',
            name='family_members',
            field=models.ForeignKey(blank=True, default='No members', null=True, on_delete=django.db.models.deletion.SET_NULL, to='phone_book.family_members'),
        ),
    ]