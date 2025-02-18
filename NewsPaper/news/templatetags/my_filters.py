from django import template

register = template.Library()


@register.filter()
def censor(value):
    unwanted_words = ['bad', 'word', 'example']
    for word in unwanted_words:
        value = value.replace(word, '*' * len(word))

    return f'{value} Р'
