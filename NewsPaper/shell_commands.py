from django.contrib.auth.models import User
from news.models import Author, Category, Post, Comment
from django.utils import timezone

user1 = User.objects.create_user('user1', 'user1@example.com', 'password1')
user2 = User.objects.create_user('user2', 'user2@example.com', 'password2')

author1 = Author.objects.create(user=user1)
author2 = Author.objects.create(user=user2)

category1 = Category.objects.create(name='Спорт')
category2 = Category.objects.create(name='Политика')
category3 = Category.objects.create(name='Образование')
category4 = Category.objects.create(name='Технологии')

post1 = Post.objects.create(author=author1, type='AR', title='Статья 1', text='Это текст первой статьи.', created_at=timezone.now())
post2 = Post.objects.create(author=author1, type='NW', title='Новость 1', text='Это текст первой новости.', created_at=timezone.now())
post3 = Post.objects.create(author=author2, type='AR', title='Статья 2', text='Это текст второй статьи.', created_at=timezone.now())

post1.categories.add(category1, category2)
post2.categories.add(category3)
post3.categories.add(category4, category2)

comment1 = Comment.objects.create(post=post1, user=user1, text='Комментарий 1 для Статьи 1.', created_at=timezone.now())
comment2 = Comment.objects.create(post=post2, user=user2, text='Комментарий 1 для Новости 1.', created_at=timezone.now())
comment3 = Comment.objects.create(post=post1, user=user2, text='Комментарий 2 для Статьи 1.', created_at=timezone.now())
comment4 = Comment.objects.create(post=post3, user=user1, text='Комментарий 1 для Статьи 2.', created_at=timezone.now())

post1.like()
post1.like()
post1.dislike()
post2.like()
comment1.like()
comment2.like()
comment3.dislike()
comment4.like()

author1.update_rating()
author2.update_rating()

best_user = Author.objects.order_by('-rating').first()
print(f'Лучший пользователь: {best_user.user.username}, Рейтинг: {best_user.rating}')

best_post = Post.objects.order_by('-rating').first()
print(f'Лучший пост: {best_post.title}, Автор: {best_post.author.user.username}, Рейтинг: {best_post.rating}')
print(f'Превью: {best_post.preview()}')

best_post_comments = Comment.objects.filter(post=best_post)
for comment in best_post_comments:
    print(f'Комментарий от {comment.user.username} {comment.created_at}: {comment.text} (Рейтинг: {comment.rating})')