#!/usr/bin/env python3
"""
Authentication module
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """Template class for authentication system """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Method to determine if authentication is required """
        return False

    def authorization_header(self, request=None) -> str:
        """ Method to get the authorization header """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Method to get the current user"""
        return None
