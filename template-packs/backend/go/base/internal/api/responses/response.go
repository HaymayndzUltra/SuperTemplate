package responses

import (
	"net/http"

	"github.com/go-playground/validator/v10"
	"github.com/labstack/echo/v4"
)

type Response struct {
	Success bool        `json:"success"`
	Message string      `json:"message"`
	Data    interface{} `json:"data,omitempty"`
	Errors  interface{} `json:"errors,omitempty"`
}

type PaginatedResponse struct {
	Data interface{} `json:"data"`
	Meta PaginationMeta `json:"meta"`
}

type PaginationMeta struct {
	Page       int `json:"page"`
	Limit      int `json:"limit"`
	Total      int `json:"total"`
	TotalPages int `json:"total_pages"`
}

// Success returns a success response
func Success(c echo.Context, statusCode int, message string, data interface{}) error {
	return c.JSON(statusCode, Response{
		Success: true,
		Message: message,
		Data:    data,
	})
}

// Error returns an error response
func Error(c echo.Context, statusCode int, message string, errors interface{}) error {
	return c.JSON(statusCode, Response{
		Success: false,
		Message: message,
		Errors:  errors,
	})
}

// BadRequest returns a 400 error
func BadRequest(c echo.Context, message string) error {
	return Error(c, http.StatusBadRequest, message, nil)
}

// Unauthorized returns a 401 error
func Unauthorized(c echo.Context, message string) error {
	return Error(c, http.StatusUnauthorized, message, nil)
}

// Forbidden returns a 403 error
func Forbidden(c echo.Context, message string) error {
	return Error(c, http.StatusForbidden, message, nil)
}

// NotFound returns a 404 error
func NotFound(c echo.Context, message string) error {
	return Error(c, http.StatusNotFound, message, nil)
}

// InternalError returns a 500 error
func InternalError(c echo.Context, message string) error {
	return Error(c, http.StatusInternalServerError, message, nil)
}

// ValidationError returns validation errors
func ValidationError(c echo.Context, err error) error {
	var errors []string
	for _, err := range err.(validator.ValidationErrors) {
		errors = append(errors, err.Field() + " " + err.Tag())
	}
	return Error(c, http.StatusBadRequest, "Validation failed", errors)
}