package utils

import (
	"crypto/rand"
	"encoding/hex"
)

// GenerateRefreshToken creates a secure random refresh token
func GenerateRefreshToken() (string, error) {
	bytes := make([]byte, 32)
	if _, err := rand.Read(bytes); err != nil {
		return "", err
	}
	return hex.EncodeToString(bytes), nil
}