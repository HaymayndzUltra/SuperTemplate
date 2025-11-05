"""
User Context Extraction Utilities
Extracts user_id, owner_id, and role from JWT token payload
"""
from typing import Dict, Any, Optional


def extract_user_context(token_payload: Dict[str, Any]) -> Dict[str, str]:
    """
    Extract user context from JWT token payload
    
    Args:
        token_payload: Decoded JWT token payload
        
    Returns:
        Dictionary with user_id, owner_id, and role
    """
    user_id = token_payload.get("sub") or token_payload.get("user_id")
    
    if not user_id:
        raise ValueError("User ID not found in token payload")
    
    # Extract role from user_metadata or app_metadata
    user_metadata = token_payload.get("user_metadata", {})
    app_metadata = token_payload.get("app_metadata", {})
    
    role = (
        user_metadata.get("role") or
        app_metadata.get("role") or
        "owner"  # Default role
    )
    
    # owner_id is the same as user_id for multi-tenancy
    # This is used in RLS policies (owner_id = auth.uid())
    owner_id = user_id
    
    return {
        "user_id": str(user_id),
        "owner_id": str(owner_id),
        "role": role,
        "email": token_payload.get("email"),
    }


def get_owner_id(request) -> Optional[str]:
    """
    Extract owner_id from request state (set by AuthMiddleware)
    
    Args:
        request: FastAPI Request object
        
    Returns:
        owner_id string or None
    """
    return getattr(request.state, "owner_id", None)


def get_user_id(request) -> Optional[str]:
    """
    Extract user_id from request state (set by AuthMiddleware)
    
    Args:
        request: FastAPI Request object
        
    Returns:
        user_id string or None
    """
    return getattr(request.state, "user_id", None)


def get_role(request) -> Optional[str]:
    """
    Extract role from request state (set by AuthMiddleware)
    
    Args:
        request: FastAPI Request object
        
    Returns:
        role string or None
    """
    return getattr(request.state, "role", None)

