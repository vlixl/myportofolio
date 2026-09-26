
from .handlers.achievement_views import (
    create_achievement, 
    update_achievement, 
    delete_achievement, 
    get_achievements_json,
    toggle_achievement_star,
)
from .handlers.auth_views import (
    register, 
    login_user, 
    logout_user,
)
from .handlers.main_views import (
    show_main,
)
from .handlers.page_views import (
    show_art,
    show_education,
)
from .handlers.project_views import (
    create_project,
    show_projects,
    delete_project,
    get_projects_json,
    toggle_project_star,
)