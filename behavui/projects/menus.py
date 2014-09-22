from menu import Menu, MenuItem
from django.core.urlresolvers import reverse

Menu.add_item("main", MenuItem("Projects", 
    reverse("projects.views.index"),
    weight = 10,
    icon="tools"))
