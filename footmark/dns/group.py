from footmark.dns.dnsobject import TaggedDNSObject


class Group(TaggedDNSObject):
    def __init__(self, connection=None):
        super(Group, self).__init__(connection)

    def __repr__(self):
        return 'Group:%s' % self.id

    def __getattr__(self, name):
        if name == 'id':
            return self.id
        if name == 'name':
            return self.group_name
        if name == 'domain_count':
            return self.count
        raise AttributeError

    def __setattr__(self, name, value):
        if name == 'group_id':
            self.id = value
        if name == 'domain_count':
            self.count = value
        super(TaggedDNSObject, self).__setattr__(name, value)

    def get(self):
        return self.connection.describe_domain_group(group_id=self.id, group_name=self.name)

    def read(self):
        group = {}
        for name, value in list(self.__dict__.items()):
            if name in ["connection", "region_id", "region"]:
                continue
            if name == 'group_id':
                group['id'] = value
            group[name] = value
        return group

    def delete(self):
        return self.connection.delete_domain_group(group_id=self.id)

    def change_domain_group(self, group_id=None, domain_name=None):
        if group_id and domain_name:
            return self.connection.change_domain_group(group_id=group_id, domain_name=domain_name)
        return False

    def update_domain_group(self, group_id=None, group_name=None):
        if group_id and group_name and self.name != group_name:
            return self.connection.update_domain_group(group_id=group_id, group_name=group_name)
        return False