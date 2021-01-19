from __future__ import unicode_literals

from copy import deepcopy
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from mezzanine.blog.models import BlogPost, BlogCategory
from mezzanine.blog.admin import BlogPostAdmin, BlogCategoryAdmin


blog_fieldsets = deepcopy(BlogPostAdmin.fieldsets)
ext_fieldsets = blog_fieldsets[0][1]["fields"][:-2]
ext_fieldsets.extend(["voting_date", "content", "contest_type"])
blog_fieldsets[0][1]["fields"] = ext_fieldsets


class ContestAdmin(BlogPostAdmin):
    fieldsets = blog_fieldsets



if BlogPost in admin.site._registry: 
    admin.site.unregister(BlogPost)
    admin.site.register(BlogPost, ContestAdmin)
    BlogPost._meta.verbose_name = "Contest"
    BlogPost._meta.verbose_name_plurals = "Contests"
    BlogPost._meta.get_field('content').verbose_name = _('Description')
    
if BlogCategory in admin.site._registry:
    BlogCategory._meta.verbose_name = "Contest Category"
    BlogCategory._meta.verbose_name_plurals = "Contest Categories"