from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

from accounts.models import User


class Category(MPTTModel):
    name = models.CharField(max_length=100, verbose_name='Имя категории')
    slug = models.SlugField(max_length=100, verbose_name='Ссылка')
    parent = TreeForeignKey('self',
                            verbose_name='Родитель',
                            related_name='children',
                            on_delete=models.SET_NULL,
                            blank=True,
                            null=True
                            )

    class MPTTMeta:
        level_attr = 'mptt_level'
        order_insertion_by = ['name']

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Ingredients(models.Model):
    name = models.CharField(max_length=100, verbose_name='Ингредиент')
    slug = models.SlugField(max_length=100, verbose_name='Ссылка')

    class Meta:
        verbose_name = 'Ингредиент'
        verbose_name_plural = 'Ингредиенты'

    def __str__(self) -> str:
        return self.name


class Dish(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название блюда')
    slug = models.SlugField(max_length=50)
    ingredients = models.ForeignKey(Ingredients,
                                    related_name='ingredients',
                                    verbose_name='Ингредиенты',
                                    on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Блюда'
        verbose_name_plural = 'Блюда'

    def __str__(self) -> str:
        return self.name
    
class DeyWeek(models.Model):
    dey_name = models.CharField(max_length=50, verbose_name='День недели')


    class Meta:
        verbose_name = 'День'
        verbose_name_plural = 'Дни'

    def __str__(self) -> str:
        return self.dey_name



class DishWeek(models.Model):
    dish = models.ForeignKey(Dish,
                             related_name='dishweek',
                             verbose_name='Название блюда',
                             on_delete=models.CASCADE,
                             )
    slug = models.SlugField(max_length=50)
    ingredients = models.ForeignKey(Ingredients,
                                    related_name='ingredient',
                                    verbose_name='Ингредиенты',
                                    on_delete=models.CASCADE)
    dey_week = models.ForeignKey(DeyWeek,
                                    related_name='deyweek',
                                    verbose_name='Дни',
                                    on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Блюдо на неделю'
        verbose_name_plural = 'Блюда на неделю '

    def __str__(self) -> str:
        return f"Блюдо {self.dish}"



class Menu(models.Model):
    author = models.ForeignKey(
        User,
        verbose_name='Автор',
        related_name='Menu',
        on_delete=models.CASCADE)
    title = models.CharField(max_length=200, verbose_name='Заглавление')
    category = models.ForeignKey(Category,
                                 verbose_name='Категория',
                                 related_name='Menu',
                                 on_delete=models.SET_NULL,
                                 null=True)
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='Дата создания')
    Ingredients = models.ForeignKey(
        Ingredients,
        verbose_name='Ингредиенты',
        related_name='Ингредиент',
        on_delete=models.CASCADE)
    breakfast = models.ForeignKey(
        Dish,
        verbose_name='Завтрак',
        related_name='Завтрак',
        on_delete=models.CASCADE)
    lunch = models.ForeignKey(
        Dish,
        verbose_name='Обед',
        related_name='Обед',
        on_delete=models.CASCADE)
    dinner = models.ForeignKey(
        Dish,
        verbose_name='Ужин',
        related_name='Ужин',
        on_delete=models.CASCADE)
    create_at = models.DateTimeField(
        null=True, blank=True, verbose_name='Дата создания')

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'

    def __str__(self):
        return f"Владелец:{self.author} Завтрак: {self.breakfast} Обед: {self.lunch} Ужин:{self.dinner} Дата Создания записи {self.create_at}"


class Recipe(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    serves = models.CharField(max_length=50, verbose_name='Служит')
    prep_time = models.DurationField(
        default=0, verbose_name='Время подготовки')
    cook_time = models.DurationField(
        default=0, verbose_name='Время приготовления')
    ingredients = models.ForeignKey(
        Ingredients,
        verbose_name='Ингредиенты',
        related_name='Ингредиенты',
        on_delete=models.CASCADE)
    directions = models.TextField(verbose_name='Направление')
    menu = models.ForeignKey(Menu,
                             verbose_name='Меню',
                             related_name='recipe',
                             on_delete=models.SET_NULL,
                             null=True,
                             blank=True
                             )

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'

    def __str__(self) -> str:
        return self.name


class Comment(models.Model):
    title = models.CharField(max_length=50, verbose_name='Заглавление')
    email = models.CharField(max_length=100, verbose_name='Email')
    message = models.TextField(max_length=500, verbose_name='Сообщение')
    menu = models.ForeignKey(Menu,
                             verbose_name='Меню',
                             related_name='comment',
                             on_delete=models.CASCADE,
                             )
    author = models.ForeignKey(User,
                               verbose_name='Пользователь',
                               on_delete=models.SET_NULL,
                               null=True)

    class Meta:
        verbose_name = 'Коментарий'
        verbose_name_plural = 'Коментарии'

    def __str__(self) -> str:
        return self.title
