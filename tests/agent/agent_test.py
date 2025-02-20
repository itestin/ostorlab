"""Agent class unit tests."""
import datetime
import json
import logging
import multiprocessing as mp
import pathlib
import time

import pytest

from ostorlab.agent import agent
from ostorlab.agent import definitions as agent_definitions
from ostorlab.agent.message import message as agent_message
from ostorlab.runtimes import definitions as runtime_definitions
from ostorlab.utils import defintions as utils_definitions

logger = logging.getLogger(__name__)


@pytest.mark.timeout(60)
@pytest.mark.docker
def testAgent_whenAnAgentSendAMessageFromStartAgent_listeningToMessageReceivesIt(mq_service, redis_service):
    """The setup of this test seems complicated, but it is the most robust implementation iteration.

    The test also tests for many things at the same time, like start and process lifecycle, message emit and message
    serialization.

    The test defines two agent, a start-only agent that sends a ping and a process-only agent the listens for pings.
    The process agent is start first as a dedicated process to start listening. Once a message is received, a
    multiprocess event is set to True.

    After 1 seconds, all processes are terminated and the event is checked.
    """
    mp_event = mp.Event()

    class StartTestAgent(agent.Agent):
        def start(self) -> None:
            self.emit('v3.healthcheck.ping', {'body': f'from test agent at {datetime.datetime.now()}'})

    class ProcessTestAgent(agent.Agent):
        def process(self, message: agent_message.Message) -> None:
            logger.info('process is called, setting event')
            mp_event.set()

    start_agent = StartTestAgent(
        agent_definitions.AgentDefinition(name='start_test_agent', out_selectors=['v3.healthcheck.ping']),
        runtime_definitions.AgentSettings(
            key='agent/ostorlab/start_test_agent',
            bus_url='amqp://guest:guest@localhost:5672/', bus_exchange_topic='ostorlab_test',
            healthcheck_port=5301,
        ))
    process_agent = ProcessTestAgent(
        agent_definitions.AgentDefinition(name='process_test_agent', in_selectors=['v3.healthcheck.ping']),
        runtime_definitions.AgentSettings(
            key='agent/ostorlab/process_test_agent',
            bus_url='amqp://guest:guest@localhost:5672/', bus_exchange_topic='ostorlab_test', healthcheck_port=5302))

    mp_event.clear()
    process_agent_t = mp.Process(target=process_agent.run)
    process_agent_t.start()
    time.sleep(1)
    start_agent_t = mp.Process(target=start_agent.run)
    start_agent_t.start()
    time.sleep(1)
    process_agent_t.terminate()
    start_agent_t.terminate()

    assert mp_event.is_set() is True


def testAgentMain_whenPassedArgsAreValid_runsAgent(mocker):
    """Test agent main with proper arguments, agent runs."""

    class SampleAgent(agent.Agent):
        """Sample agent"""

    mocker.patch('ostorlab.agent.agent.Agent.__init__', return_value=None)
    mocker.patch('ostorlab.agent.agent.Agent.run', return_value=None)
    mocker.patch.object(agent, 'AGENT_DEFINITION_PATH',
                        str(pathlib.Path(__file__).parent / 'dummyagent.yaml'))

    SampleAgent.main(['--settings',
                      str(pathlib.Path(__file__).parent / 'settings.binproto')])

    SampleAgent.run.assert_called()
    SampleAgent.__init__.assert_called()


def testAgentMain_whithNonExistingFile_exits(mocker):
    """Test agent when missing definition or settings files to ensure the command exits."""

    class SampleAgent(agent.Agent):
        """Sample agent"""

    mocker.patch('ostorlab.agent.agent.Agent.__init__', return_value=None)
    mocker.patch('ostorlab.agent.agent.Agent.run', return_value=None)
    with pytest.raises(SystemExit) as wrapper_exception:
        SampleAgent.main(['--definition',
                          'random', '--settings',
                          'random'])

        SampleAgent.run.assert_not_called()
        SampleAgent.__init__.assert_not_called()
        assert wrapper_exception.type == SystemExit
        assert wrapper_exception.value.code == 42


def testAgent_withDefaultAndSettingsArgs_retunsExpectedArgs(agent_mock):
    class TestAgent(agent.Agent):
        """Test Agent"""

    test_agent = TestAgent(
        agent_definitions.AgentDefinition(name='start_test_agent', out_selectors=['v3.healthcheck.ping'],
                                          args=[
                                              {'name': 'color', 'type': 'string', 'value': None},
                                              {'name': 'speed', 'type': 'string', 'value': b'fast'},
                                          ]),
        runtime_definitions.AgentSettings(
            key='agent/ostorlab/start_test_agent',
            bus_url='amqp://guest:guest@localhost:5672/', bus_exchange_topic='ostorlab_test',
            healthcheck_port=5301,
            args=[
                utils_definitions.Arg(name='speed', type='binary', value=b'slow'),
                utils_definitions.Arg(name='color', type='string', value=json.dumps('red').encode()),
            ]
        ))

    assert test_agent.args == {
        'color': 'red',
        'speed': b'slow'
    }
