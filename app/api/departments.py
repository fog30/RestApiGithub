"""
Departments blueprint – full CRUD for department records.
All endpoints require JWT authentication.
"""
import os
from flask import Blueprint, request, jsonify, current_app
from flask_jwt_extended import jwt_required
from app.models.department import Department
from app.repositories.json_repository import JsonRepository
from app.services.department_service import DepartmentService

departments_bp = Blueprint("departments", __name__)


def _get_service() -> DepartmentService:
    data_dir = current_app.config["DATA_DIR"]
    repo = JsonRepository[Department](os.path.join(data_dir, "departments.json"), Department)
    return DepartmentService(repo)


@departments_bp.route("", methods=["GET"])
@jwt_required()
def list_departments():
    departments = _get_service().list_departments()
    return jsonify({"count": len(departments), "departments": departments}), 200
