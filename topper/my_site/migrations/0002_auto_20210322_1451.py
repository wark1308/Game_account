# Generated by Django 3.1.7 on 2021-03-22 08:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('my_site', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='topper',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='commentary',
            name='topper',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='my_site.topper'),
        ),
        migrations.AddField(
            model_name='commentary',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_comments', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='advertisement',
            name='topper',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_site.topper'),
        ),
        migrations.AddField(
            model_name='adverimage',
            name='advertisement',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='my_site.advertisement'),
        ),
    ]