from flask import Blueprint, jsonify

bp = Blueprint('main', __name__)


@bp.route('/')
def index():
    return jsonify({'message': 'Python WebApp CI/CD Pipeline - v2.0', 'status': 'running'})


@bp.route('/health')
def health():
    return jsonify({'status': 'healthy'}), 200


@bp.route('/api/info')
def info():
    return jsonify({
        'app': 'python-webapp-cicd-openshift',
        'version': '1.0.0',
        'environment': 'production'
    })
