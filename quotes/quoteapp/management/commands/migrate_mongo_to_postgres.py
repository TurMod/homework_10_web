from django.core.management.base import BaseCommand, CommandError
from django.db.utils import IntegrityError
from quoteapp.models import Quote as QuotePModel
from quoteapp.models import Author as AuthorPModel
from pymongo.errors import InvalidURI
from mongoengine import Document, connect
from mongoengine.fields import StringField, ListField, ReferenceField


class Author(Document):
    fullname = StringField()
    born_date = StringField()
    born_location = StringField()
    description = StringField()

class Quote(Document):
    tags = ListField()
    author = ReferenceField(Author)
    quote = StringField()

class Command(BaseCommand):
    help = 'Migrate data from mongodb to postgres database'

    def add_arguments(self, parser):
        parser.add_argument('mongodb_uri', nargs=1, type=str)

    def handle(self, *args, **options):
        mongodb_uri = options['mongodb_uri']
        try:
            connect(host=mongodb_uri, ssl=True)
            for author in Author.objects():
                new_author = AuthorPModel(fullname=author.fullname, biography=author.description)
                new_author.save()
                for quote in Quote.objects(author=author):
                    new_quote = QuotePModel(quote=quote.quote, author=new_author)
                    new_quote.save()
        except IntegrityError:
            raise CommandError('Elements that you are trying to migrate are already exist')
        except InvalidURI:
            raise CommandError('The URI to the database is not valid!')
