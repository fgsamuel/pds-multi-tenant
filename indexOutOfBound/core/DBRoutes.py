class DBRoutes:
    def db_for_read(self, model, **hints):
        if model._meta.app_label== 'app_tenet1':
            return 'tenet1'
        return None



    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'app_tenet1':
            return 'tenet1'

        return None

    def allow_relation(self, obj1, obj2, **hinst):
        if obj1._meta.app_label == 'app_thenet1' or \
           obj2._meta.app_label== 'app_thenet1':
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hinst):
        if app_label == 'app_tenet1':
            return db == 'tenant1'
        return None


