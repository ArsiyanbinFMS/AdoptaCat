# Generated by Django 2.2 on 2020-04-28 06:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('adoption', '0003_remove_comment_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cat',
            name='vaccines',
            field=models.ManyToManyField(blank=True, to='adoption.Vaccine'),
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=100)),
                ('housetype', models.CharField(choices=[('Single', 'บ้านเดี่ยว'), ('Shop', 'อาคารพาณิชย์หรือตึกแถว'), ('Town', 'ทาวน์เฮาส์'), ('Flat ', 'แฟลตหรืออาพาร์ตเม้นต์'), ('Condominium ', 'คอนโดมิเนียม')], max_length=40)),
                ('fencedetail', models.CharField(choices=[('Yes', 'มีรั้ว'), ('No', 'ไม่มีมีรั้ว')], max_length=15)),
                ('budget', models.PositiveIntegerField()),
                ('pets', models.CharField(choices=[('Yes', 'ใช่'), ('No', 'ไม่ใช่')], max_length=10)),
                ('message', models.TextField(max_length=200)),
                ('date', models.DateField(auto_now_add=True)),
                ('contact', models.CharField(default='หมายเลขโทรศัพท์หรืออีเมลติดต่อ', max_length=40)),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requests', to='adoption.Cat')),
                ('requester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
