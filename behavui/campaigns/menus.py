from menu import Menu, Menuitem
from django.core.urlresolvers import reverse

Menu.add_item("main",MenuItem("Campaign",
            reverse("campaign_list"),
            weight=10,
            icon="tools",)
        )



