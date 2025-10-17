package middleware

import (
	"strings"

	"{{PROJECT_NAME}}/internal/api/responses"
	"{{PROJECT_NAME}}/internal/config"
	"{{PROJECT_NAME}}/internal/utils"

	"github.com/labstack/echo/v4"
)

type AuthMiddleware struct {
	jwtConfig config.JWTConfig
}

func NewAuthMiddleware(jwtConfig config.JWTConfig) *AuthMiddleware {
	return &AuthMiddleware{
		jwtConfig: jwtConfig,
	}
}

// Authenticate validates JWT token
func (m *AuthMiddleware) Authenticate() echo.MiddlewareFunc {
	return func(next echo.HandlerFunc) echo.HandlerFunc {
		return func(c echo.Context) error {
			// Get token from header
			authHeader := c.Request().Header.Get("Authorization")
			if authHeader == "" {
				return responses.Unauthorized(c, "Missing authorization header")
			}

			// Extract token
			tokenParts := strings.Split(authHeader, " ")
			if len(tokenParts) != 2 || tokenParts[0] != "Bearer" {
				return responses.Unauthorized(c, "Invalid authorization header format")
			}

			token := tokenParts[1]

			// Validate token
			claims, err := utils.ValidateToken(token, m.jwtConfig.Secret)
			if err != nil {
				return responses.Unauthorized(c, "Invalid or expired token")
			}

			// Set user info in context
			c.Set("user_id", claims.UserID)
			c.Set("user_email", claims.Email)
			c.Set("user_role", claims.Role)

			return next(c)
		}
	}
}

// RequireRole checks if user has required role
func (m *AuthMiddleware) RequireRole(role string) echo.MiddlewareFunc {
	return func(next echo.HandlerFunc) echo.HandlerFunc {
		return func(c echo.Context) error {
			userRole := c.Get("user_role").(string)
			
			if userRole != role {
				return responses.Forbidden(c, "Insufficient permissions")
			}

			return next(c)
		}
	}
}