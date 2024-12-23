from django import template

register = template.Library()


@register.inclusion_tag('tags/recipe_card.html')
def show_recipe(recipe,
                explain=False,
                btn_detail=False,
                btn_edit=False,
                btn_delete=False):
    return {"recipe": recipe,
            "btn_detail": btn_detail,
            "btn_edit": btn_edit,
            "btn_delete": btn_delete,
            "explain": explain}
