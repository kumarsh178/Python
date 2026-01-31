from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry
from .models import Customer

@registry.register_document
class CustomerDocument(Document):
    class Index:
        name = "customers"
        settings = {'number_of_shards': 1,
                    'number_of_replicas': 0}
    # father models properties to index foreign index
    father_name = fields.ObjectField(properties = {
            "name": fields.TextField()
        }
    )
    class Django:
        model = Customer
        fields=[
            "name",
            "email",
            "phone",
            "city",
            "age"
        ]