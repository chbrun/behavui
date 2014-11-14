from menu import Menu, MenuItem
from django.core.urlresolvers import reverse

Menu.add_item(
    "main",
    MenuItem(
        "Campaign",
        reverse("campaigns_list"),
        weight=10,
        icon="tools",
    )
)
