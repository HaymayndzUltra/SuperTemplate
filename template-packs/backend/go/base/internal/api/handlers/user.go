package handlers

import (
	"net/http"
	"strconv"

	"{{PROJECT_NAME}}/internal/api/requests"
	"{{PROJECT_NAME}}/internal/api/responses"
	"{{PROJECT_NAME}}/internal/services"

	"github.com/labstack/echo/v4"
)

type UserHandler struct {
	userService *services.UserService
}

func NewUserHandler(userService *services.UserService) *UserHandler {
	return &UserHandler{
		userService: userService,
	}
}

// GetAll retrieves all users
func (h *UserHandler) GetAll(c echo.Context) error {
	// Parse query parameters
	page, _ := strconv.Atoi(c.QueryParam("page"))
	if page < 1 {
		page = 1
	}
	
	limit, _ := strconv.Atoi(c.QueryParam("limit"))
	if limit < 1 {
		limit = 10
	}

	search := c.QueryParam("search")
	isActive := c.QueryParam("is_active")
	role := c.QueryParam("role")

	// Get users with pagination
	result, err := h.userService.GetAll(page, limit, search, isActive, role)
	if err != nil {
		return responses.InternalError(c, "Failed to fetch users")
	}

	return responses.Success(c, http.StatusOK, "Users retrieved successfully", result)
}

// GetByID retrieves a user by ID
func (h *UserHandler) GetByID(c echo.Context) error {
	id := c.Param("id")
	
	user, err := h.userService.GetByID(id)
	if err != nil {
		return responses.NotFound(c, "User not found")
	}

	return responses.Success(c, http.StatusOK, "User retrieved successfully", user.ToResponse())
}

// GetProfile retrieves the current user's profile
func (h *UserHandler) GetProfile(c echo.Context) error {
	userID := c.Get("user_id").(uint)
	
	user, err := h.userService.GetByID(strconv.Itoa(int(userID)))
	if err != nil {
		return responses.NotFound(c, "User not found")
	}

	return responses.Success(c, http.StatusOK, "Profile retrieved successfully", user.ToResponse())
}

// Create creates a new user (admin only)
func (h *UserHandler) Create(c echo.Context) error {
	var req requests.CreateUserRequest
	if err := c.Bind(&req); err != nil {
		return responses.BadRequest(c, "Invalid request body")
	}

	if err := c.Validate(req); err != nil {
		return responses.ValidationError(c, err)
	}

	// Check if user already exists
	existingUser, _ := h.userService.GetByEmail(req.Email)
	if existingUser != nil {
		return responses.BadRequest(c, "User with this email already exists")
	}

	// Create user
	user, err := h.userService.Create(requests.RegisterRequest{
		Email:    req.Email,
		Password: req.Password,
		FullName: req.FullName,
	})
	if err != nil {
		return responses.InternalError(c, "Failed to create user")
	}

	return responses.Success(c, http.StatusCreated, "User created successfully", user.ToResponse())
}

// Update updates a user (admin only)
func (h *UserHandler) Update(c echo.Context) error {
	id := c.Param("id")
	
	var req requests.UpdateUserRequest
	if err := c.Bind(&req); err != nil {
		return responses.BadRequest(c, "Invalid request body")
	}

	if err := c.Validate(req); err != nil {
		return responses.ValidationError(c, err)
	}

	// Update user
	user, err := h.userService.Update(id, req)
	if err != nil {
		if err.Error() == "user not found" {
			return responses.NotFound(c, "User not found")
		}
		return responses.InternalError(c, "Failed to update user")
	}

	return responses.Success(c, http.StatusOK, "User updated successfully", user.ToResponse())
}

// UpdateProfile updates the current user's profile
func (h *UserHandler) UpdateProfile(c echo.Context) error {
	userID := c.Get("user_id").(uint)
	
	var req requests.UpdateProfileRequest
	if err := c.Bind(&req); err != nil {
		return responses.BadRequest(c, "Invalid request body")
	}

	if err := c.Validate(req); err != nil {
		return responses.ValidationError(c, err)
	}

	// Convert to update user request
	updateReq := requests.UpdateUserRequest{
		FullName:    req.FullName,
		PhoneNumber: req.PhoneNumber,
		Avatar:      req.Avatar,
	}

	// Update user
	user, err := h.userService.Update(strconv.Itoa(int(userID)), updateReq)
	if err != nil {
		return responses.InternalError(c, "Failed to update profile")
	}

	return responses.Success(c, http.StatusOK, "Profile updated successfully", user.ToResponse())
}

// Delete deletes a user (admin only)
func (h *UserHandler) Delete(c echo.Context) error {
	id := c.Param("id")
	
	if err := h.userService.Delete(id); err != nil {
		if err.Error() == "user not found" {
			return responses.NotFound(c, "User not found")
		}
		return responses.InternalError(c, "Failed to delete user")
	}

	return responses.Success(c, http.StatusOK, "User deleted successfully", nil)
}