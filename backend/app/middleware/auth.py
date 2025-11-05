"""
Authentication Middleware
Validates JWT tokens from Authorization header and extracts user context
"""
from fastapi import Request, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from starlette.middleware.base import BaseHTTPMiddleware
from typing import Optional

from app.utils.jwt import verify_token
from app.utils.user import extract_user_context


class AuthMiddleware(BaseHTTPMiddleware):
    """Middleware for JWT token validation"""
    
    def __init__(self, app, exclude_paths: Optional[list] = None):
        super().__init__(app)
        self.exclude_paths = exclude_paths or ["/health", "/docs", "/openapi.json", "/redoc"]
    
    async def dispatch(self, request: Request, call_next):
        # Skip authentication for excluded paths
        if any(request.url.path.startswith(path) for path in self.exclude_paths):
            return await call_next(request)
        
        # Extract token from Authorization header
        authorization = request.headers.get("Authorization")
        
        if not authorization:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Authorization header missing",
                headers={"WWW-Authenticate": "Bearer"},
            )
        
        # Check if Bearer token format
        if not authorization.startswith("Bearer "):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid authorization header format",
                headers={"WWW-Authenticate": "Bearer"},
            )
        
        token = authorization.split("Bearer ")[1]
        
        # Verify token
        try:
            payload = verify_token(token)
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail=f"Invalid token: {str(e)}",
                headers={"WWW-Authenticate": "Bearer"},
            )
        
        # Extract user context
        user_context = extract_user_context(payload)
        
        # Add user context to request state
        request.state.user = user_context
        request.state.user_id = user_context.get("user_id")
        request.state.owner_id = user_context.get("owner_id")
        request.state.role = user_context.get("role")
        
        response = await call_next(request)
        return response


security = HTTPBearer()

async def get_current_user(
    credentials: HTTPAuthorizationCredentials = security,
) -> dict:
    """
    Dependency function for FastAPI routes to get current user
    Usage: @app.get("/protected", dependencies=[Depends(get_current_user)])
    """
    token = credentials.credentials
    
    try:
        payload = verify_token(token)
        return extract_user_context(payload)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Invalid token: {str(e)}",
            headers={"WWW-Authenticate": "Bearer"},
        )
