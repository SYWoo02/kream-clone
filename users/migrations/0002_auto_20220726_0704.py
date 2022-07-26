# Generated by Django 3.2 on 2022-07-26 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='프로필 이미지'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_ad_email',
            field=models.BooleanField(default=False, verbose_name='광고성 이메일 수신동의 여부'),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_ad_message',
            field=models.BooleanField(default=False, verbose_name='광고성 메세지 수신동의 여부'),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(max_length=11, verbose_name='연락처'),
        ),
        migrations.AlterField(
            model_name='user',
            name='shoes_size',
            field=models.CharField(blank=True, choices=[('220', '220'), ('225', '225'), ('230', '230'), ('235', '235'), ('240', '240'), ('245', '245'), ('250', '250'), ('255', '255'), ('260', '260'), ('265', '265'), ('270', '270'), ('275', '275'), ('280', '280'), ('285', '285'), ('290', '290'), ('295', '295'), ('300', '300')], max_length=3, verbose_name='신발 사이즈'),
        ),
    ]