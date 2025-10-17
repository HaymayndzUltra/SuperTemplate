package services

import (
	"errors"
	"time"

	"{{PROJECT_NAME}}/internal/config"
	"{{PROJECT_NAME}}/internal/models"
	"{{PROJECT_NAME}}/internal/utils"

	"gorm.io/gorm"
)

type AuthService struct {
	db        *gorm.DB
	jwtConfig config.JWTConfig
}

func NewAuthService(db *gorm.DB, jwtConfig config.JWTConfig) *AuthService {
	return &AuthService{
		db:        db,
		jwtConfig: jwtConfig,
	}
}

type TokenResponse struct {
	AccessToken  string `json:"access_token"`
	RefreshToken string `json:"refresh_token"`
	TokenType    string `json:"token_type"`
	ExpiresIn    int    `json:"expires_in"`
}

// Authenticate validates user credentials
func (s *AuthService) Authenticate(email, password string) (*models.User, error) {
	var user models.User
	
	err := s.db.Where("email = ?", email).First(&user).Error
	if err != nil {
		return nil, errors.New("invalid credentials")
	}

	if !user.CheckPassword(password) {
		return nil, errors.New("invalid credentials")
	}

	if !user.IsActive {
		return nil, errors.New("account is inactive")
	}

	return &user, nil
}

// GenerateTokens creates access and refresh tokens
func (s *AuthService) GenerateTokens(user *models.User) (*TokenResponse, error) {
	// Generate access token
	accessToken, err := utils.GenerateToken(user.ID, user.Email, string(user.Role), s.jwtConfig.Secret, s.jwtConfig.AccessTokenDuration)
	if err != nil {
		return nil, err
	}

	// Generate refresh token
	refreshToken, err := utils.GenerateRefreshToken()
	if err != nil {
		return nil, err
	}

	// Save refresh token to database
	refreshTokenModel := &models.RefreshToken{
		UserID:    user.ID,
		Token:     refreshToken,
		ExpiresAt: time.Now().Add(s.jwtConfig.RefreshTokenDuration),
	}

	if err := s.db.Create(refreshTokenModel).Error; err != nil {
		return nil, err
	}

	return &TokenResponse{
		AccessToken:  accessToken,
		RefreshToken: refreshToken,
		TokenType:    "Bearer",
		ExpiresIn:    int(s.jwtConfig.AccessTokenDuration.Seconds()),
	}, nil
}

// RefreshTokens creates new tokens from refresh token
func (s *AuthService) RefreshTokens(refreshToken string) (*TokenResponse, error) {
	var tokenModel models.RefreshToken
	
	// Find refresh token
	err := s.db.Where("token = ?", refreshToken).First(&tokenModel).Error
	if err != nil {
		return nil, errors.New("invalid refresh token")
	}

	// Check if expired
	if tokenModel.IsExpired() {
		s.db.Delete(&tokenModel)
		return nil, errors.New("refresh token expired")
	}

	// Get user
	var user models.User
	if err := s.db.First(&user, tokenModel.UserID).Error; err != nil {
		return nil, errors.New("user not found")
	}

	// Delete old refresh token
	s.db.Delete(&tokenModel)

	// Generate new tokens
	return s.GenerateTokens(&user)
}

// RevokeAllRefreshTokens removes all refresh tokens for a user
func (s *AuthService) RevokeAllRefreshTokens(userID uint) error {
	return s.db.Where("user_id = ?", userID).Delete(&models.RefreshToken{}).Error
}