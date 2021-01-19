from django.db import models
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

from mezzanine.conf import settings
from mezzanine.blog.models import BlogPost, BlogCategory

from mezzanine.core.fields import FileField, RichTextField
from mezzanine.core.models import RichText, Orderable, Slugged
from mezzanine.pages.models import Page, Link
from mezzanine.utils.models import upload_to

from main.common import AdType, AD_TYPES, SOCIAL_MEDIA_TYPES, SocialMediaType



# class HomePage(Page, RichText):
#     '''
#     A page representing the format of the home page
#     '''
#     # heading = models.CharField(max_length=200,
#     #     help_text="The heading under the icon blurbs")
#     # subheading = models.CharField(max_length=200,
#     #     help_text="The subheading just below the heading")
#     feature_heading = models.CharField(max_length=200,
#         default="Contest Features")
#     current_contest_description = models.CharField(max_length=200,
#          default="""Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
#         Mihi vero, inquit, placet agi subtilius et, ut ipse dixisti, pressius.""")
#     recent_contest_description = models.CharField(max_length=200,
#         help_text="This a short description of the recent contest section displayed "
#                   "on the home page.",
#         default="""Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
#         Mihi vero, inquit, placet agi subtilius et, ut ipse dixisti, pressius.""")

#     class Meta:
#         verbose_name = _("Home page")
#         verbose_name_plural = _("Home pages")


# class AdSlider(Orderable):
#     '''
#     A slide in a slider connected to a HomePage
#     '''
#     homepage = models.ForeignKey(HomePage, related_name="adslides")
#     ad_sloggan = models.CharField(max_length=200,
#         help_text="The Sloggan to display under the link title")
#     image = FileField(verbose_name=_("Image"),
#         upload_to=upload_to("home.AdSlide.image", "slider"),
#         format="Image", max_length=255)
#     ad_type = models.CharField(
#         max_length=255,
#         choices=AD_TYPES,
#         default=AdType.BRAND,
#     )
#     brand_logo =  FileField(verbose_name=_("Brand Logo"),
#         upload_to=upload_to("home.AdSlide.image", "brand"),
#         format="Image", max_length=255, null=True, blank=True)
#     link = models.ForeignKey(Link, help_text="Clicking the Slider will go here.")


# class SocialMediaLinks(Orderable):
#     '''
#     An icon box on a HomePage
#     '''
#     media_type = models.CharField(
#         max_length=255,
#         choices=SOCIAL_MEDIA_TYPES, 
#         default=SocialMediaType.FACEBOOK,
#     )
#     link = models.CharField(max_length=2000, blank=True,
#         help_text="Optional, if provided clicking the blurb will go here.")


# class Shopping(Orderable):
#     '''
#     A collection of individual Shopping items
#     '''
#     homepage = models.ForeignKey(HomePage, related_name="shopping")

#     shop_description = models.CharField(max_length=200,
#         help_text="This a short description of the shopping section displayed "
#                   "on the home page.",
#         default="""Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
#         Mihi vero, inquit, placet agi subtilius et, ut ipse dixisti, pressius.""")

#     product_price = models.IntegerField(verbose_name=_("Product price"), default=0)
    
#     discount_price = models.IntegerField(verbose_name=_("Discount price"), default=0)
#     image = FileField(verbose_name=_("Product Image"),
#         upload_to=upload_to("home.shopping.image", "products"),
#         format="Image", max_length=255)
#     link = models.ForeignKey(Link, help_text="Clicking the Product will go there.")
#     class Meta:
#         verbose_name = _("Shopping Item")
#         verbose_name_plural = _("Shopping Items")