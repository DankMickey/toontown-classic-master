# File: L (Python 2.4)

from toontown.coghq.SpecImports import *
GlobalEntities = {
    1000: {
        'type': 'levelMgr',
        'name': 'LevelMgr',
        'comment': '',
        'parentEntId': 0,
        'cogLevel': 0,
        'farPlaneDistance': 1500,
        'modelFilename': 'phase_10/models/cashbotHQ/ZONE08a',
        'wantDoors': 1 },
    1001: {
        'type': 'editMgr',
        'name': 'EditMgr',
        'parentEntId': 0,
        'insertEntity': None,
        'removeEntity': None,
        'requestNewEntity': None,
        'requestSave': None },
    0: {
        'type': 'zone',
        'name': 'UberZone',
        'comment': '',
        'parentEntId': 0,
        'scale': 1,
        'description': '',
        'visibility': [] },
    10055: {
        'type': 'attribModifier',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 10001,
        'attribName': 'modelPath',
        'recursive': 1,
        'typeName': 'model',
        'value': '' },
    10001: {
        'type': 'nodepath',
        'name': 'crates',
        'comment': '',
        'parentEntId': 10028,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': Vec3(1.3, 1.3, 1.6489199999999999) },
    10002: {
        'type': 'nodepath',
        'name': 'rewardBarrels',
        'comment': '',
        'parentEntId': 0,
        'pos': Point3(-0.71973399999999998, 56.969099999999997, 10.0021),
        'hpr': Vec3(61.699199999999998, 0, 0),
        'scale': Vec3(1, 1, 1) },
    10003: {
        'type': 'nodepath',
        'name': 'upperWall',
        'comment': 'TODO: replace with lines of shelves',
        'parentEntId': 0,
        'pos': Point3(-20.3203, 52.654899999999998, 9.9087300000000003),
        'hpr': Vec3(270, 0, 0),
        'scale': Vec3(1.1143000000000001, 1.1143000000000001, 1.1143000000000001) },
    10009: {
        'type': 'nodepath',
        'name': 'toGear0',
        'comment': '',
        'parentEntId': 10001,
        'pos': Point3(-26.5593, 31.856000000000002, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': Vec3(1, 1, 1) },
    10011: {
        'type': 'nodepath',
        'name': 'toGear1',
        'comment': '',
        'parentEntId': 10001,
        'pos': Point3(-25.884, 13.674899999999999, 0),
        'hpr': Vec3(41.633499999999998, 0, 0),
        'scale': Vec3(1, 1, 1) },
    10023: {
        'type': 'nodepath',
        'name': 'leftWall',
        'comment': '',
        'parentEntId': 10003,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1 },
    10024: {
        'type': 'nodepath',
        'name': 'rightWall',
        'comment': '',
        'parentEntId': 10003,
        'pos': Point3(-26.711200000000002, 6.85982, 0),
        'hpr': Point3(180, 0, 0),
        'scale': Vec3(1, 1, 1) },
    10028: {
        'type': 'nodepath',
        'name': 'lowerPuzzle',
        'comment': '',
        'parentEntId': 0,
        'pos': Point3(0, 0, 0.050000000000000003),
        'hpr': Vec3(0, 0, 0),
        'scale': 1 },
    10029: {
        'type': 'nodepath',
        'name': 'entranceWall',
        'comment': '',
        'parentEntId': 10001,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1 },
    10032: {
        'type': 'nodepath',
        'name': 'props',
        'comment': '',
        'parentEntId': 0,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1 },
    10038: {
        'type': 'nodepath',
        'name': 'archStompers',
        'comment': '',
        'parentEntId': 10028,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1 },
    10040: {
        'type': 'nodepath',
        'name': 'backWall',
        'comment': '',
        'parentEntId': 10001,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1 },
    10044: {
        'type': 'nodepath',
        'name': 'gear',
        'comment': '',
        'parentEntId': 10028,
        'pos': Point3(11.85, -11.380000000000001, 12.528),
        'hpr': Vec3(0, 0, 0),
        'scale': Vec3(1, 1, 1) },
    10046: {
        'type': 'nodepath',
        'name': 'supportedCrateBackWall',
        'comment': '',
        'parentEntId': 10028,
        'pos': Point3(34.904499999999999, -34.058900000000001, -1.5168699999999999),
        'hpr': Vec3(63.434899999999999, 0, 0),
        'scale': Vec3(1, 1, 1) },
    10051: {
        'type': 'nodepath',
        'name': 'supportedCrateEntrance',
        'comment': '',
        'parentEntId': 10028,
        'pos': Point3(48.5077, 7.75915, 0.35789700000000002),
        'hpr': Point3(0, 0, 0),
        'scale': Vec3(1, 1, 1) },
    10059: {
        'type': 'nodepath',
        'name': 'largeStack',
        'comment': '',
        'parentEntId': 10029,
        'pos': Point3(47.979999999999997, -16.98, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1 },
    10061: {
        'type': 'nodepath',
        'name': 'lower',
        'comment': '',
        'parentEntId': 10059,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1 },
    100001: {
        'type': 'nodepath',
        'name': 'trap1 cog node',
        'comment': '',
        'parentEntId': 0,
        'pos': Point3(0, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': 1 },
    100003: {
        'type': 'path',
        'name': 'test goon path',
        'comment': '',
        'parentEntId': 0,
        'pos': Point3(-50.480800000000002, 0, 0),
        'hpr': Vec3(0, 0, 0),
        'scale': Vec3(1, 1, 1),
        'pathIndex': 0,
        'pathScale': 1.0 } }
Scenario0 = { }
levelSpec = {
    'globalEntities': GlobalEntities,
    'scenarios': [
        Scenario0] }