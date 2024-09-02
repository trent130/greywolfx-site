from django import template
from django.utils.safestring import mark_safe
from staticpages.models import BlogPost, Category, Testimonial, Director

register = template.Library()

@register.simple_tag
def get_recent_posts(num=4):
    return BlogPost.objects.order_by('-time_uploaded')[:num]

@register.simple_tag
def get_categories():
    return Category.objects.all()

# @register.filter
# def truncate_words(value, length):
#     words = value.split()
#     if len(words) > length:
#         return ' '.join(words[:length]) + '...'
#     return value

@register.simple_tag
def get_popular_posts(num=4):
    return BlogPost.objects.order_by('-likes')[:num]

@register.inclusion_tag('staticpages/tags/category_list.html')
def show_categories_with_post_count():
    categories = Category.objects.prefetch_related('posts').all()
    return {'categories': categories}

@register.filter(is_safe=True)
def highlight_search(text, search):
    if not search:
        return mark_safe(text)
    return mark_safe(text.replace(search, f'<span class="highlight">{search}</span>'))

@register.inclusion_tag('staticpages/tags/testimonial.html')
def show_testimonials_with_profile_pictures():
    testimonials = Testimonial.objects.all()
    return {'testimonials': testimonials }

@register.inclusion_tag('staticpages/tags/director.html')
def show_directors_with_their_pictures():
    directors = Director.objects.all()
    return {'directors': directors}