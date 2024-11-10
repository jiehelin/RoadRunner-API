# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: mathworks/scenario/simulation/simulation_status.proto
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
    'mathworks/scenario/simulation/simulation_status.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from mathworks.scenario.simulation import condition_status_pb2 as mathworks_dot_scenario_dot_simulation_dot_condition__status__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n5mathworks/scenario/simulation/simulation_status.proto\x12\x1dmathworks.scenario.simulation\x1a\x34mathworks/scenario/simulation/condition_status.proto\"\xce\x01\n\x13SimulationStopCause\x12\x0f\n\x07summary\x18\x01 \x01(\t\x12P\n\x13simulation_complete\x18\x02 \x01(\x0b\x32\x31.mathworks.scenario.simulation.SimulationCompleteH\x00\x12L\n\x11simulation_failed\x18\x03 \x01(\x0b\x32/.mathworks.scenario.simulation.SimulationFailedH\x00\x42\x06\n\x04type\"\xea\x01\n\x10SimulationFailed\x12\x46\n\x0e\x66\x61ilure_status\x18\x01 \x01(\x0b\x32,.mathworks.scenario.simulation.FailureStatusH\x00\x12\x42\n\x0c\x65ngine_error\x18\x02 \x01(\x0b\x32*.mathworks.scenario.simulation.EngineErrorH\x00\x12\x42\n\x0c\x63lient_error\x18\x03 \x01(\x0b\x32*.mathworks.scenario.simulation.ClientErrorH\x00\x42\x06\n\x04type\"O\n\rSuccessStatus\x12>\n\x06status\x18\x01 \x03(\x0b\x32..mathworks.scenario.simulation.ConditionStatus\"O\n\rFailureStatus\x12>\n\x06status\x18\x01 \x03(\x0b\x32..mathworks.scenario.simulation.ConditionStatus\"\r\n\x0b\x45ngineError\"\r\n\x0b\x43lientError\"\xf9\x01\n\x12SimulationComplete\x12\x46\n\x0esuccess_status\x18\x01 \x01(\x0b\x32,.mathworks.scenario.simulation.SuccessStatusH\x00\x12\x46\n\x0estop_requested\x18\x02 \x01(\x0b\x32,.mathworks.scenario.simulation.StopRequestedH\x00\x12K\n\x11stop_time_reached\x18\x03 \x01(\x0b\x32..mathworks.scenario.simulation.StopTimeReachedH\x00\x42\x06\n\x04type\"\"\n\rStopRequested\x12\x11\n\tclient_id\x18\x01 \x01(\t\"\x11\n\x0fStopTimeReached*\x91\x01\n\x10SimulationStatus\x12!\n\x1dSIMULATION_STATUS_UNSPECIFIED\x10\x00\x12\x1d\n\x19SIMULATION_STATUS_STOPPED\x10\x01\x12\x1d\n\x19SIMULATION_STATUS_RUNNING\x10\x02\x12\x1c\n\x18SIMULATION_STATUS_PAUSED\x10\x03\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'mathworks.scenario.simulation.simulation_status_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_SIMULATIONSTATUS']._serialized_start=1088
  _globals['_SIMULATIONSTATUS']._serialized_end=1233
  _globals['_SIMULATIONSTOPCAUSE']._serialized_start=143
  _globals['_SIMULATIONSTOPCAUSE']._serialized_end=349
  _globals['_SIMULATIONFAILED']._serialized_start=352
  _globals['_SIMULATIONFAILED']._serialized_end=586
  _globals['_SUCCESSSTATUS']._serialized_start=588
  _globals['_SUCCESSSTATUS']._serialized_end=667
  _globals['_FAILURESTATUS']._serialized_start=669
  _globals['_FAILURESTATUS']._serialized_end=748
  _globals['_ENGINEERROR']._serialized_start=750
  _globals['_ENGINEERROR']._serialized_end=763
  _globals['_CLIENTERROR']._serialized_start=765
  _globals['_CLIENTERROR']._serialized_end=778
  _globals['_SIMULATIONCOMPLETE']._serialized_start=781
  _globals['_SIMULATIONCOMPLETE']._serialized_end=1030
  _globals['_STOPREQUESTED']._serialized_start=1032
  _globals['_STOPREQUESTED']._serialized_end=1066
  _globals['_STOPTIMEREACHED']._serialized_start=1068
  _globals['_STOPTIMEREACHED']._serialized_end=1085
# @@protoc_insertion_point(module_scope)
