from app.domain.entities.reaction import db, Reaction
from app.domain.repositories.base_repository import BaseRepository

class ReactionRepository(BaseRepository):

    @staticmethod
    def get_all_reactions():
        return Reaction.query.all()
        # Obtiene todos las reacciones  de la base de datos.

    @staticmethod
    def get_reactions_by_post(post_id):
        """Get all reactions for a specific post."""
        return Reaction.query.filter_by(post_id=post_id).all()
    
    @staticmethod
    def get_reactions_by_comment(comment_id):
        """Get all reactions for a specific post."""
        return Reaction.query.filter_by(comment_id=comment_id).all()
    
    @staticmethod
    def add(reaction):
        db.session.add(reaction)
        db.session.commit()
        # Añade un usuario a la base de datos y confirma la transacción.

    @staticmethod
    def update_reaction():
        db.session.commit()

    @staticmethod
    def get_reaction_by_post_and_user(post_id, user_id):
        return Reaction.query.filter_by(post_id=post_id, user_id=user_id).first()

    @staticmethod
    def get_reaction_by_comment_and_user(comment_id, user_id):
        return Reaction.query.filter_by(comment_id=comment_id, user_id=user_id).first()

    @staticmethod
    def delete_reaction(reaction):
        db.session.delete(reaction)
        db.session.commit()