# schema.py
import graphene
from graphene_django.types import DjangoObjectType
from .models import Book

class BookType(DjangoObjectType):
    class Meta:
        model = Book

#Query
class Query(graphene.ObjectType):
    all_books = graphene.List(BookType)
    book = graphene.Field(BookType, id=graphene.Int())
    some_book = graphene.List(BookType, total=graphene.Int())

    def resolve_all_books(root, info):
        return Book.objects.all()

    def resolve_book(root, info, id):
        return Book.objects.get(pk=id)
    def resolve_some_book(root, info, total):
        return Book.objects.all()[:total]

# Create
class CreateBook(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        author = graphene.String(required=True)
        published_year = graphene.Int(required=True)

    book = graphene.Field(BookType)

    def mutate(self, info, title, author, published_year):
        book = Book(title=title, author=author, published_year=published_year)
        book.save()
        return CreateBook(book=book)

# Update
class UpdateBook(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        title = graphene.String()
        author = graphene.String()
        published_year = graphene.Int()

    book = graphene.Field(BookType)

    def mutate(self, info, id, title=None, author=None, published_year=None):
        book = Book.objects.get(pk=id)
        if title: book.title = title
        if author: book.author = author
        if published_year: book.published_year = published_year
        book.save()
        return UpdateBook(book=book)

# Delete
class DeleteBook(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    ok = graphene.Boolean()

    def mutate(self, info, id):
        book = Book.objects.get(pk=id)
        book.delete()
        return DeleteBook(ok=True)

# Root Mutation
class Mutation(graphene.ObjectType):
    create_book = CreateBook.Field()
    update_book = UpdateBook.Field()
    delete_book = DeleteBook.Field()

# Final Schema
schema = graphene.Schema(query=Query, mutation=Mutation)
