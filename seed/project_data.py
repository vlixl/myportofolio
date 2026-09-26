from main.models import Project

Project.objects.all().delete()

Project.objects.create(
    title = "Bézier Curve Visualizer",
    description = "An interactive Bézier curve visualizer "
    "built with tkinter that demonstrates "
    "how control points shape smooth curves in real time.",
    tech_stack = "Python",
    project_url = "",
    project_image_url = "",
)

Project.objects.create(
    title = "Phyllotaxis Visualizer",
    description = "An interactive visualization " 
    "that explores how different divergence angles " 
    "affect the arrangement of points, highlighting " 
    "the remarkably even distribution produced by the golden angle.",
    tech_stack = "Python",
    project_url = "",
    project_image_url = "",
)

Project.objects.create(
    title="Generic Graph Data Structure",
    description="A reusable Java implementation "
    "of a generic graph data structure, designed to support "
    "flexible vertex types and common graph operations.",
    tech_stack = "Java",
    project_url = "",
    project_image_url = "",
)