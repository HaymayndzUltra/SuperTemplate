package requests

type CreateUserRequest struct {
	Email       string `json:"email" validate:"required,email"`
	Password    string `json:"password" validate:"required,min=8"`
	FullName    string `json:"full_name" validate:"required"`
	PhoneNumber string `json:"phone_number" validate:"omitempty"`
	Role        string `json:"role" validate:"omitempty,oneof=user admin"`
}

type UpdateUserRequest struct {
	Email       string `json:"email" validate:"omitempty,email"`
	FullName    string `json:"full_name" validate:"omitempty"`
	PhoneNumber string `json:"phone_number" validate:"omitempty"`
	Avatar      string `json:"avatar" validate:"omitempty"`
	Role        string `json:"role" validate:"omitempty,oneof=user admin"`
	IsActive    *bool  `json:"is_active" validate:"omitempty"`
}

type UpdateProfileRequest struct {
	FullName    string `json:"full_name" validate:"omitempty"`
	PhoneNumber string `json:"phone_number" validate:"omitempty"`
	Avatar      string `json:"avatar" validate:"omitempty"`
}