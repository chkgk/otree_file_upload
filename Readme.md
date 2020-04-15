# File and Image upload with oTree
## Overview
This demonstrates how you can handle file uploads and specifically image file uploads by participants in oTree experiments. It uses standard django fields and directly attaches the files to the player object.

## Demo
Here is a [simple demo](https://otree-file-upload.herokuapp.com).

## Requirements
Make sure to add ```pillow``` to the ```requirements.txt``` if you want to handle image uploads.

## Usage
Creata a ```media``` folder in your project and add the following to your ```settings.py```. Uploaded files will be stored in the media folder.
```python
from os import path

ROOT_URLCONF = 'urls'
MEDIA_ROOT = "_media"
MEDIA_URL = "/media/"
```

Create ```urls.py``` in your project containing:
```python
from otree.urls import urlpatterns
from django.conf.urls.static import static
import settings

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

In your app, you need to import the model fields directly from django and specify the ```upload_to``` parameter. Files will be stored in these subdirectories of the ```MEDIA_ROOT``` setting we added earlier.

models.py:
```python
from django.db import models as django_models

class Player(BasePlayer):
    image = django_models.ImageField(upload_to="images")
    file = django_models.FileField(upload_to="files")
```

In ```pages.py```, add the fields as you would do with any other fields:
```python
class Upload(Page):
    form_model = 'player'
    form_fields = ['image', 'file']
```

To display uploaded images or provide links to uploaded files in the templates, make sure to reference the ```url``` property of the field like this:
```html
<img src="{{ player.image.url }}">
<a href="{{ player.file.url }}">download</a>
```

## A serious note
Allowing people to upload files to your server is a security risk. Please make sure you know what you are doing and are ready to take the risks before using this snippet.