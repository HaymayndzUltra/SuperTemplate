package handlers_test

import (
	"net/http"
	"net/http/httptest"
	"testing"

	"{{PROJECT_NAME}}/internal/api/handlers"

	"github.com/labstack/echo/v4"
	"github.com/stretchr/testify/assert"
)

func TestHealthCheck(t *testing.T) {
	// Setup
	e := echo.New()
	req := httptest.NewRequest(http.MethodGet, "/health", nil)
	rec := httptest.NewRecorder()
	c := e.NewContext(req, rec)

	// Create handler
	h := handlers.NewHealthHandler()

	// Test
	if assert.NoError(t, h.Check(c)) {
		assert.Equal(t, http.StatusOK, rec.Code)
		assert.Contains(t, rec.Body.String(), "healthy")
		assert.Contains(t, rec.Body.String(), "{{PROJECT_NAME}} API")
	}
}