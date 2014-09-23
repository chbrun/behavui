from menu import Menu, MenuItem
from django.core.urlresolvers import reverse

project_submenu = (
        MenuItem("List", 
            reverse("projects_list"),
            weight=10,
            icon="tools"),
        )

Menu.add_item("main", MenuItem("Projects", 
    reverse("projects_list"),
    weight = 10,
    children = project_submenu,
    icon="tools"))
