# Generated by Django 4.0 on 2024-01-15 19:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_remove_post_hit_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='sub_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sub_categoryes', to='posts.subcategory'),
        ),
    ]
