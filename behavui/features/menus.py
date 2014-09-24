from menu import Menu, MenuItem
from django.core.urlresolvers import reverse

Menu.add_item("main",MenuItem("Features",
            reverse("features_list"),
            weight=10,
            icon="tools",
            )
        )



