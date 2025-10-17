package handlers

import (
	"net/http"
	"strconv"

	"{{PROJECT_NAME}}/internal/api/requests"
	"{{PROJECT_NAME}}/internal/api/responses"
	"{{PROJECT_NAME}}/internal/services"

	"github.com/labstack/echo/v4"
)

type AuthHandler struct {
	authService *services.AuthService
	userService *services.UserService
}

func NewAuthHandler(authService *services.AuthService, userService *services.UserService) *AuthHandler {
	return &AuthHandler{
		authService: authService,
		userService: userService,
	}
}

// Register handles user registration
func (h *AuthHandler) Register(c echo.Context) error {
	var req requests.RegisterRequest
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
	user, err := h.userService.Create(req)
	if err != nil {
		return responses.InternalError(c, "Failed to create user")
	}

	// Generate tokens
	tokens, err := h.authService.GenerateTokens(user)
	if err != nil {
		return responses.InternalError(c, "Failed to generate tokens")
	}

	return responses.Success(c, http.StatusCreated, "User registered successfully", map[string]interface{}{
		"user":   user.ToResponse(),
		"tokens": tokens,
	})
}

// Login handles user login
func (h *AuthHandler) Login(c echo.Context) error {
	var req requests.LoginRequest
	if err := c.Bind(&req); err != nil {
		return responses.BadRequest(c, "Invalid request body")
	}

	if err := c.Validate(req); err != nil {
		return responses.ValidationError(c, err)
	}

	// Authenticate user
	user, err := h.authService.Authenticate(req.Email, req.Password)
	if err != nil {
		return responses.Unauthorized(c, "Invalid credentials")
	}

	// Generate tokens
	tokens, err := h.authService.GenerateTokens(user)
	if err != nil {
		return responses.InternalError(c, "Failed to generate tokens")
	}

	// Update last login
	h.userService.UpdateLastLogin(user.ID)

	return responses.Success(c, http.StatusOK, "Login successful", map[string]interface{}{
		"user":   user.ToResponse(),
		"tokens": tokens,
	})
}

// RefreshToken handles token refresh
func (h *AuthHandler) RefreshToken(c echo.Context) error {
	var req requests.RefreshTokenRequest
	if err := c.Bind(&req); err != nil {
		return responses.BadRequest(c, "Invalid request body")
	}

	if err := c.Validate(req); err != nil {
		return responses.ValidationError(c, err)
	}

	// Refresh tokens
	tokens, err := h.authService.RefreshTokens(req.RefreshToken)
	if err != nil {
		return responses.Unauthorized(c, "Invalid refresh token")
	}

	return responses.Success(c, http.StatusOK, "Token refreshed successfully", tokens)
}

// Logout handles user logout
func (h *AuthHandler) Logout(c echo.Context) error {
	userID := c.Get("user_id").(uint)

	// Revoke all refresh tokens
	if err := h.authService.RevokeAllRefreshTokens(userID); err != nil {
		return responses.InternalError(c, "Failed to logout")
	}

	return responses.Success(c, http.StatusOK, "Logged out successfully", nil)
}

// ChangePassword handles password change
func (h *AuthHandler) ChangePassword(c echo.Context) error {
	var req requests.ChangePasswordRequest
	if err := c.Bind(&req); err != nil {
		return responses.BadRequest(c, "Invalid request body")
	}

	if err := c.Validate(req); err != nil {
		return responses.ValidationError(c, err)
	}

	userID := c.Get("user_id").(uint)

	// Get user
	user, err := h.userService.GetByID(strconv.Itoa(int(userID)))
	if err != nil {
		return responses.NotFound(c, "User not found")
	}

	// Verify old password
	if !user.CheckPassword(req.OldPassword) {
		return responses.BadRequest(c, "Invalid old password")
	}

	// Update password
	if err := h.userService.UpdatePassword(userID, req.NewPassword); err != nil {
		return responses.InternalError(c, "Failed to update password")
	}

	// Revoke all refresh tokens
	h.authService.RevokeAllRefreshTokens(userID)

	return responses.Success(c, http.StatusOK, "Password changed successfully", nil)
}