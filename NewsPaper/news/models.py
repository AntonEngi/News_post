from django.db import models

# Create your models here.
world = 'WO'
business = 'BU'
health = 'HE'
tech = 'TE'
travel = 'TR'
sports = 'SP'
CATEGORIES = [
    (world, 'Мир'),
    (business, 'Бизнес'),
    (health, 'Здоровье'),
    (tech, 'Технология'),
    (travel, 'Путешествия')
    (sports, 'Спорт')
]
class Author(models.Model):
    full_name = models.CharField(max_length=255)
    info_author = models.TextField()
    # cвязь «один к одному» с встроенной моделью пользователей User;
    # рейтинг пользователя
class Category(models.Model):
    title_category = models.CharField(max_length = 2, choices = CATEGORIES, unique = True, default = world)
    description_category = models.CharField(max_length=255)

class Post(models.Model):
    header = models.CharField(max_leight=255) #заголовок статьи
    content = models.TextField() #текст статьи
    date_of_post = models.DateTimeField(auto_now_add=True) #дата и время создания
    # связь «один ко многим» с моделью Author
    # поле с выбором — «статья» или «новость»;
    # связь «многие ко многим» с моделью Category (с дополнительной моделью PostCategory)
    # рейтинг статьи/новости.
    # id_author = models.IntegerField(Author)
class PostCategory(models.Model):
    pass
    # связь «один ко многим» с моделью Post;
    # связь «один ко многим» с моделью Category.
class Comment(models.Model):
    comment_text = models.TextField() # текст комментария;
    date_of_creation = models.DateTimeField(auto_now_add=True) # дата и время создания комментария;
    # связь «один ко многим» с моделью Post;
    # связь «один ко многим» со встроенной моделью User(комментарии может оставить любой пользователь, необязательно автор);

    # рейтинг комментария.