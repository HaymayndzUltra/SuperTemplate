package models

import (
	"time"

	"golang.org/x/crypto/bcrypt"
	"gorm.io/gorm"
)

type UserRole string

const (
	RoleUser  UserRole = "user"
	RoleAdmin UserRole = "admin"
)

type User struct {
	ID              uint           `json:"id" gorm:"primarykey"`
	Email           string         `json:"email" gorm:"uniqueIndex;not null"`
	Password        string         `json:"-" gorm:"not null"`
	FullName        string         `json:"full_name" gorm:"not null"`
	PhoneNumber     string         `json:"phone_number"`
	Avatar          string         `json:"avatar"`
	Role            UserRole       `json:"role" gorm:"default:user"`
	IsActive        bool           `json:"is_active" gorm:"default:true"`
	IsEmailVerified bool           `json:"is_email_verified" gorm:"default:false"`
	LastLoginAt     *time.Time     `json:"last_login_at"`
	CreatedAt       time.Time      `json:"created_at"`
	UpdatedAt       time.Time      `json:"updated_at"`
	DeletedAt       gorm.DeletedAt `json:"-" gorm:"index"`
	RefreshTokens   []RefreshToken `json:"-"`
}

// BeforeCreate hook to hash password before saving
func (u *User) BeforeCreate(tx *gorm.DB) error {
	hashedPassword, err := bcrypt.GenerateFromPassword([]byte(u.Password), bcrypt.DefaultCost)
	if err != nil {
		return err
	}
	u.Password = string(hashedPassword)
	return nil
}

// CheckPassword verifies the password
func (u *User) CheckPassword(password string) bool {
	err := bcrypt.CompareHashAndPassword([]byte(u.Password), []byte(password))
	return err == nil
}

// UpdatePassword updates the user's password
func (u *User) UpdatePassword(newPassword string) error {
	hashedPassword, err := bcrypt.GenerateFromPassword([]byte(newPassword), bcrypt.DefaultCost)
	if err != nil {
		return err
	}
	u.Password = string(hashedPassword)
	return nil
}

// UserResponse is the response struct without sensitive data
type UserResponse struct {
	ID              uint       `json:"id"`
	Email           string     `json:"email"`
	FullName        string     `json:"full_name"`
	PhoneNumber     string     `json:"phone_number,omitempty"`
	Avatar          string     `json:"avatar,omitempty"`
	Role            UserRole   `json:"role"`
	IsActive        bool       `json:"is_active"`
	IsEmailVerified bool       `json:"is_email_verified"`
	LastLoginAt     *time.Time `json:"last_login_at,omitempty"`
	CreatedAt       time.Time  `json:"created_at"`
	UpdatedAt       time.Time  `json:"updated_at"`
}

// ToResponse converts User to UserResponse
func (u *User) ToResponse() UserResponse {
	return UserResponse{
		ID:              u.ID,
		Email:           u.Email,
		FullName:        u.FullName,
		PhoneNumber:     u.PhoneNumber,
		Avatar:          u.Avatar,
		Role:            u.Role,
		IsActive:        u.IsActive,
		IsEmailVerified: u.IsEmailVerified,
		LastLoginAt:     u.LastLoginAt,
		CreatedAt:       u.CreatedAt,
		UpdatedAt:       u.UpdatedAt,
	}
}