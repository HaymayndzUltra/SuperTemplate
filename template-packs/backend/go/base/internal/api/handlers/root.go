package handlers

import (
	"net/http"

	"github.com/labstack/echo/v4"
)

// Root handler for the root endpoint
func Root(c echo.Context) error {
	return c.JSON(http.StatusOK, map[string]interface{}{
		"name":        "{{PROJECT_NAME}} API",
		"version":     "1.0.0",
		"description": "{{INDUSTRY}} {{PROJECT_TYPE}} API",
		"health":      "/health",
		"docs":        "/api/docs",
	})
}