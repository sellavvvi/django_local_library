# Generated by Django 5.0.6 on 2024-07-03 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sch', '0003_lessons_answer_les_lessons_text_les'),
    ]

    operations = [
        migrations.CreateModel(
            name='TagLessons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=100)),
                ('slug', models.SlugField(blank=True, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='lessons',
            name='url',
            field=models.SlugField(unique=True),
        ),
        migrations.AddField(
            model_name='lessons',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='tags', to='sch.taglessons'),
        ),
    ]
