# Generated by Django 3.0.7 on 2020-10-02 20:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Actores', '0001_initial'),
        ('Categoria', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Documentales',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('keywords', models.CharField(max_length=255)),
                ('description', models.TextField(max_length=255)),
                ('lugar', models.IntegerField(default='1')),
                ('puntuacion', models.IntegerField(default='1')),
                ('image', models.ImageField(upload_to='Documentales/')),
                ('detail', models.TextField()),
                ('slug', models.SlugField(unique=True)),
                ('status', models.BooleanField(default=True)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('actores', models.ManyToManyField(to='Actores.ActoresModelo')),
                ('genero', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Categoria.Categorias')),
            ],
            options={
                'verbose_name': 'Documental',
                'verbose_name_plural': 'Documentales',
                'ordering': ['lugar'],
            },
        ),
        migrations.CreateModel(
            name='ImagesDocumentales',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50)),
                ('image', models.ImageField(blank=True, upload_to='Partes Documentales/')),
                ('documentales', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Documentales.Documentales')),
            ],
            options={
                'verbose_name': 'Imagen',
                'verbose_name_plural': 'Imagenes',
                'ordering': ['id'],
            },
        ),
    ]
