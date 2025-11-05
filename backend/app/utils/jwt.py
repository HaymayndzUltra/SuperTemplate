"""
JWT Token Validation Utilities
Validates Supabase JWT tokens and extracts claims
"""
import os
from typing import Optional, Dict, Any
from jose import jwt, JWTError
from datetime import datetime


# Supabase JWT secret from environment
SUPABASE_JWT_SECRET = os.getenv("SUPABASE_JWT_SECRET")

if not SUPABASE_JWT_SECRET:
    raise ValueError("SUPABASE_JWT_SECRET environment variable is required")


def verify_token(token: str) -> Dict[str, Any]:
    """
    Verify JWT token signature and expiration
    
    Args:
        token: JWT token string
        
    Returns:
        Decoded token payload
        
    Raises:
        JWTError: If token is invalid or expired
    """
    try:
        # Verify using HS256 with JWT secret
        # Note: Supabase uses RS256 by default, but we can configure it to use HS256
        # For now, using HS256 with JWT secret for simplicity
        payload = jwt.decode(
            token,
            SUPABASE_JWT_SECRET,
            algorithms=["HS256"],
            options={
                "verify_signature": True,
                "verify_exp": True,
                "verify_iat": True,
            },
        )
        
        # Check expiration
        exp = payload.get("exp")
        if exp and datetime.fromtimestamp(exp) < datetime.utcnow():
            raise JWTError("Token has expired")
        
        return payload
        
    except JWTError as e:
        raise JWTError(f"Token validation failed: {str(e)}")
    except Exception as e:
        raise JWTError(f"Token verification error: {str(e)}")


def decode_token(token: str) -> Dict[str, Any]:
    """
    Decode JWT token without verification (for debugging only)
    
    Args:
        token: JWT token string
        
    Returns:
        Decoded token payload (unverified)
    """
    return jwt.decode(token, options={"verify_signature": False})

