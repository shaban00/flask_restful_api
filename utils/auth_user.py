__author__ = 'Shaban Mohammedsaani Hassan [shaban00]'

class AuthUser:
    def __init__(self, ref_id, privileges=[]):
        self.ref_id = ref_id
        self.privileges = privileges
