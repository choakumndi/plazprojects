from __future__ import unicode_literals
from datetime import datetime, timedelta

from django.contrib.auth import get_user_model
from django.db.models import Count, Q
from django.utils import timezone

from mezzanine.generic.models import Keyword
from mezzanine import template
from main.models import DisplayedProduct

User = get_user_model()

register = template.Library()

convert_to_timezone = lambda x: x.astimezone(timezone.get_current_timezone())

is_future = lambda a:convert_to_timezone(a) >= convert_to_timezone(datetime.today())

seconds_from_today = lambda b: (convert_to_timezone(b) - convert_to_timezone(datetime.today())).total_seconds()


@register.filter
def is_login_path(pth):
    """
    Put a list of dates for contest posts into the template context.
    """
    return pth == '/accounts/login/'
    
    
@register.filter
def is_signup_path(pth):
    """
    Put a list of dates for contest posts into the template context.
    """
    return pth == '/accounts/signup/'
    
    

@register.filter
def in_future(t):
    """
    Put a list of dates for contest posts into the template context.
    """
    return (convert_to_timezone(t) - convert_to_timezone(datetime.now())).total_seconds() > 0
    

   
@register.filter
def to_timestamp(t):
    """
    Put a list of dates for contest posts into the template context.
    """ 
    return str(seconds_from_today(t))

@register.filter
def join_or_vote(d):
    """
    Put a list of dates for contest posts into the template context.
    """
    if convert_to_timezone(d) >= convert_to_timezone(datetime.now()):
        text = 'join now free' 
    else:
        text = 'start voting'
    return text
  

@register.inclusion_tag("admin/includes/quick_contest.html", takes_context=True)
def quick_contest(context):
    """
    Admin dashboard tag for the quick contest form.
    """
    context["form"] = ContestPostForm()
    return context.flatten()


@register.inclusion_tag('includes/home/shop_item_list.html')
def quick_home_contest(obj):
    """
    A.
    """
    context["page_object"] = obj
    return context.flatten()
    
@register.inclusion_tag('includes/home/shop_item_list.html', takes_context=True)
def quick_shop_tag(context):
    """
    A.
    """
    # context = {}
    products = DisplayedProduct.objects.all()
    context["shop_details"] = products
    return context.flatten()
