from flask import Blueprint, jsonify, request
from app.domain.services.reaction_service import ReactionService

reaction_api = Blueprint('reaction_api', 'reaction_api', url_prefix='/api/reactions')

error_reaction = 'Reaction not found'

@reaction_api.route('/', methods=['GET'])
def get_reactions():
    reactions = ReactionService.get_all_reactions()
    return jsonify([reaction.to_dict() for reaction in reactions])

@reaction_api.route('/post/<int:post_id>', methods=['GET'])
def get_reactions_by_post(post_id):
    reactions = ReactionService.get_reactions_by_post(post_id)
    if reactions:
        return jsonify([reaction.to_dict() for reaction in reactions])
    return jsonify({'error': error_reaction}), 404

@reaction_api.route('/comment/<int:comment_id>', methods=['GET'])
def get_reactions_by_comment(comment_id):
    reactions = ReactionService.get_reactions_by_comment(comment_id)
    if reactions:
        return jsonify([reaction.to_dict() for reaction in reactions])
    return jsonify({'error': error_reaction}), 404

@reaction_api.route('/', methods=['POST'])
def create_reaction():
    data = request.json
    new_reaction = ReactionService.create_reaction(
        data.get('user_id'),
        data.get('type'),
        data.get('post_id'),
        data.get('comment_id')
    )
    return jsonify(new_reaction.to_dict()), 201

@reaction_api.route('/post/<int:post_id>/user/<int:user_id>', methods=['PUT'])
def update_reaction_by_post_and_user(post_id, user_id):
    data = request.json
    updated_reaction, error_reaction = ReactionService.update_reaction_by_post_and_user(post_id, user_id, data)

    if updated_reaction:
        return jsonify(updated_reaction.to_dict()), 200

    return jsonify({'error': error_reaction}), 404

@reaction_api.route('/comment/<int:comment_id>/user/<int:user_id>', methods=['PUT'])
def update_reaction_by_comment_and_user(comment_id, user_id):
    data = request.json
    updated_reaction, error_reaction = ReactionService.update_reaction_by_comment_and_user(comment_id, user_id, data)

    if updated_reaction:
        return jsonify(updated_reaction.to_dict()), 200

    return jsonify({'error': error_reaction}), 404

@reaction_api.route('/<int:post_id>', methods=['DELETE'])
def delete_reaction_in_post(post_id, user_id):
    success, error_reaction = ReactionService.delete_reaction_by_post_and_user(post_id, user_id)
    if success:
        return jsonify({'message': 'Reaction deleted successfully'}), 200
    return jsonify({'error': error_reaction}), 404

@reaction_api.route('/comment/<int:comment_id>/<int:user_id>', methods=['DELETE'])
def delete_reaction_in_comment(comment_id, user_id):
    success, error_reaction = ReactionService.delete_reaction_by_comment_and_user(comment_id, user_id)
    if success:
        return jsonify({'message': 'Reaction deleted successfully'}), 200
    return jsonify({'error': error_reaction}), 404