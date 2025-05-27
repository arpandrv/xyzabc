class MangoAppRouter:
    """
    A router to control database operations for mango_app.
    This router prevents mango_app from performing any database operations.
    """
    
    def db_for_read(self, model, **hints):
        """Suggest the database to read from."""
        if model._meta.app_label == 'mango_app':
            return None  # Don't allow database reads
        return None  # Use default for other apps
    
    def db_for_write(self, model, **hints):
        """Suggest the database to write to."""
        if model._meta.app_label == 'mango_app':
            return None  # Don't allow database writes
        return None  # Use default for other apps
    
    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """Ensure that mango_app models don't get migrated."""
        if app_label == 'mango_app':
            return False  # Don't create tables for mango_app
        return None  # Use default for other apps
    
    def allow_relation(self, obj1, obj2, **hints):
        """Allow relations if models are in the same app."""
        # This method controls whether a relation is allowed between two objects
        return None  # Use default behavior 