package service

import (
	"course/model"
	"course/util"

	"github.com/gookit/slog"
)

type courseRepo interface {
	GetCategoryList(categoryIDs []string) ([]*model.Category, error)
	Create(course *model.Course) error
	GetByIDWithChapters(id string) (model.Course, error)
	GetAll(pagination util.Pagination) []model.Course
	GetCourseIDsForUser(userID string) []string
}

type CourseService struct {
	courseRepo courseRepo
}

func NewCourseService(repo courseRepo) *CourseService {
	slog.Info("Initializing Course Service")

	return &CourseService{
		courseRepo: repo,
	}
}

func (svc *CourseService) GetByID(id string) (model.Course, error) {
	slog.Infof("Getting course by id %s", id)
	course, err := svc.courseRepo.GetByIDWithChapters(id)
	if err != nil {
		slog.Error(err)
		return model.Course{}, err	
	}

	return course, nil
}


func (svc *CourseService) Create(course model.Course, categoryIDs []string) (string, error) {
	slog.Infof("Creating course %s", course.Title)
	categories, err := svc.courseRepo.GetCategoryList(categoryIDs)
	if err != nil {
		slog.Error(err)
		return "", err
	}
	
	course.Categories = categories
	if err := svc.courseRepo.Create(&course); err != nil {
		slog.Error(err)
		return "", nil
	}

	return course.ID, nil
} 

func (svc *CourseService) GetAll(pagination util.Pagination) []model.Course {
	slog.Info("Getting all courses")
	return svc.courseRepo.GetAll(pagination)
}

func (svc *CourseService) GetCourseIDsForUser(userID string) []string {
	slog.Info("Getting a list of course IDs for user %s", userID)
	return svc.courseRepo.GetCourseIDsForUser(userID)
}