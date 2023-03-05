# Operation Victoria
***
### This repository Will house **`kalenshi.com`** Written in flask as opposed to the one written in Django
***
```
├── docker-compose.yaml
├── Dockerfile
├── notes.txt
├── README.md
├── requirements.txt
├── run.py
└── victoria
    ├── config
    │   ├── config.dev.json
    │   ├── config.local.json
    │   ├── config.prod.json
    │   ├── config.py
    │   └── __init__.py
    ├── error_handlers
    │   ├── __init__.py
    │   ├── routes
    │   │   ├── forbidden.py
    │   │   ├── __init__.py
    │   │   ├── pagenotfound.py
    │   │   └── server_error.py
    │   └── templates
    │       └── error_404.html
    ├── __init__.py
    ├── main
    │   ├── forms
    │   │   └── __init__.py
    │   ├── __init__.py
    │   ├── routes
    │   │   ├── about.py
    │   │   ├── home.py
    │   │   └── __init__.py
    │   └── templates
    │       ├── about.html
    │       └── home.html
    ├── models
    │   ├── __init__.py
    │   ├── post.py
    │   └── user.py
    ├── posts
    │   ├── forms
    │   │   ├── __init__.py
    │   │   └── post.py
    │   ├── __init__.py
    │   ├── routes
    │   │   ├── create_post.py
    │   │   ├── delete_post.py
    │   │   ├── __init__.py
    │   │   ├── post_page.py
    │   │   └── update_post.py
    │   └── templates
    │       ├── create_post.html
    │       └── post_page.html
    ├── static
    │   ├── css
    │   │   ├── error_page.css
    │   │   └── main.css
    │   └── media
    │       └── profile_pics
    │           ├── 080388d6f8cd3c199f53cd45339a49f9.jpg
    │           ├── 3173e2d5ac65a7ece5f8e74748d8e4cc.jpg
    │           └── default.png
    ├── templates
    │   └── base.html
    ├── tests
    │   └── __init__.py
    └── users
        ├── forms
        │   ├── account.py
        │   ├── account_update.py
        │   ├── __init__.py
        │   ├── login.py
        │   ├── register.py
        │   ├── request_reset_form.py
        │   └── reset_password.py
        ├── __init__.py
        ├── routes
        │   ├── account.py
        │   ├── __init__.py
        │   ├── login.py
        │   ├── logout.py
        │   ├── register.py
        │   ├── request_reset.py
        │   ├── reset_password.py
        │   └── user_posts.py
        ├── templates
        │   ├── account.html
        │   ├── account_update.html
        │   ├── login.html
        │   ├── register.html
        │   ├── request_reset.html
        │   ├── reset_password.html
        │   └── user_posts.html
        └── utils
            ├── __init__.py
            ├── save_picture.py
            └── send_mail.py

```
