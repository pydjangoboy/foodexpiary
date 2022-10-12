how to run this code  :
### Step 1: Create a Virtual Environment

Isolate your python project from other python projects by using the built-in [venv](https://docs.python.org/dev/library/venv.html) module:

```
python3.10 -m venv venv
```

- I recommend Python 3.8 and up
- You can use _any_ virtual environment manager (poetry, pipenv, virtualenv, etc)

### Step 2: Activate Virtual Environment

_macOS/Linux_

```
source venv/bin/activate
```

_Windows_

```
.\venv\Scripts\activate
```

### Step 3: Install Requirements

```
$(venv) python -m pip install pip --upgrade
$(venv) python -m pip install -r requirements.txt
```

- `$(venv)` is merely denoting the virtual environment is activated
- In `requirements.txt` you'll see `django>=3.2,<4.0` -- this means I'm using the latest version of Django 3.2 since it's an LTS release.
- You can use `venv/bin/python -m pip install -r requirements.txt` (mac/linux) or `venv\bin\python -m pip install -r requirements.txt` (windows)
- `pip install ...` is not as reliable as `python -m pip install ...`

### Step 4: to run on local server :
```
$(venv) python manage.py runserver
```

### Step 5: copy the link and past into chrom url bar :
```
http://127.0.0.1:8000/
```


### Step 6: login admin user id and password :

```
user id : jai
password : jai..
admin mail  : admin123@gmail.com

```

### Step 7: Task ToDo :

Track export date status :

    good green
    yellow warning
    red expired

Authentication page :  [login page/signup/ logout]

    email
    password
    fname
    lname

user profile:

    registered email

item details :

    descriptions
    photo
    quantity
    expiry date
    price

option :

    dairy
    beverages
    frozen vegetables
    meat
    fruits

extra thing :

    Separate specific search tag:
    Separate each item
    Live track the items expiration date day by day
    Notification expire items
    registered email send



EXPIRY_DATE_DICTIONARY = {
    'Apple': 28,
    'Avocado': 5,
    'Banana': 5,
    'Kiwi': 20,
    'Lemon': 28,
    'Lime': 30,
    'Mango': 5,
    'Melon': 10,
    'Nectarine': 5,
    'Orange': 28,
    'Papaya': 7,
    'Passion fruit': 28,
    'Peach': 5,
    'Pear': 7,
    'Pineapple': 5,
    'Plum': 5,
    'Pomegranate': 50,
    'Red grapefruit': 28,
    'Tangerine': 14,
    'Juice': 14,
    'Milk': 10,
    'Sour-Cream': 21,
    'Soy-Milk': 14,
    'Yoghurt': 14,
    'Asparagus': 7,
    'Eggplant': 10,
    'Brown-Cap-Mushroom': 7,
    'Cabbage': 28,
    'Carrots': 28,
    'Cucumber': 7,
    'Garlic': 180,
    'Ginger': 42,
    'Leek': 14,
    'Onion': 42,
    'Pepper': 14,
    'Potato': 120,
    'Beet': 5,
    'Tomato': 7,
    'Zucchini': 14,
    'Corn': 5,
    'Snowpeas': 4,
    'White-Mushroom': 14,
}


todo : 
request.user.exp_date - date.today()).days <= 90