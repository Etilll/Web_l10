import json
from pathlib import Path
from django.contrib.auth.models import User
from .models import Post, Author, Tag

def prepare_tags_for_db():
    tags_set = set()
    with open(f"{Path(__file__).parent.resolve()}/quotes_reformatted.json", "r") as file:
        records = json.load(file)

        for record in records:
            for tag in record['post_tags']:
                tags_set.add(tag)

    return tags_set


def prepare_data_for_db():
    tags = prepare_tags_for_db()
    tags_dict = dict()

    tag_id = 1
    for item in tags:
        tmp = Tag(id=tag_id, tag_name=item, tag_creator=User.objects.get(id=1))
        tmp.save()
        tags_dict[item] = tag_id
        tag_id += 1

    authors_dict = dict()
    with open(f"{Path(__file__).parent.resolve()}/authors_reformatted.json", "r") as file:
        records = json.load(file)

        auth_id = 1
        for record in records:
            tmp = Author(id=auth_id, author_name=record['author_name'], author_desc=record['author_desc'], author_birth_day=record['author_birth_day'],author_birth_month=record['author_birth_month'],author_birth_year=record['author_birth_year'],author_birth_place=record['author_birth_place'],author_creator=User.objects.get(id=1))
            tmp.save()
            authors_dict[record['author_name']] = auth_id
            auth_id += 1

    with open(f"{Path(__file__).parent.resolve()}/quotes_reformatted.json", "r") as file:
        records = json.load(file)

        post_id = 1
        for record in records:
            tmp = Post(id=post_id, post_text=record['post_text'], post_author=Author.objects.get(id=authors_dict[record['post_author']]), post_creator=User.objects.get(id=1))
            tmp.save()
            for tagg in record['post_tags']:
                temp_tag = Tag.objects.get(id=tags_dict[tagg])
                tmp.post_tags.add(temp_tag)
            tmp.save()
            post_id += 1


def transform_authors():
    new_data = []
    with open(f"{Path(__file__).parent.resolve()}/authors.json", "r") as file:
        records = json.load(file)

        for record in records:
            new_record = {}
            new_record['author_name'] = record['fullname']
            tmp = record['born_date'].strip().split()
            tmp[1] = str(tmp[1])[:len(tmp[1])-1]
            new_record['author_birth_day'] = tmp[1]
            new_record['author_birth_month'] = tmp[0]
            new_record['author_birth_year'] = tmp[2]
            new_record['author_birth_place'] = record['born_location']
            new_record['author_desc'] = record['description']
            new_record['author_creator'] = 1
            new_data.append(new_record)
            
        with open(f"{Path(__file__).parent.resolve()}/authors_reformatted.json", "w") as newfile:
            newfile = json.dump(new_data, newfile, indent=2)

def transform_quotes():
    new_data = []
    with open(f"{Path(__file__).parent.resolve()}/quotes.json", "r") as file:
        records = json.load(file)

        for record in records:
            new_record = {}
            new_record['post_author'] = record['author']
            new_record['post_text'] = record['quote']
            new_record['post_tags'] = record['tags']
            new_record['post_creator'] = 1
            new_data.append(new_record)

        with open(f"{Path(__file__).parent.resolve()}/quotes_reformatted.json", "w") as newfile:
            newfile = json.dump(new_data, newfile, indent=2)

#transform_authors()
#transform_quotes()
prepare_data_for_db()

