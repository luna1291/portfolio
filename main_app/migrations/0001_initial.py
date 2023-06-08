# Generated by Django 4.1.7 on 2023-06-08 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="AboutPage",
            fields=[
                (
                    "id",
                    models.CharField(max_length=100, primary_key=True, serialize=False),
                ),
                (
                    "about_shert",
                    models.CharField(max_length=250, verbose_name="Название"),
                ),
                (
                    "header",
                    models.CharField(
                        max_length=250, null=True, verbose_name="Заголовок"
                    ),
                ),
                ("topbox", models.TextField(verbose_name="Опыт")),
                (
                    "header2",
                    models.CharField(
                        max_length=250, null=True, verbose_name="Заголовок"
                    ),
                ),
                ("botbox", models.TextField(verbose_name="Навыки")),
                (
                    "image",
                    models.ImageField(
                        default="", upload_to="img/", verbose_name="Шкала"
                    ),
                ),
            ],
            options={
                "verbose_name": "Профессия",
                "verbose_name_plural": "Профессия",
            },
        ),
        migrations.CreateModel(
            name="HomePage",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("quote", models.TextField(verbose_name="Цитата")),
                ("text", models.TextField(verbose_name="Приветствие")),
                (
                    "photo",
                    models.ImageField(
                        blank=True, default="", upload_to="img/", verbose_name="Фото"
                    ),
                ),
            ],
            options={
                "verbose_name": "Приветствие",
                "verbose_name_plural": "Приветствия",
            },
        ),
        migrations.CreateModel(
            name="Serts",
            fields=[
                ("id", models.IntegerField(primary_key=True, serialize=False)),
                (
                    "sert_name",
                    models.CharField(max_length=250, verbose_name="Название"),
                ),
                (
                    "serts",
                    models.ImageField(
                        default="", upload_to="img/", verbose_name="Сертификаты"
                    ),
                ),
            ],
            options={
                "verbose_name": "Сертификат",
                "verbose_name_plural": "Сертификаты",
            },
        ),
    ]