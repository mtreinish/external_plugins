    @abc.abstractmethod
    def register_opts(self, conf):
        """Method to add additional configuration options to tempest. This
        method will be run for the plugin during the register_opts() function
        in tempest.config

        :param ConfigOpts conf: The conf object that can be used to register
            additional options on.
        """
        return

    @abc.abstractmethod
    def get_opt_lists(self):
        """Method to get a list of options for sample config generation

        :return option_list: A list of tuples with the group name and options
                             in that group.
        :rtype: list
        """
        return []
