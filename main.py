import django_setup
from home.models import Game,Genre

# game1 = Game(
#     title='Tetris',
#     release_date='1999-03-14',
#     rating=5,
#     )
# game2 = Game(
#     title='Minecraft',
#     release_date='2014-03-14',
#     rating=5,
#     )
# genre_action = Genre(title='action')
# genre_simulation = Genre(title='simulation')
# genre_sandbox = Genre(title='sandbox')

# genre_action.save()
# genre_simulation.save()
# genre_sandbox.save()

# game1.save()
# game2.save()

minecraft = Game.objects.get(id=2)
tetris = Game.objects.get(id=3)

action = Genre.objects.get(id=1)
simulation = Genre.objects.get(id=2)
sandbox = Genre.objects.get(id=3)

# tetris.genres.add(action)
# tetris.genres.add(sandbox)

# minecraft.genres.add(simulation)
# minecraft.genres.add(sandbox)

print(minecraft.genres.all())
print(tetris.genres.all())