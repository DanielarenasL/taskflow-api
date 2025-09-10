from apps.teams import *
from apps.projects import *
from apps.tasks import *
from apps.users import *

import datetime


#* USERS

# create_user("test", "test@test.com", "test", "test", "admin")
# get_users()
# get_user_by_id("4b9707e2-0de2-4a21-ad7f-a189734d7bff")
# update_user("4b9707e2-0de2-4a21-ad7f-a189734d7bff", "email", "daniel@test.com")

#* TEAM

# create_team("zapatos", "grupo de desarrollo", "84a43351-8298-452c-a5ae-46a90736bb5f")
# get_teams()
# update_team("0154dfb1-cf6d-455e-a537-4d7e86d7d34c", "name", "LosPerchas")

#* MEMBERS

# add_member("LosPerchas", "4b9707e2-0de2-4a21-ad7f-a189734d7bff")
# delete_member("LosPerchas", "4b9707e2-0de2-4a21-ad7f-a189734d7bff")
# get_members("de002b98-154d-44f6-97b4-2dd29c56738f")

#* PROJECT

# create_project("perchas11", "ApiREST", "de002b98-154d-44f6-97b4-2dd29c56738f", "planning", datetime.date(2025, 9, 10), datetime.date(2025, 11, 10), "high")
# delete_project("8314f18a-3b79-46fa-bdbf-f1e1020264a3")
# update_project("82cfd186-ba22-49fd-94ce-4e98b45f3808", "start_date", datetime.date(2026, 9, 2))
# get_projects_filtered("team_id", "de002b98-154d-44f6-97b4-2dd29c56738f")

#* TASK

# create_task("Crear crud", "Crear crud en Python","cbe31dab-af35-46b8-b638-30b67ce5acb9" ,"84a43351-8298-452c-a5ae-46a90736bb5f", "todo", "low", 50, 24, datetime.date(2025, 9, 10), ["a", "b"])
# get_task_by_id("ab2616e4-790b-4526-80dd-873d1919bdfa")
# delete_task("b5793100-c3ca-4f2e-8a19-fe9a2eabf940")
# assign_task("b9a547bb-2d4e-4444-82dd-f135c4909280", "4b9707e2-0de2-4a21-ad7f-a189734d7bff")
# get_user_tasks("4b9707e2-0de2-4a21-ad7f-a189734d7bff")
# update_task("a638832e-a291-4aa9-bd1f-c7e0386ceffe", "assigned_to", "4b9707e2-0de2-4a21-ad7f-a189734d7bff")