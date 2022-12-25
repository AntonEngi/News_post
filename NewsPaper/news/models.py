from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum

# Create your models here.
# world = 'WO'
# business = 'BU'
# health = 'HE'
# tech = 'TE'
# travel = 'TR'
# sports = 'SP'
# CATEGORIES = [
#     (world, 'Мир'),
#     (business, 'Бизнес'),
#     (health, 'Здоровье'),
#     (tech, 'Технология'),
#     (travel, 'Путешествия')
#     (sports, 'Спорт')
# ]
class Author(models.Model):
    authorUser = models.OneToOneField(User, on_delete=models.CASCADE) # cвязь «один к одному» с встроенной моделью пользователей User;
    ratingAuthor = models.SmallIntegerField(default=0) # рейтинг пользователя
    # full_name = models.CharField(max_length=255)
    # info_author = models.TextField()
    def update_rating(self):
        postRat = self.post_set.aggregate(postRating=Sum('rating'))
        pRat = 0
        pRat += postRat.get('postRating')

        commentRat = self.authorUser.comment_set.aggregate(commentRating=Sum('rating'))
        cRat = 0
        cRat += commentRat.get('commentRating')

        self.ratingAuthor = pRat * 3 + cRat
        self.save()
class Category(models.Model):
    # title_category = models.CharField(max_length = 2, choices = CATEGORIES, unique = True, default = world)
    # description_category = models.CharField(max_length=255)
    name = models.CharField(max_length=64, unique=True)
class Post(models.Model):
    header = models.CharField(max_length=255) #заголовок статьи
    content = models.TextField() #текст статьи
    date_of_post = models.DateTimeField(auto_now_add=True) #дата и время создания
    author = models.ForeignKey(Author, on_delete=models.CASCADE)# связь «один ко многим» с моделью Author

    NEWS = 'NW'# поле с выбором — «статья» или «новость»;
    ARTICLE = 'AR'
    CATEGORY_CHOISES = (
        (NEWS, 'Новость'),
        (ARTICLE, 'Статья'),
    )
    categoryType = models.CharField(max_length=2, choices=CATEGORY_CHOISES, default=ARTICLE)
    dateCreation = models.DateTimeField(auto_now_add=True)
    postCategory = models. ManyToManyField(Category, through='PostCategory')
    title = models.CharField(max_length=128)
    rating = models.SmallIntegerField(default=0)

    # связь «многие ко многим» с моделью Category (с дополнительной моделью PostCategory)
    def like(self):# рейтинг статьи/новости.
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()
    # id_author = models.IntegerField(Author)
class PostCategory(models.Model):
    postThrough = models.ForeignKey(Post, on_delete=models.CASCADE)
    categoryThrough = models.ForeignKey(Category, on_delete=models.CASCADE)
    # связь «один ко многим» с моделью Post;
    # связь «один ко многим» с моделью Category.
class Comment(models.Model):
    # comment_text = models.TextField() # текст комментария;
    # date_of_creation = models.DateTimeField(auto_now_add=True) # дата и время создания комментария;
    commentPost = models.ForeignKey(Post, on_delete=models.CASCADE)
    commentUser = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    dataCreation = models.DateTimeField(auto_now_add=True)
    rating = models.SmallIntegerField(default=0)
    def like(self):
        self.rating += 1
        self.save()
    def dislike(self):
        self.rating -= 1
        self.save()
    def preview(self):
        return self.text[0:123] + '...' + str(self.rating) #прописать форматом '{} ... {}'.format

    # связь «один ко многим» с моделью Post;
    # связь «один ко многим» со встроенной моделью User(комментарии может оставить любой пользователь, необязательно автор);

    # рейтинг комментария.