from main.models import Achievement

Achievement.objects.all().delete()

Achievement.objects.create(
    award="3rd",
    award_label="Place",
    category="Mathematics",

    month=4,
    year=2023,

    event="OSNK / Olimpiade Sains Nasional Kabupaten",
    organization="Pusat Prestasi Nasional (Puspresnas)",

    description=
    "Demonstrated advanced logical reasoning, "
    "problem-solving, and mathematical analysis.",
)

Achievement.objects.create(
    award="3rd",
    award_label="Place",
    category="English Speech Competition",

    month=11,
    year=2024,

    event="14th ALSA English Festival",
    organization="Diponegoro University (UNDIP)",

    description=
    "Secured 3rd place among participants nationwide, "
    "showcasing persuasive communication, critical thinking, "
    "and public speaking skills.",
)

Achievement.objects.create(
    award="3rd",
    award_label="Place",
    category="Youth Choir",

    month=6,
    year=2024,

    event="9th Festival Paduan Suara (FESPA) Ubaya",
    organization="University of Surabaya",

    description=
    "Achieved 3rd place out of 12 choirs, highlighting teamwork, "
    "musical interpretation, and stage performance.",
)

Achievement.objects.create(
    award="Gold",
    award_label="Medal B",
    category="Youth Choir",

    month=2,
    year=2025,

    event="Swara Saraswati II Festival",
    organization="Indonesian Institute of the Arts (ISI)",

    description=
    "Won one of the most prestigious choir festivals, "
    "reflecting vocal artistry, discipline, and collaborative excellence.",
)