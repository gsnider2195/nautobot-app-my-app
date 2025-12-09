"""Menu items."""

from nautobot.apps.ui import NavMenuAddButton, NavMenuGroup, NavMenuItem, NavMenuTab

items = (
    NavMenuItem(
        link="plugins:my_app:testmodel_list",
        name="My App",
        permissions=["my_app.view_testmodel"],
        buttons=(
            NavMenuAddButton(
                link="plugins:my_app:testmodel_add",
                permissions=["my_app.add_testmodel"],
            ),
        ),
    ),
)

menu_items = (
    NavMenuTab(
        name="Apps",
        groups=(NavMenuGroup(name="My App", items=tuple(items)),),
    ),
)
