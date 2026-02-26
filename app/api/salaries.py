"""
Salaries blueprint – full CRUD for salary records.
All endpoints require JWT authentication.
"""
import os
from flask import Blueprint, request, jsonify, current_app
from flask_jwt_extended import jwt_required
from app.models.salary import Salary
from app.repositories.json_repository import JsonRepository
from app.services.salary_service import SalaryService

salaries_bp = Blueprint("salaries", __name__)


def _get_service() -> SalaryService:
    data_dir = current_app.config["DATA_DIR"]
    repo = JsonRepository[Salary](os.path.join(data_dir, "salaries.json"), Salary)
    return SalaryService(repo)


@salaries_bp.route("", methods=["GET"])
@jwt_required()
def list_salaries():
    salaries = _get_service().list_salaries()
    return jsonify({"count": len(salaries), "salaries": salaries}), 200
