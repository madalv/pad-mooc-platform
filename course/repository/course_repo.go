package repository

import (
	"course/model"
	"course/storage"
	"course/util"

	"github.com/gookit/slog"
	"gorm.io/gorm"
)

type CourseRepository struct {
	db *gorm.DB
}

func NewCourseRepository(db *gorm.DB) *CourseRepository {
	slog.Info("Initializing Course Repository")

	return &CourseRepository{
		db: db,
	}
}

func (r *CourseRepository) CreateWithCategories(course *model.Course, categoryIDs []string) error {
	// find the categories that
	var categories []*model.Category
	if err := r.db.Where("id IN (?)", categoryIDs).Find(&categories).Error; err != nil {
		return err
	}

	course.Categories = categories
	return r.db.Create(course).Error
}

func (r *CourseRepository) GetByID(id string) (model.Course, error) {
	var course model.Course
	err := r.db.First(&course, "id = ?", id).Error
	return course, err
}

func (r *CourseRepository) GetAll(pagination util.Pagination) []model.Course {
	var petitions []model.Course

	r.db.Scopes(storage.Paginate(pagination)).Preload("Categories").Find(&petitions)
	return petitions
}

func (r *CourseRepository) GetCourseIDsForUser(userID string) []string {
	var courseIDs []string
	r.db.Model(&model.Enrollment{}).
		Where("user_id = ?", userID).
		Pluck("course_id", &courseIDs)

	return courseIDs
}
