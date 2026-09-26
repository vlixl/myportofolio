# To import seeded data, open the terminal, and type:
# python manage.py shell < import.py

exec(open("seed/music_data.py").read())
exec(open("seed/education_data.py").read())
exec(open("seed/achievement_data.py").read())
exec(open("seed/photo_data.py").read())
exec(open("seed/users.py").read())