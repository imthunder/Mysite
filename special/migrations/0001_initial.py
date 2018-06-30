# Generated by Django 2.0.6 on 2018-06-30 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DxDetail',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('pid', models.CharField(max_length=255, primary_key=True)),
                ('article', models.TextField()),
                ('tags', models.TextField()),
            ],
            options={
                'db_table': 'dx_detail',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DxIndex',
            fields=[
                ('id', models.CharField(max_length=16, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('cover', models.TextField()),
            ],
            options={
                'db_table': 'dx_index',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DxList',
            fields=[
                ('pid', models.CharField(max_length=16)),
                ('href', models.CharField(max_length=255, primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('imgurl', models.TextField(db_column='imgUrl')),
                ('author', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'dx_list',
                'managed': False,
            },
        ),
    ]
