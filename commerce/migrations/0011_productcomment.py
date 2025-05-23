# Generated by Django 4.2.20 on 2025-03-28 08:52

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('commerce', '0010_rename_foodproductdetail_productdetail'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(help_text='Nội dung bình luận của khách hàng')),
                ('rating', models.PositiveSmallIntegerField(blank=True, help_text='Đánh giá sản phẩm (từ 1 đến 5)', null=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='commerce.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_comments', to='commerce.user')),
            ],
        ),
    ]
