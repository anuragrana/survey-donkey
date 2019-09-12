#### Details
 - Project: Survey Donkey  
 - Developer: Anurag Rana  
--------
#### Setup:
##### Prerequisits:
 - Python 3.5
 - Mysql 5.7+
 - Ubuntu 16.04
 
##### Steps:
- Create [virtual environment](https://www.pythoncircle.com/post/404/virtual-environment-in-python-a-pocket-guide/) using Python3.5
- Activate virtual environment using command `source venv/bin/activate`.
- Install python packages using requirements.txt file. Command `pip install -r requirements.txt`:
- Create Mysql DB 'survey_db'. Update username and password in settings.py file.
- Run migrations `python manage.py migrate`.
- Run the development server using command `python manage.py runserver`.
- Go to browser and open the application on URL localhost:8000.
  

-------
#### Features:

##### Done:
- Create survey.
- Add Questions. Question can be of one of the below type:  
    - Small Text - Text Input
    - Large Text - Textarea
    - Multiple Choice, single select - Radio button
    - Multiple Choice, Multi Select - Checkbox
- Preview on right side.
- Fill survey
- Store responses
- Show Results
    - Pie charts/Bar charts/Tables 
##### Remaining:
- Validations Frontend and backend.
- Exception handling
- Delete Question
- Edit Survey

----------    
#### Future Work:  
 - Reordering of questions
     - Either by deleting and inserting a new question at specific place.
     - Or by drag and drop.
     - Or up and down arrow on each question.
 - Color scheme
 - Number of questions per page, Progress bar
 - Authorization
