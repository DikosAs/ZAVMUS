# Generated by Django 5.0 on 2023-12-27 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0003_alter_contacts_options_alter_objacts_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataFromIndexPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ru_text', models.TextField(verbose_name='Текст на русском')),
                ('ud_text', models.TextField(verbose_name='Текст на удмуртском')),
                ('en_text', models.TextField(verbose_name='Текст на английском')),
            ],
        ),
    ]