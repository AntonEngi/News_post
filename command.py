#создание пользователя
us1 = User.objects.create_user(username='Petrov Ivan Stepanovich')
us2 = User.objects.create_user(username='Orlov Vasilij Ivanovich')
us3 = User.objects.create_user(username='Ribko Elena Petrovna')

#Авторы
Author.objects.create(autorUser=us1)
Author.objects.create(autorUser=us2)
#Категории
Category.objects.create(name='IT')

#Статьи
author = Author.objects.get(id=1)
Post.objects.create(author=author, categoryType='NW', title='sometitle', text='somebigtext')
    #Проверка
    Post.objects.get(id=1).title

#Категория
Post.objects.get(id=1).postCategory.add(Category.objects.get(id=1))

#Комментарии
Comment.objects.create(commentPost=Post.object.get(id=1), commentUser=Author.objects.get(id=1).authorUser, text='anytextauthor')

#Лайки дизлайки
Comment.objects.get(id=1).like()
    #Comment.objects.get(id=1).rating

#Рейтинг автора
a = Author.objects.get(id=1)
a.update_rating()
a.ratingAuthor
    #Post.objects.get(id=1).like()

#Вывести рейтинг лучшего пользователя
a = Author.objects.order_by('-ratingAuthor')[:1]

    #for i in a:
        # i.ratingAuthor
        # i.authorUser.username