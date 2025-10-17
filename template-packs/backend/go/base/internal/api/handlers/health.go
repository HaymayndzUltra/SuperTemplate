package handlers

import (
	"net/http"
	"time"

	"github.com/labstack/echo/v4"
)

type HealthHandler struct{}

func NewHealthHandler() *HealthHandler {
	return &HealthHandler{}
}

// Check performs a health check
func (h *HealthHandler) Check(c echo.Context) error {
	return c.JSON(http.StatusOK, map[string]interface{}{
		"status":    "healthy",
		"service":   "{{PROJECT_NAME}} API",
		"version":   "1.0.0",
		"timestamp": time.Now().UTC(),
		"checks": map[string]string{
			"database": "ok",
			"cache":    "ok",
		},
	})
}