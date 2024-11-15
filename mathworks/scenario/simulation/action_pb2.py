# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: mathworks/scenario/simulation/action.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    2,
    '',
    'mathworks/scenario/simulation/action.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from mathworks.scenario.common import geometry_pb2 as mathworks_dot_scenario_dot_common_dot_geometry__pb2
from mathworks.scenario.simulation import attributes_pb2 as mathworks_dot_scenario_dot_simulation_dot_attributes__pb2
from mathworks.scenario.simulation import comparison_pb2 as mathworks_dot_scenario_dot_simulation_dot_comparison__pb2
from mathworks.scenario.simulation import custom_command_pb2 as mathworks_dot_scenario_dot_simulation_dot_custom__command__pb2
from mathworks.scenario.simulation import targets_pb2 as mathworks_dot_scenario_dot_simulation_dot_targets__pb2
from mathworks.scenario.simulation import transition_dynamics_pb2 as mathworks_dot_scenario_dot_simulation_dot_transition__dynamics__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*mathworks/scenario/simulation/action.proto\x12\x1dmathworks.scenario.simulation\x1a(mathworks/scenario/common/geometry.proto\x1a.mathworks/scenario/simulation/attributes.proto\x1a.mathworks/scenario/simulation/comparison.proto\x1a\x32mathworks/scenario/simulation/custom_command.proto\x1a+mathworks/scenario/simulation/targets.proto\x1a\x37mathworks/scenario/simulation/transition_dynamics.proto\"\xa6\x01\n\x06\x41\x63tion\x12\n\n\x02id\x18\x01 \x01(\t\x12\x42\n\x0c\x61\x63tor_action\x18\x65 \x01(\x0b\x32*.mathworks.scenario.simulation.ActorActionH\x00\x12\x44\n\rsystem_action\x18\x66 \x01(\x0b\x32+.mathworks.scenario.simulation.SystemActionH\x00\x42\x06\n\x04type\"\xbf\x06\n\x0b\x41\x63torAction\x12\x10\n\x08\x61\x63tor_id\x18\x01 \x01(\t\x12\x44\n\x0ephase_interval\x18\x02 \x01(\x0e\x32,.mathworks.scenario.simulation.PhaseInterval\x12M\n\x12lane_change_action\x18\x65 \x01(\x0b\x32/.mathworks.scenario.simulation.LaneChangeActionH\x00\x12@\n\x0bpath_action\x18\x66 \x01(\x0b\x32).mathworks.scenario.simulation.PathActionH\x00\x12H\n\x0fposition_action\x18g \x01(\x0b\x32-.mathworks.scenario.simulation.PositionActionH\x00\x12\x42\n\x0cspeed_action\x18h \x01(\x0b\x32*.mathworks.scenario.simulation.SpeedActionH\x00\x12W\n\x17\x63hange_parameter_action\x18i \x01(\x0b\x32\x34.mathworks.scenario.simulation.ChangeParameterActionH\x00\x12S\n\x15lateral_offset_action\x18j \x01(\x0b\x32\x32.mathworks.scenario.simulation.LateralOffsetActionH\x00\x12\x61\n\x1clongitudinal_distance_action\x18k \x01(\x0b\x32\x39.mathworks.scenario.simulation.LongitudinalDistanceActionH\x00\x12O\n\x13user_defined_action\x18l \x01(\x0b\x32\x30.mathworks.scenario.simulation.UserDefinedActionH\x00\x12O\n\x13remove_actor_action\x18m \x01(\x0b\x32\x30.mathworks.scenario.simulation.RemoveActorActionH\x00\x42\x06\n\x04type\"\xbd\x01\n\x0bSpeedAction\x12@\n\x0cspeed_target\x18\x01 \x01(\x0b\x32*.mathworks.scenario.simulation.SpeedTarget\x12N\n\x13transition_dynamics\x18\x02 \x01(\x0b\x32\x31.mathworks.scenario.simulation.TransitionDynamics\x12\x1c\n\x14\x61llow_negative_speed\x18\x03 \x01(\x08\"\xaf\x01\n\x10LaneChangeAction\x12K\n\x12lane_change_target\x18\x01 \x01(\x0b\x32/.mathworks.scenario.simulation.LaneChangeTarget\x12N\n\x13transition_dynamics\x18\x02 \x01(\x0b\x32\x31.mathworks.scenario.simulation.TransitionDynamics\"\xbe\x01\n\x0ePositionAction\x12\x0f\n\x05value\x18\x01 \x01(\x01H\x00\x12;\n\x05range\x18\x02 \x01(\x0b\x32*.mathworks.scenario.simulation.DoubleRangeH\x00\x12L\n\x12position_reference\x18\x03 \x01(\x0b\x32\x30.mathworks.scenario.simulation.PositionReferenceB\x10\n\x0eposition_value\"\x7f\n\x11PositionReference\x12\x1a\n\x12reference_actor_id\x18\x01 \x01(\t\x12N\n\x13position_comparison\x18\x02 \x01(\x0e\x32\x31.mathworks.scenario.simulation.PositionComparison\"A\n\x0fPathPointTiming\x12\x0c\n\x04time\x18\x01 \x01(\x01\x12\r\n\x05speed\x18\x02 \x01(\x01\x12\x11\n\twait_time\x18\x03 \x01(\x01\"\xd2\x01\n\nPathAction\x12-\n\x04path\x18\x01 \x01(\x0b\x32\x1f.mathworks.scenario.common.Path\x12\x10\n\x08\x61\x63tor_id\x18\x02 \x01(\t\x12?\n\x07timings\x18\x03 \x03(\x0b\x32..mathworks.scenario.simulation.PathPointTiming\x12\x42\n\x12\x61\x63tor_orientations\x18\x04 \x03(\x0b\x32&.mathworks.scenario.common.Orientation\"\x9a\x01\n\x15\x43hangeParameterAction\x12;\n\tparameter\x18\x01 \x01(\x0b\x32(.mathworks.scenario.simulation.Attribute\x12\x44\n\x0eparameter_type\x18\x65 \x01(\x0e\x32,.mathworks.scenario.simulation.ParameterType\"\xbc\x01\n\x13LateralOffsetAction\x12Q\n\x15lateral_offset_target\x18\x01 \x01(\x0b\x32\x32.mathworks.scenario.simulation.LateralOffsetTarget\x12R\n\x13transition_dynamics\x18\x02 \x01(\x0b\x32\x35.mathworks.scenario.simulation.TimeTransitionDynamics\"\x8b\x02\n\x1aLongitudinalDistanceAction\x12\x46\n\x0f\x64istance_target\x18\x01 \x01(\x0b\x32-.mathworks.scenario.simulation.DistanceTarget\x12U\n\x17reference_sampling_mode\x18\x02 \x01(\x0e\x32\x34.mathworks.scenario.simulation.ReferenceSamplingMode\x12N\n\x13\x64ynamic_constraints\x18\x03 \x01(\x0b\x32\x31.mathworks.scenario.simulation.DynamicConstraints\"p\n\x11UserDefinedAction\x12\x44\n\x0e\x63ustom_command\x18\x01 \x01(\x0b\x32,.mathworks.scenario.simulation.CustomCommand\x12\x15\n\rinstantaneous\x18\x02 \x01(\x08\"\x13\n\x11RemoveActorAction\"\xbd\x02\n\x0cSystemAction\x12J\n\x10scenario_success\x18\x01 \x01(\x0b\x32..mathworks.scenario.simulation.ScenarioSuccessH\x00\x12J\n\x10scenario_failure\x18\x02 \x01(\x0b\x32..mathworks.scenario.simulation.ScenarioFailureH\x00\x12@\n\x0bwait_action\x18\x03 \x01(\x0b\x32).mathworks.scenario.simulation.WaitActionH\x00\x12K\n\x11send_event_action\x18\x04 \x01(\x0b\x32..mathworks.scenario.simulation.SendEventActionH\x00\x42\x06\n\x04type\"\x11\n\x0fScenarioSuccess\"\x11\n\x0fScenarioFailure\"\x0c\n\nWaitAction\"W\n\x0fSendEventAction\x12\x44\n\x0e\x63ustom_command\x18\x01 \x01(\x0b\x32,.mathworks.scenario.simulation.CustomCommand*\x85\x01\n\rPhaseInterval\x12\x1e\n\x1aPHASE_INTERVAL_UNSPECIFIED\x10\x00\x12\x1b\n\x17PHASE_INTERVAL_AT_START\x10\x01\x12\x19\n\x15PHASE_INTERVAL_AT_END\x10\x02\x12\x1c\n\x18PHASE_INTERVAL_INVARIANT\x10\x03*\xc0\x01\n\x11\x41\x63tionEventStatus\x12#\n\x1f\x41\x43TION_EVENT_STATUS_UNSPECIFIED\x10\x00\x12\"\n\x1e\x41\x43TION_EVENT_STATUS_DISPATCHED\x10\x01\x12#\n\x1f\x41\x43TION_EVENT_STATUS_INTERRUPTED\x10\x02\x12\x1f\n\x1b\x41\x43TION_EVENT_STATUS_SKIPPED\x10\x03\x12\x1c\n\x18\x41\x43TION_EVENT_STATUS_DONE\x10\x04\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'mathworks.scenario.simulation.action_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_PHASEINTERVAL']._serialized_start=3559
  _globals['_PHASEINTERVAL']._serialized_end=3692
  _globals['_ACTIONEVENTSTATUS']._serialized_start=3695
  _globals['_ACTIONEVENTSTATUS']._serialized_end=3887
  _globals['_ACTION']._serialized_start=370
  _globals['_ACTION']._serialized_end=536
  _globals['_ACTORACTION']._serialized_start=539
  _globals['_ACTORACTION']._serialized_end=1370
  _globals['_SPEEDACTION']._serialized_start=1373
  _globals['_SPEEDACTION']._serialized_end=1562
  _globals['_LANECHANGEACTION']._serialized_start=1565
  _globals['_LANECHANGEACTION']._serialized_end=1740
  _globals['_POSITIONACTION']._serialized_start=1743
  _globals['_POSITIONACTION']._serialized_end=1933
  _globals['_POSITIONREFERENCE']._serialized_start=1935
  _globals['_POSITIONREFERENCE']._serialized_end=2062
  _globals['_PATHPOINTTIMING']._serialized_start=2064
  _globals['_PATHPOINTTIMING']._serialized_end=2129
  _globals['_PATHACTION']._serialized_start=2132
  _globals['_PATHACTION']._serialized_end=2342
  _globals['_CHANGEPARAMETERACTION']._serialized_start=2345
  _globals['_CHANGEPARAMETERACTION']._serialized_end=2499
  _globals['_LATERALOFFSETACTION']._serialized_start=2502
  _globals['_LATERALOFFSETACTION']._serialized_end=2690
  _globals['_LONGITUDINALDISTANCEACTION']._serialized_start=2693
  _globals['_LONGITUDINALDISTANCEACTION']._serialized_end=2960
  _globals['_USERDEFINEDACTION']._serialized_start=2962
  _globals['_USERDEFINEDACTION']._serialized_end=3074
  _globals['_REMOVEACTORACTION']._serialized_start=3076
  _globals['_REMOVEACTORACTION']._serialized_end=3095
  _globals['_SYSTEMACTION']._serialized_start=3098
  _globals['_SYSTEMACTION']._serialized_end=3415
  _globals['_SCENARIOSUCCESS']._serialized_start=3417
  _globals['_SCENARIOSUCCESS']._serialized_end=3434
  _globals['_SCENARIOFAILURE']._serialized_start=3436
  _globals['_SCENARIOFAILURE']._serialized_end=3453
  _globals['_WAITACTION']._serialized_start=3455
  _globals['_WAITACTION']._serialized_end=3467
  _globals['_SENDEVENTACTION']._serialized_start=3469
  _globals['_SENDEVENTACTION']._serialized_end=3556
# @@protoc_insertion_point(module_scope)
