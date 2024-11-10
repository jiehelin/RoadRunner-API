# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: mathworks/scenario/scene/hd/hd_map.proto
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
    'mathworks/scenario/scene/hd/hd_map.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from mathworks.scenario.scene.hd import hd_lanes_pb2 as mathworks_dot_scenario_dot_scene_dot_hd_dot_hd__lanes__pb2
from mathworks.scenario.scene.hd import hd_lane_markings_pb2 as mathworks_dot_scenario_dot_scene_dot_hd_dot_hd__lane__markings__pb2
from mathworks.scenario.scene.hd import hd_junctions_pb2 as mathworks_dot_scenario_dot_scene_dot_hd_dot_hd__junctions__pb2
from mathworks.scenario.scene.hd import hd_barriers_pb2 as mathworks_dot_scenario_dot_scene_dot_hd_dot_hd__barriers__pb2
from mathworks.scenario.scene.hd import hd_signs_pb2 as mathworks_dot_scenario_dot_scene_dot_hd_dot_hd__signs__pb2
from mathworks.scenario.scene.hd import hd_static_objects_pb2 as mathworks_dot_scenario_dot_scene_dot_hd_dot_hd__static__objects__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n(mathworks/scenario/scene/hd/hd_map.proto\x12\x1emathworks.scenario.scene.hdmap\x1a*mathworks/scenario/scene/hd/hd_lanes.proto\x1a\x32mathworks/scenario/scene/hd/hd_lane_markings.proto\x1a.mathworks/scenario/scene/hd/hd_junctions.proto\x1a-mathworks/scenario/scene/hd/hd_barriers.proto\x1a*mathworks/scenario/scene/hd/hd_signs.proto\x1a\x33mathworks/scenario/scene/hd/hd_static_objects.proto\"\xe9\x05\n\x05HDMap\x12\x33\n\x05lanes\x18\x01 \x03(\x0b\x32$.mathworks.scenario.scene.hdmap.Lane\x12\x45\n\x0flane_boundaries\x18\x02 \x03(\x0b\x32,.mathworks.scenario.scene.hdmap.LaneBoundary\x12>\n\x0blane_groups\x18\x03 \x03(\x0b\x32).mathworks.scenario.scene.hdmap.LaneGroup\x12\x42\n\rlane_markings\x18\x04 \x03(\x0b\x32+.mathworks.scenario.scene.hdmap.LaneMarking\x12;\n\tjunctions\x18\x05 \x03(\x0b\x32(.mathworks.scenario.scene.hdmap.Junction\x12L\n\rbarrier_types\x18\x06 \x03(\x0b\x32\x35.mathworks.scenario.scene.hdmap.BarrierTypeDefinition\x12\x39\n\x08\x62\x61rriers\x18\x07 \x03(\x0b\x32\'.mathworks.scenario.scene.hdmap.Barrier\x12\x46\n\nsign_types\x18\x08 \x03(\x0b\x32\x32.mathworks.scenario.scene.hdmap.SignTypeDefinition\x12\x33\n\x05signs\x18\t \x03(\x0b\x32$.mathworks.scenario.scene.hdmap.Sign\x12W\n\x13static_object_types\x18\n \x03(\x0b\x32:.mathworks.scenario.scene.hdmap.StaticObjectTypeDefinition\x12\x44\n\x0estatic_objects\x18\x0b \x03(\x0b\x32,.mathworks.scenario.scene.hdmap.StaticObjectb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'mathworks.scenario.scene.hd.hd_map_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_HDMAP']._serialized_start=365
  _globals['_HDMAP']._serialized_end=1110
# @@protoc_insertion_point(module_scope)
