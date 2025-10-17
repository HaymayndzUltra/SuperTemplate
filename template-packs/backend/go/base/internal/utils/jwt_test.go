package utils_test

import (
	"testing"
	"time"

	"{{PROJECT_NAME}}/internal/utils"

	"github.com/stretchr/testify/assert"
)

func TestGenerateAndValidateToken(t *testing.T) {
	// Test data
	userID := uint(123)
	email := "test@example.com"
	role := "user"
	secret := "test-secret"
	duration := 1 * time.Hour

	// Generate token
	token, err := utils.GenerateToken(userID, email, role, secret, duration)
	assert.NoError(t, err)
	assert.NotEmpty(t, token)

	// Validate token
	claims, err := utils.ValidateToken(token, secret)
	assert.NoError(t, err)
	assert.NotNil(t, claims)
	assert.Equal(t, userID, claims.UserID)
	assert.Equal(t, email, claims.Email)
	assert.Equal(t, role, claims.Role)
}

func TestValidateTokenWithWrongSecret(t *testing.T) {
	// Generate token with one secret
	token, err := utils.GenerateToken(1, "test@example.com", "user", "secret1", 1*time.Hour)
	assert.NoError(t, err)

	// Try to validate with different secret
	_, err = utils.ValidateToken(token, "wrong-secret")
	assert.Error(t, err)
}

func TestValidateExpiredToken(t *testing.T) {
	// Generate token with negative duration (already expired)
	token, err := utils.GenerateToken(1, "test@example.com", "user", "secret", -1*time.Hour)
	assert.NoError(t, err)

	// Try to validate expired token
	_, err = utils.ValidateToken(token, "secret")
	assert.Error(t, err)
}