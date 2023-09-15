__author__ = 'Shaban Mohammedsaani Hassan [shaban00]'

from resources.college import CollegeResource
from resources.department import DepartmentResource
from resources.student import StudentResource

""" Register all API_URLS

    API_URLS = [
        {
            "resource": Resource,
            "urls": (
                "/,
                "/index",
            ),
            "endpoint": "index"
        }
    ]
 """

API_URLS = [
    {
        "resource": CollegeResource,
        "urls": ("/colleges", "/colleges/"),
        "endpoint": "colleges",
    },
    {
        "resource": DepartmentResource,
        "urls": ("/departments", "/departments/",),
        "endpoint": "departments",
    },
    {
        "resource": StudentResource,
        "urls": ("/students", "/students/"),
        "endpoint": "students",
    },
]
