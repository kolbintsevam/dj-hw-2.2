# Generated by Django 4.2 on 2023-05-02 13:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_tag_alter_article_options_scope_article_scope'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='scope',
            options={'verbose_name': 'Связь', 'verbose_name_plural': 'Связи'},
        ),
        migrations.RemoveField(
            model_name='article',
            name='scope',
        ),
        migrations.AlterField(
            model_name='scope',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.tag', verbose_name='Раздел'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Название тэгов'),
        ),
    ]