
class Folder(dict):
    fields = ['athlete_id', 'id', 'type', 'name', 'description', 'start_date_local', 'children', 'canEdit', 'sharedWithCount', 'shareToken', 'owner', 'sharedFolderId']

    def __init__(self, **kwargs):
        for field in kwargs.keys():
            if field not in Folder.fields:
                raise TypeError("Unknown property {}".format(field))

        if kwargs.get('children') is not None:
            children = []
            for c in kwargs['children']:
                children.append(Children(**c))
            kwargs['children'] = children

        dict.__init__(self, **kwargs)
