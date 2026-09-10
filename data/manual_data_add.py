from main.models import Music

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

from main.models import Education

Education.objects.create(
    title="SD Santa Maria Purwokerto",
    description_1="Lorem ipsum dolor sit amet.",
    description_2="Lorem ipsum dolor sit amet.",
    description_3="Lorem ipsum dolor sit amet.",
)