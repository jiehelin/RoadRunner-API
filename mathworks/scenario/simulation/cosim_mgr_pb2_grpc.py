# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from mathworks.scenario.simulation import cosim_pb2 as mathworks_dot_scenario_dot_simulation_dot_cosim__pb2
from mathworks.scenario.simulation import event_pb2 as mathworks_dot_scenario_dot_simulation_dot_event__pb2

GRPC_GENERATED_VERSION = '1.67.1'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in mathworks/scenario/simulation/cosim_mgr_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class CoSimulationMgrStub(object):
    """gRPC service interface for management of multiple co-simulations
    ////////////////////////////////////
    Client connection and subscriptions
    ////////////////////////////////////
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.RegisterClient = channel.unary_unary(
                '/mathworks.scenario.simulation.CoSimulationMgr/RegisterClient',
                request_serializer=mathworks_dot_scenario_dot_simulation_dot_cosim__pb2.RegisterClientRequest.SerializeToString,
                response_deserializer=mathworks_dot_scenario_dot_simulation_dot_cosim__pb2.RegisterClientResponse.FromString,
                _registered_method=True)
        self.SetReady = channel.unary_unary(
                '/mathworks.scenario.simulation.CoSimulationMgr/SetReady',
                request_serializer=mathworks_dot_scenario_dot_simulation_dot_cosim__pb2.SetReadyRequest.SerializeToString,
                response_deserializer=mathworks_dot_scenario_dot_simulation_dot_cosim__pb2.SetReadyResponse.FromString,
                _registered_method=True)
        self.SetBusy = channel.unary_unary(
                '/mathworks.scenario.simulation.CoSimulationMgr/SetBusy',
                request_serializer=mathworks_dot_scenario_dot_simulation_dot_cosim__pb2.SetBusyRequest.SerializeToString,
                response_deserializer=mathworks_dot_scenario_dot_simulation_dot_cosim__pb2.SetBusyResponse.FromString,
                _registered_method=True)
        self.SubscribeEvents = channel.unary_stream(
                '/mathworks.scenario.simulation.CoSimulationMgr/SubscribeEvents',
                request_serializer=mathworks_dot_scenario_dot_simulation_dot_cosim__pb2.SubscribeEventsRequest.SerializeToString,
                response_deserializer=mathworks_dot_scenario_dot_simulation_dot_event__pb2.Event.FromString,
                _registered_method=True)
        self.AddSimulations = channel.unary_unary(
                '/mathworks.scenario.simulation.CoSimulationMgr/AddSimulations',
                request_serializer=mathworks_dot_scenario_dot_simulation_dot_cosim__pb2.AddSimulationsRequest.SerializeToString,
                response_deserializer=mathworks_dot_scenario_dot_simulation_dot_cosim__pb2.AddSimulationsResponse.FromString,
                _registered_method=True)
        self.RemoveSimulations = channel.unary_unary(
                '/mathworks.scenario.simulation.CoSimulationMgr/RemoveSimulations',
                request_serializer=mathworks_dot_scenario_dot_simulation_dot_cosim__pb2.RemoveSimulationsRequest.SerializeToString,
                response_deserializer=mathworks_dot_scenario_dot_simulation_dot_cosim__pb2.RemoveSimulationsResponse.FromString,
                _registered_method=True)
        self.GetSimulationServiceProfiles = channel.unary_unary(
                '/mathworks.scenario.simulation.CoSimulationMgr/GetSimulationServiceProfiles',
                request_serializer=mathworks_dot_scenario_dot_simulation_dot_cosim__pb2.GetSimulationServiceProfilesRequest.SerializeToString,
                response_deserializer=mathworks_dot_scenario_dot_simulation_dot_cosim__pb2.GetSimulationServiceProfilesResponse.FromString,
                _registered_method=True)
        self.LaunchSimulations = channel.unary_unary(
                '/mathworks.scenario.simulation.CoSimulationMgr/LaunchSimulations',
                request_serializer=mathworks_dot_scenario_dot_simulation_dot_cosim__pb2.LaunchSimulationsRequest.SerializeToString,
                response_deserializer=mathworks_dot_scenario_dot_simulation_dot_cosim__pb2.LaunchSimulationsResponse.FromString,
                _registered_method=True)


class CoSimulationMgrServicer(object):
    """gRPC service interface for management of multiple co-simulations
    ////////////////////////////////////
    Client connection and subscriptions
    ////////////////////////////////////
    """

    def RegisterClient(self, request, context):
        """Initialization function where a calling client is assigned an id.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetReady(self, request, context):
        """Register the calling client as ready to proceed with the next update.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetBusy(self, request, context):
        """Notify that the client is alive and busy
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SubscribeEvents(self, request, context):
        """Register the calling client to receive events.
        Note that this is a long-lived stream, and persists until the client or the server shuts down.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddSimulations(self, request, context):
        """////////////////////////////////////
        Co-simulation management interface
        ////////////////////////////////////

        Add scenario simulations
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RemoveSimulations(self, request, context):
        """Remove scenario simulations
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetSimulationServiceProfiles(self, request, context):
        """Get the currently added simulations
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def LaunchSimulations(self, request, context):
        """Launch batch simulations
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_CoSimulationMgrServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'RegisterClient': grpc.unary_unary_rpc_method_handler(
                    servicer.RegisterClient,
                    request_deserializer=mathworks_dot_scenario_dot_simulation_dot_cosim__pb2.RegisterClientRequest.FromString,
                    response_serializer=mathworks_dot_scenario_dot_simulation_dot_cosim__pb2.RegisterClientResponse.SerializeToString,
            ),
            'SetReady': grpc.unary_unary_rpc_method_handler(
                    servicer.SetReady,
                    request_deserializer=mathworks_dot_scenario_dot_simulation_dot_cosim__pb2.SetReadyRequest.FromString,
                    response_serializer=mathworks_dot_scenario_dot_simulation_dot_cosim__pb2.SetReadyResponse.SerializeToString,
            ),
            'SetBusy': grpc.unary_unary_rpc_method_handler(
                    servicer.SetBusy,
                    request_deserializer=mathworks_dot_scenario_dot_simulation_dot_cosim__pb2.SetBusyRequest.FromString,
                    response_serializer=mathworks_dot_scenario_dot_simulation_dot_cosim__pb2.SetBusyResponse.SerializeToString,
            ),
            'SubscribeEvents': grpc.unary_stream_rpc_method_handler(
                    servicer.SubscribeEvents,
                    request_deserializer=mathworks_dot_scenario_dot_simulation_dot_cosim__pb2.SubscribeEventsRequest.FromString,
                    response_serializer=mathworks_dot_scenario_dot_simulation_dot_event__pb2.Event.SerializeToString,
            ),
            'AddSimulations': grpc.unary_unary_rpc_method_handler(
                    servicer.AddSimulations,
                    request_deserializer=mathworks_dot_scenario_dot_simulation_dot_cosim__pb2.AddSimulationsRequest.FromString,
                    response_serializer=mathworks_dot_scenario_dot_simulation_dot_cosim__pb2.AddSimulationsResponse.SerializeToString,
            ),
            'RemoveSimulations': grpc.unary_unary_rpc_method_handler(
                    servicer.RemoveSimulations,
                    request_deserializer=mathworks_dot_scenario_dot_simulation_dot_cosim__pb2.RemoveSimulationsRequest.FromString,
                    response_serializer=mathworks_dot_scenario_dot_simulation_dot_cosim__pb2.RemoveSimulationsResponse.SerializeToString,
            ),
            'GetSimulationServiceProfiles': grpc.unary_unary_rpc_method_handler(
                    servicer.GetSimulationServiceProfiles,
                    request_deserializer=mathworks_dot_scenario_dot_simulation_dot_cosim__pb2.GetSimulationServiceProfilesRequest.FromString,
                    response_serializer=mathworks_dot_scenario_dot_simulation_dot_cosim__pb2.GetSimulationServiceProfilesResponse.SerializeToString,
            ),
            'LaunchSimulations': grpc.unary_unary_rpc_method_handler(
                    servicer.LaunchSimulations,
                    request_deserializer=mathworks_dot_scenario_dot_simulation_dot_cosim__pb2.LaunchSimulationsRequest.FromString,
                    response_serializer=mathworks_dot_scenario_dot_simulation_dot_cosim__pb2.LaunchSimulationsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'mathworks.scenario.simulation.CoSimulationMgr', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('mathworks.scenario.simulation.CoSimulationMgr', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class CoSimulationMgr(object):
    """gRPC service interface for management of multiple co-simulations
    ////////////////////////////////////
    Client connection and subscriptions
    ////////////////////////////////////
    """

    @staticmethod
    def RegisterClient(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/mathworks.scenario.simulation.CoSimulationMgr/RegisterClient',
            mathworks_dot_scenario_dot_simulation_dot_cosim__pb2.RegisterClientRequest.SerializeToString,
            mathworks_dot_scenario_dot_simulation_dot_cosim__pb2.RegisterClientResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def SetReady(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/mathworks.scenario.simulation.CoSimulationMgr/SetReady',
            mathworks_dot_scenario_dot_simulation_dot_cosim__pb2.SetReadyRequest.SerializeToString,
            mathworks_dot_scenario_dot_simulation_dot_cosim__pb2.SetReadyResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def SetBusy(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/mathworks.scenario.simulation.CoSimulationMgr/SetBusy',
            mathworks_dot_scenario_dot_simulation_dot_cosim__pb2.SetBusyRequest.SerializeToString,
            mathworks_dot_scenario_dot_simulation_dot_cosim__pb2.SetBusyResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def SubscribeEvents(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(
            request,
            target,
            '/mathworks.scenario.simulation.CoSimulationMgr/SubscribeEvents',
            mathworks_dot_scenario_dot_simulation_dot_cosim__pb2.SubscribeEventsRequest.SerializeToString,
            mathworks_dot_scenario_dot_simulation_dot_event__pb2.Event.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def AddSimulations(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/mathworks.scenario.simulation.CoSimulationMgr/AddSimulations',
            mathworks_dot_scenario_dot_simulation_dot_cosim__pb2.AddSimulationsRequest.SerializeToString,
            mathworks_dot_scenario_dot_simulation_dot_cosim__pb2.AddSimulationsResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def RemoveSimulations(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/mathworks.scenario.simulation.CoSimulationMgr/RemoveSimulations',
            mathworks_dot_scenario_dot_simulation_dot_cosim__pb2.RemoveSimulationsRequest.SerializeToString,
            mathworks_dot_scenario_dot_simulation_dot_cosim__pb2.RemoveSimulationsResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetSimulationServiceProfiles(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/mathworks.scenario.simulation.CoSimulationMgr/GetSimulationServiceProfiles',
            mathworks_dot_scenario_dot_simulation_dot_cosim__pb2.GetSimulationServiceProfilesRequest.SerializeToString,
            mathworks_dot_scenario_dot_simulation_dot_cosim__pb2.GetSimulationServiceProfilesResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def LaunchSimulations(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/mathworks.scenario.simulation.CoSimulationMgr/LaunchSimulations',
            mathworks_dot_scenario_dot_simulation_dot_cosim__pb2.LaunchSimulationsRequest.SerializeToString,
            mathworks_dot_scenario_dot_simulation_dot_cosim__pb2.LaunchSimulationsResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
