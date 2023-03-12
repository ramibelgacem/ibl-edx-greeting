0001 Purpose of This Repo
#########################

Status
******

**Draft**

Context
*******

This project is for an application for a Python developer position.

Decision
********

REST API greeting endpoint

The django app project include a REST API POST endpoint which accept a greeting message from the user.

This endpoint should do the following things with the user-submitted greeting:
    - Log it in the LMS platform.
    - Save it in the database.
    - If the greeting is “hello”, then the view of this API endpoint should call the original greeting endpoint again with “goodbye” as the parameter.

It is secured with Oauth2.
