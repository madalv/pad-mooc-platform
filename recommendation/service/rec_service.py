import logging
from rec_system import rec_system as rs
from repository import course_repo as cr

class RecService:
  course_repo = None
  rec_sys = None

  def __init__(self, course_repo: cr.CourseRepo):
    logging.info("Init Recommendation Service")
    self.course_repo = course_repo
    courses = self.course_repo.fetch_courses()
    # TODO don't do this
    courses = courses if courses != [] else [('test', 'test', 'test', 'test', 'test')]
    self.rec_sys = rs.RecSystem(courses)


  def add_course(self, course: dict):
    """
    Takes a dict of the form:
    {
      'course_id': '179',
      'title': 'Distributed Databases Course',
      'description': 'Introduction to Distributed Applications, Databases, Cloud',
      'author': 'New Author',
      'categories': 'Cloud Distributed Applications Databases'
    }
    """
    logging.info(f'Adding course {course["course_id"]}')
    # add course to both active dataframe and database
    self.rec_sys.append_course(course)
    self.course_repo.add_course(course)
  
  def get_recs_for_user(self, user_id: str, nr: int):
    """
    Returns a unique list of tuples of the form [(title, id), (title, id), ...]
    """

  

    logging.info(f'Getting recs for user {user_id}')
    list = self.course_repo.fetch_user_courses(user_id)
    # logging.debug(list)
    recs = []

    if len(list) == 0:
      raise Exception("no courses found for user")
    
    # if the course list is bigger than the nr of recs required, get 1 rec per course
    nr_per_course = 1 if (nr / len(list) < 1) else int(nr / len(list) + 1)

    for id in list:
      course_recs = self.rec_sys.get_recs(id, nr_per_course)
      for rec in course_recs:
        if rec not in list:
          recs.append(rec)

    if len(recs) > nr:
      return recs[:nr]
    else:
      return recs

  def get_recs_for_course(self, course_id: str, nr: int):
    """
    Returns a list of tuples of the form [(title, id), (title, id), ...]
    """
    self.rec_sys = rs.RecSystem(self.course_repo.fetch_courses())
    logging.info(f'Getting recs for course {course_id}')
    return self.rec_sys.get_recs(course_id, nr)