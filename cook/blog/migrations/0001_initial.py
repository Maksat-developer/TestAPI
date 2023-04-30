# Generated by Django 4.2 on 2023-04-30 14:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя категории')),
                ('slug', models.SlugField(max_length=100, verbose_name='Ссылка')),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('mptt_level', models.PositiveIntegerField(editable=False)),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children', to='blog.category', verbose_name='Родитель')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='DeyWeek',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dey_name', models.CharField(max_length=50, verbose_name='День недели')),
            ],
            options={
                'verbose_name': 'День',
                'verbose_name_plural': 'Дни',
            },
        ),
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название блюда')),
                ('slug', models.SlugField()),
            ],
            options={
                'verbose_name': 'Блюда',
                'verbose_name_plural': 'Блюда',
            },
        ),
        migrations.CreateModel(
            name='Ingredients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Ингредиент')),
                ('slug', models.SlugField(max_length=100, verbose_name='Ссылка')),
            ],
            options={
                'verbose_name': 'Ингредиент',
                'verbose_name_plural': 'Ингредиенты',
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Заглавление')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('create_at', models.DateTimeField(blank=True, null=True, verbose_name='Дата создания')),
                ('Ingredients', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Ингредиент', to='blog.ingredients', verbose_name='Ингредиенты')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Menu', to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
                ('breakfast', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Завтрак', to='blog.dish', verbose_name='Завтрак')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Menu', to='blog.category', verbose_name='Категория')),
                ('dinner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Ужин', to='blog.dish', verbose_name='Ужин')),
                ('lunch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Обед', to='blog.dish', verbose_name='Обед')),
            ],
            options={
                'verbose_name': 'Меню',
                'verbose_name_plural': 'Меню',
            },
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название')),
                ('serves', models.CharField(max_length=50, verbose_name='Служит')),
                ('prep_time', models.DurationField(default=0, verbose_name='Время подготовки')),
                ('cook_time', models.DurationField(default=0, verbose_name='Время приготовления')),
                ('directions', models.TextField(verbose_name='Направление')),
                ('ingredients', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Ингредиенты', to='blog.ingredients', verbose_name='Ингредиенты')),
                ('menu', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='recipe', to='blog.menu', verbose_name='Меню')),
            ],
            options={
                'verbose_name': 'Рецепт',
                'verbose_name_plural': 'Рецепты',
            },
        ),
        migrations.CreateModel(
            name='DishWeek',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField()),
                ('dey_week', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='deyweek', to='blog.deyweek', verbose_name='Дни')),
                ('dish', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dishweek', to='blog.dish', verbose_name='Название блюда')),
                ('ingredients', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ingredient', to='blog.ingredients', verbose_name='Ингредиенты')),
            ],
            options={
                'verbose_name': 'Блюдо на неделю',
                'verbose_name_plural': 'Блюда на неделю ',
            },
        ),
        migrations.AddField(
            model_name='dish',
            name='ingredients',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ingredients', to='blog.ingredients', verbose_name='Ингредиенты'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Заглавление')),
                ('email', models.CharField(max_length=100, verbose_name='Email')),
                ('message', models.TextField(max_length=500, verbose_name='Сообщение')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='blog.menu', verbose_name='Меню')),
            ],
            options={
                'verbose_name': 'Коментарий',
                'verbose_name_plural': 'Коментарии',
            },
        ),
    ]