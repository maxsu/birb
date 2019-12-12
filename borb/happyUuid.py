import uuid


class hasId:
    """ Gives each instance of a subclass a random uuid

    self.id:   fetches values
    self._id:  store
    """
    @property
    def id(self):
        try:
            return self._id
        except AttributeError:
            self._id = uuid.uuid4().hex
            return self._id
