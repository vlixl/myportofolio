from main.models import Achievement

Achievement.objects.all().delete()

Achievement.objects.create(
    title="3rd Place, Mathematics",
    event="OSNK/Olimpiade Sains Nasional Kabupaten",
    organization="Pusat Prestasi Nasional (Puspresnas)",

    month = 4,
    year = 2023,

    description=
    "Demonstrated advanced logical reasoning, " 
    "problem-solving, and mathematical analysis.",
)

Achievement.objects.create(
    title="3rd Place, English Speech Competition",
    event="14th ALSA English Festival",
    organization="Diponegoro University (UNDIP)",

    month = 11,
    year = 2024,

    description=
    "Secured 3rd place among participants nationwide, " 
    "showcasing persuasive communication, critical thinking, "
    "and public speaking skills.",
)

Achievement.objects.create(
    title="3rd Place, Youth Choir",
    event="9th Festival Paduan Suara (FESPA) Ubaya",
    organization="University of Surabaya",

    month = 6,
    year = 2024,

    description=
    "Achieved 3rd place out of 12 choirs, highlighting teamwork, " \
    "musical interpretation, and stage performance.",
)

Achievement.objects.create(
    title="Gold Medal B, Youth Choir",
    event="Swara Saraswati II Festival",
    organization="Indonesian Institute of the Arts (ISI)",

    month = 2,
    year = 2025,

    description=
    "Won one of the most prestigious choir festival, " \
    "reflecting vocal artistry, discipline, and collaborative excellence.",
)