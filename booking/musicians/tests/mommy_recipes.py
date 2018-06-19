from model_mommy import mommy
from model_mommy.recipe import Recipe, foreign_key, seq

from musicians.models import Musician
from home.models import OpusUser

admin_user_recipe = Recipe(
    OpusUser,
    is_staff=True,
    is_active=True
)

user_musician_recipe = Recipe(
    OpusUser,
    is_musician=True
)

musician_recipe = Recipe(
    Musician,
    user=foreign_key(user_musician_recipe),
    slug=seq("slug")
)