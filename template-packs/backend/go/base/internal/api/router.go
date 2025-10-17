package api

import (
	"{{PROJECT_NAME}}/internal/api/handlers"
	"{{PROJECT_NAME}}/internal/api/middleware"
	"{{PROJECT_NAME}}/internal/config"
	"{{PROJECT_NAME}}/internal/models"
	"{{PROJECT_NAME}}/internal/services"

	"github.com/labstack/echo/v4"
	"gorm.io/gorm"
)

// SetupRoutes configures all API routes
func SetupRoutes(e *echo.Echo, db *gorm.DB, cfg *config.Config) {
	// Setup validator
	SetupValidator(e)
	// Initialize services
	userService := services.NewUserService(db)
	authService := services.NewAuthService(db, cfg.JWT)

	// Initialize handlers
	healthHandler := handlers.NewHealthHandler()
	authHandler := handlers.NewAuthHandler(authService, userService)
	userHandler := handlers.NewUserHandler(userService)

	// Initialize middleware
	authMiddleware := middleware.NewAuthMiddleware(cfg.JWT)

	// API v1 group
	v1 := e.Group("/api/v1")

	// Public routes
	e.GET("/", handlers.Root)
	e.GET("/health", healthHandler.Check)

	// Auth routes (public)
	auth := v1.Group("/auth")
	auth.POST("/register", authHandler.Register)
	auth.POST("/login", authHandler.Login)
	auth.POST("/refresh", authHandler.RefreshToken)

	// Protected auth routes
	authProtected := auth.Group("")
	authProtected.Use(authMiddleware.Authenticate())
	authProtected.POST("/logout", authHandler.Logout)
	authProtected.POST("/change-password", authHandler.ChangePassword)

	// User routes (protected)
	users := v1.Group("/users")
	users.Use(authMiddleware.Authenticate())
	users.GET("", userHandler.GetAll, authMiddleware.RequireRole(string(models.RoleAdmin)))
	users.POST("", userHandler.Create, authMiddleware.RequireRole(string(models.RoleAdmin)))
	users.GET("/me", userHandler.GetProfile)
	users.PUT("/me", userHandler.UpdateProfile)
	users.GET("/:id", userHandler.GetByID, authMiddleware.RequireRole(string(models.RoleAdmin)))
	users.PUT("/:id", userHandler.Update, authMiddleware.RequireRole(string(models.RoleAdmin)))
	users.DELETE("/:id", userHandler.Delete, authMiddleware.RequireRole(string(models.RoleAdmin)))
}