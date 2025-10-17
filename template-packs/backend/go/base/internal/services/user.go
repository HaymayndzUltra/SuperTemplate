package services

import (
	"errors"
	"strconv"
	"time"

	"{{PROJECT_NAME}}/internal/api/requests"
	"{{PROJECT_NAME}}/internal/api/responses"
	"{{PROJECT_NAME}}/internal/models"

	"gorm.io/gorm"
)

type UserService struct {
	db *gorm.DB
}

func NewUserService(db *gorm.DB) *UserService {
	return &UserService{
		db: db,
	}
}

// GetAll retrieves all users with pagination
func (s *UserService) GetAll(page, limit int, search, isActive, role string) (*responses.PaginatedResponse, error) {
	var users []models.User
	var total int64

	query := s.db.Model(&models.User{})

	// Apply filters
	if search != "" {
		query = query.Where("email LIKE ? OR full_name LIKE ?", "%"+search+"%", "%"+search+"%")
	}

	if isActive != "" {
		active, _ := strconv.ParseBool(isActive)
		query = query.Where("is_active = ?", active)
	}

	if role != "" {
		query = query.Where("role = ?", role)
	}

	// Count total
	query.Count(&total)

	// Apply pagination
	offset := (page - 1) * limit
	err := query.Offset(offset).Limit(limit).Order("created_at DESC").Find(&users).Error
	if err != nil {
		return nil, err
	}

	// Convert to response
	var userResponses []models.UserResponse
	for _, user := range users {
		userResponses = append(userResponses, user.ToResponse())
	}

	totalPages := int(total) / limit
	if int(total)%limit != 0 {
		totalPages++
	}

	return &responses.PaginatedResponse{
		Data: userResponses,
		Meta: responses.PaginationMeta{
			Page:       page,
			Limit:      limit,
			Total:      int(total),
			TotalPages: totalPages,
		},
	}, nil
}

// GetByID retrieves a user by ID
func (s *UserService) GetByID(id string) (*models.User, error) {
	var user models.User
	
	err := s.db.First(&user, id).Error
	if err != nil {
		if errors.Is(err, gorm.ErrRecordNotFound) {
			return nil, errors.New("user not found")
		}
		return nil, err
	}

	return &user, nil
}

// GetByEmail retrieves a user by email
func (s *UserService) GetByEmail(email string) (*models.User, error) {
	var user models.User
	
	err := s.db.Where("email = ?", email).First(&user).Error
	if err != nil {
		if errors.Is(err, gorm.ErrRecordNotFound) {
			return nil, nil
		}
		return nil, err
	}

	return &user, nil
}

// Create creates a new user
func (s *UserService) Create(req requests.RegisterRequest) (*models.User, error) {
	user := &models.User{
		Email:    req.Email,
		Password: req.Password,
		FullName: req.FullName,
		Role:     models.RoleUser,
	}

	if err := s.db.Create(user).Error; err != nil {
		return nil, err
	}

	return user, nil
}

// Update updates a user
func (s *UserService) Update(id string, req requests.UpdateUserRequest) (*models.User, error) {
	user, err := s.GetByID(id)
	if err != nil {
		return nil, err
	}

	// Update fields
	if req.Email != "" {
		user.Email = req.Email
	}
	if req.FullName != "" {
		user.FullName = req.FullName
	}
	if req.PhoneNumber != "" {
		user.PhoneNumber = req.PhoneNumber
	}
	if req.Avatar != "" {
		user.Avatar = req.Avatar
	}
	if req.Role != "" {
		user.Role = models.UserRole(req.Role)
	}
	if req.IsActive != nil {
		user.IsActive = *req.IsActive
	}

	if err := s.db.Save(user).Error; err != nil {
		return nil, err
	}

	return user, nil
}

// UpdatePassword updates user password
func (s *UserService) UpdatePassword(userID uint, newPassword string) error {
	user, err := s.GetByID(strconv.Itoa(int(userID)))
	if err != nil {
		return err
	}

	if err := user.UpdatePassword(newPassword); err != nil {
		return err
	}

	return s.db.Save(user).Error
}

// UpdateLastLogin updates user's last login time
func (s *UserService) UpdateLastLogin(userID uint) error {
	now := time.Now()
	return s.db.Model(&models.User{}).Where("id = ?", userID).Update("last_login_at", &now).Error
}

// Delete deletes a user
func (s *UserService) Delete(id string) error {
	result := s.db.Delete(&models.User{}, id)
	if result.Error != nil {
		return result.Error
	}
	if result.RowsAffected == 0 {
		return errors.New("user not found")
	}
	return nil
}