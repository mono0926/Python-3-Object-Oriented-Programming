    def emails_in_groups(self, *groups):
        groups = set(groups)
        return {e for (e, g) in self.email_map.items()
                if g & groups}
