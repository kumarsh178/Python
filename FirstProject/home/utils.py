from django.template.defaultfilters import slugify
import uuid

def generateNewSlug(name,ModelClass):
    new_slug = slugify(name)
    if ModelClass.objects.filter(product_slug = new_slug).exists():
        new_slug = f"{new_slug}-{str(uuid.uuid4()).split('_')[0]}"
    return new_slug