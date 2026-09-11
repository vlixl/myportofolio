from main.models import Music

Music.objects.all().delete()

Music.objects.create(
    title="Revived in the Light",
    description="A Renewed Hope in an Endless Fight",
    link="../static/audio/Revived by the Light.mp3",
)

Music.objects.create(
    title="Echo",
    description="A call from the past to relay unto the future",
    link="../static/audio/Echo Orchestra-2.mp3",
)

Music.objects.create(
    title="Eternal Twilight",
    description="Reminisce at the light of dusk",
    link="../static/audio/Eternal Twilight-2.mp3",
)