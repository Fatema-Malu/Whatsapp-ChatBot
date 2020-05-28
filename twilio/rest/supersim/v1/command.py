# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base import deserialize
from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.page import Page


class CommandList(ListResource):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version):
        """
        Initialize the CommandList

        :param Version version: Version that contains the resource

        :returns: twilio.rest.supersim.v1.command.CommandList
        :rtype: twilio.rest.supersim.v1.command.CommandList
        """
        super(CommandList, self).__init__(version)

        # Path Solution
        self._solution = {}
        self._uri = '/Commands'.format(**self._solution)

    def create(self, sim, command, callback_method=values.unset,
               callback_url=values.unset):
        """
        Create the CommandInstance

        :param unicode sim: The sid or unique_name of the SIM to send the Command to
        :param unicode command: The message body of the command
        :param unicode callback_method: The HTTP method we should use to call callback_url
        :param unicode callback_url: The URL we should call after we have sent the command

        :returns: The created CommandInstance
        :rtype: twilio.rest.supersim.v1.command.CommandInstance
        """
        data = values.of({
            'Sim': sim,
            'Command': command,
            'CallbackMethod': callback_method,
            'CallbackUrl': callback_url,
        })

        payload = self._version.create(method='POST', uri=self._uri, data=data, )

        return CommandInstance(self._version, payload, )

    def stream(self, sim=values.unset, status=values.unset, direction=values.unset,
               limit=None, page_size=None):
        """
        Streams CommandInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param unicode sim: The SID or unique name of the Sim that Command was sent to or from.
        :param CommandInstance.Status status: The status of the Command
        :param CommandInstance.Direction direction: The direction of the Command
        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.supersim.v1.command.CommandInstance]
        """
        limits = self._version.read_limits(limit, page_size)

        page = self.page(sim=sim, status=status, direction=direction, page_size=limits['page_size'], )

        return self._version.stream(page, limits['limit'], limits['page_limit'])

    def list(self, sim=values.unset, status=values.unset, direction=values.unset,
             limit=None, page_size=None):
        """
        Lists CommandInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param unicode sim: The SID or unique name of the Sim that Command was sent to or from.
        :param CommandInstance.Status status: The status of the Command
        :param CommandInstance.Direction direction: The direction of the Command
        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.supersim.v1.command.CommandInstance]
        """
        return list(self.stream(
            sim=sim,
            status=status,
            direction=direction,
            limit=limit,
            page_size=page_size,
        ))

    def page(self, sim=values.unset, status=values.unset, direction=values.unset,
             page_token=values.unset, page_number=values.unset,
             page_size=values.unset):
        """
        Retrieve a single page of CommandInstance records from the API.
        Request is executed immediately

        :param unicode sim: The SID or unique name of the Sim that Command was sent to or from.
        :param CommandInstance.Status status: The status of the Command
        :param CommandInstance.Direction direction: The direction of the Command
        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of CommandInstance
        :rtype: twilio.rest.supersim.v1.command.CommandPage
        """
        data = values.of({
            'Sim': sim,
            'Status': status,
            'Direction': direction,
            'PageToken': page_token,
            'Page': page_number,
            'PageSize': page_size,
        })

        response = self._version.page(method='GET', uri=self._uri, params=data, )

        return CommandPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of CommandInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of CommandInstance
        :rtype: twilio.rest.supersim.v1.command.CommandPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url,
        )

        return CommandPage(self._version, response, self._solution)

    def get(self, sid):
        """
        Constructs a CommandContext

        :param sid: The SID that identifies the resource to fetch

        :returns: twilio.rest.supersim.v1.command.CommandContext
        :rtype: twilio.rest.supersim.v1.command.CommandContext
        """
        return CommandContext(self._version, sid=sid, )

    def __call__(self, sid):
        """
        Constructs a CommandContext

        :param sid: The SID that identifies the resource to fetch

        :returns: twilio.rest.supersim.v1.command.CommandContext
        :rtype: twilio.rest.supersim.v1.command.CommandContext
        """
        return CommandContext(self._version, sid=sid, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Supersim.V1.CommandList>'


class CommandPage(Page):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, response, solution):
        """
        Initialize the CommandPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API

        :returns: twilio.rest.supersim.v1.command.CommandPage
        :rtype: twilio.rest.supersim.v1.command.CommandPage
        """
        super(CommandPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of CommandInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.supersim.v1.command.CommandInstance
        :rtype: twilio.rest.supersim.v1.command.CommandInstance
        """
        return CommandInstance(self._version, payload, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Supersim.V1.CommandPage>'


class CommandContext(InstanceContext):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, sid):
        """
        Initialize the CommandContext

        :param Version version: Version that contains the resource
        :param sid: The SID that identifies the resource to fetch

        :returns: twilio.rest.supersim.v1.command.CommandContext
        :rtype: twilio.rest.supersim.v1.command.CommandContext
        """
        super(CommandContext, self).__init__(version)

        # Path Solution
        self._solution = {'sid': sid, }
        self._uri = '/Commands/{sid}'.format(**self._solution)

    def fetch(self):
        """
        Fetch the CommandInstance

        :returns: The fetched CommandInstance
        :rtype: twilio.rest.supersim.v1.command.CommandInstance
        """
        payload = self._version.fetch(method='GET', uri=self._uri, )

        return CommandInstance(self._version, payload, sid=self._solution['sid'], )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Supersim.V1.CommandContext {}>'.format(context)


class CommandInstance(InstanceResource):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    class Status(object):
        QUEUED = "queued"
        SENT = "sent"
        DELIVERED = "delivered"
        RECEIVED = "received"
        FAILED = "failed"

    class Direction(object):
        TO_SIM = "to_sim"
        FROM_SIM = "from_sim"

    def __init__(self, version, payload, sid=None):
        """
        Initialize the CommandInstance

        :returns: twilio.rest.supersim.v1.command.CommandInstance
        :rtype: twilio.rest.supersim.v1.command.CommandInstance
        """
        super(CommandInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'sid': payload.get('sid'),
            'account_sid': payload.get('account_sid'),
            'sim_sid': payload.get('sim_sid'),
            'command': payload.get('command'),
            'status': payload.get('status'),
            'direction': payload.get('direction'),
            'date_created': deserialize.iso8601_datetime(payload.get('date_created')),
            'date_updated': deserialize.iso8601_datetime(payload.get('date_updated')),
            'url': payload.get('url'),
        }

        # Context
        self._context = None
        self._solution = {'sid': sid or self._properties['sid'], }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: CommandContext for this CommandInstance
        :rtype: twilio.rest.supersim.v1.command.CommandContext
        """
        if self._context is None:
            self._context = CommandContext(self._version, sid=self._solution['sid'], )
        return self._context

    @property
    def sid(self):
        """
        :returns: The unique string that identifies the resource
        :rtype: unicode
        """
        return self._properties['sid']

    @property
    def account_sid(self):
        """
        :returns: The SID of the Account that created the resource
        :rtype: unicode
        """
        return self._properties['account_sid']

    @property
    def sim_sid(self):
        """
        :returns: The SID of the SIM that this Command was sent to or from
        :rtype: unicode
        """
        return self._properties['sim_sid']

    @property
    def command(self):
        """
        :returns: The message body of the command sent to or from the SIM
        :rtype: unicode
        """
        return self._properties['command']

    @property
    def status(self):
        """
        :returns: The status of the Command
        :rtype: CommandInstance.Status
        """
        return self._properties['status']

    @property
    def direction(self):
        """
        :returns: The direction of the Command
        :rtype: CommandInstance.Direction
        """
        return self._properties['direction']

    @property
    def date_created(self):
        """
        :returns: The ISO 8601 date and time in GMT when the resource was created
        :rtype: datetime
        """
        return self._properties['date_created']

    @property
    def date_updated(self):
        """
        :returns: The ISO 8601 date and time in GMT when the resource was last updated
        :rtype: datetime
        """
        return self._properties['date_updated']

    @property
    def url(self):
        """
        :returns: The absolute URL of the Command resource
        :rtype: unicode
        """
        return self._properties['url']

    def fetch(self):
        """
        Fetch the CommandInstance

        :returns: The fetched CommandInstance
        :rtype: twilio.rest.supersim.v1.command.CommandInstance
        """
        return self._proxy.fetch()

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Supersim.V1.CommandInstance {}>'.format(context)
