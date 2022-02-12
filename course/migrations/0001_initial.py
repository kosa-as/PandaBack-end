# Generated by Django 3.2.12 on 2022-02-12 11:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account_management', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_cover', models.CharField(max_length=200)),
                ('category_title', models.CharField(max_length=15)),
                ('category_description', models.CharField(max_length=200)),
                ('category_author', models.CharField(max_length=15)),
                ('category_total', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word_content', models.CharField(max_length=10)),
                ('word_spelling', models.CharField(max_length=30)),
                ('word_meaning', models.CharField(max_length=200)),
                ('word_spell_url', models.CharField(max_length=200)),
                ('user', models.ManyToManyField(to='account_management.User')),
            ],
        ),
        migrations.CreateModel(
            name='VideoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_title', models.CharField(max_length=100)),
                ('video_level', models.CharField(default='', max_length=20)),
                ('video_cover', models.CharField(max_length=200)),
                ('video_url', models.CharField(max_length=200)),
                ('video_author', models.CharField(max_length=40)),
                ('video_reference', models.CharField(default='', max_length=40)),
                ('submission_date', models.DateTimeField(auto_now_add=True)),
                ('video_description', models.CharField(default='', max_length=200)),
                ('video_heat', models.IntegerField(default=0)),
                ('user', models.ManyToManyField(to='account_management.User')),
            ],
        ),
        migrations.CreateModel(
            name='Sentence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sentence_content', models.CharField(max_length=100)),
                ('sentence_English', models.CharField(max_length=100)),
                ('sentence_pronunciation', models.CharField(max_length=200)),
                ('sentence_pinyin', models.CharField(max_length=300)),
                ('user', models.ManyToManyField(to='account_management.User')),
                ('video', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='course.videomodel')),
                ('word', models.ManyToManyField(to='course.Word')),
            ],
        ),
        migrations.CreateModel(
            name='Grammar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grammar_content', models.CharField(max_length=100)),
                ('grammar_example1', models.CharField(default='', max_length=100)),
                ('grammar_example2', models.CharField(default='', max_length=100)),
                ('sentence', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='course.sentence')),
            ],
        ),
    ]