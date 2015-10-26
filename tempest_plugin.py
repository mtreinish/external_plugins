@six.add_metaclass(abc.ABCMeta)
class TempestPlugin(object):
    """A TempestPlugin class provides the basic hooks for an external
    plugin to provide tempest the necessary information to run the plugin.
    """

    @abc.abstractmethod
    def load_tests(self):
        """Method to return the information necessary to load the tests in the
        plugin.

        :return: a tuple with the first value being the test_dir and the second
                 being the top_level
        :rtype: tuple
        """
        return
