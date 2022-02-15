FORMAT: 1A

HOST: http://127.0.0.1:8000/

# course-DRF

Course is a simple API for creating courses and for finding courses.

## Authentication
This API is not authentication.

### List All Courses [GET]

+ Response 200 (application/json)

        [
            {
                "category": 1,
                "name": "OgogoAcademy",
                "description": "We are course",
                "logo": "https://ogogo.kg/academy",
                "contacts": [
                    {
                        "type": 1,
                        "link": "+996 (550) 312-312"
                    },
                    {
                        "type": 5,
                        "link": "+996 (550) 312-312"
                    }
                ],
                "branches": [
                    {
                        "latitude": "42.873518",
                        "longitude": "74.619908",
                        "address": "115/1 Ибраимова"
                    }
                ]
            }
        ]

### Create a New Course [POST]

You may create your own course using this action. It takes a JSON
object containing course data
+ Parameters
    + name (string) - The course name
    + description (string) - A information about this course.
    + category (array[object]) - Course category
    + logo (string) - Course logo
    + contacts (array[object]) - Course contacts
        + type (int) - contact type
        + link (string) - link social network or phone number
    + branches (array[object]) - Course branches
        + latitude (string)
            **Latitude**. *Example: 5*. The latitude coordinate of the location of your 
            interest. Must use with `lon`.
        + longitude (string)
            **Longitude**. *Example: 9*. Longitude coordinate of the location of your 
            interest. Must use with `lat`.

+ Request (application/json)

        {
            "name": "OgogoAcademy",
            "description": "We are course",
            "category": 1,
            "logo": "https://ogogo.kg/academy/logo",
            "contacts": [
                {
                    "type": 1, 
                    "link": "+996 (550) 312-312"
                },
                {
                    "type": 5,
                    "link": "+996 (550) 312-312"

                }],
            "branches": [
                {
                    "latitude": "42.873518",
                    "longitude": "74.619908",
                    "address": "115/1 Ибраимова"
                }
                ]
        }
        
+ Response 200 (application/json)

        Successful response

    + Attributes (Successful response)

+ Response 404

        Not found response

## Get Course [/api/course/{course_id}]

## Delete Course [/api/courses/{course_id}/]