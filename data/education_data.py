from main.models import Education

Education.objects.all().delete()

Education.objects.create(
    school="SD Santa Maria Purwokerto",

    start_year = 2013,
    end_year = 2019,
    grade=94.10,

    description=
    "Built an early foundation "
    "in academics and competitions.",
    
    logo="../static/img/education/logo_sd.webp",
)

Education.objects.create(
    school="SMP Susteran Purwokerto",

    start_year = 2019,
    end_year = 2022,
    grade=92.73,

    description=
    "Developed stronger interests "
    "in science and mathematics.",
    
    logo="../static/img/education/logo_smp.webp",
)

Education.objects.create(
    school="SMA Sedes Sapientiae Jambu",

    start_year = 2022,
    end_year = 2025,
    grade=89.24,

    description=
    "Expanded into academics, "
    "public speaking, and performing arts.",
    
    logo="../static/img/education/logo_sma.webp",
)

Education.objects.create(
    school="Universitas Indonesia",

    start_year = 2025,

    description=
    "Currently studying Computer Science "
    "and building technical skills.",
    
    logo="../static/img/education/logo_ui.webp",
)